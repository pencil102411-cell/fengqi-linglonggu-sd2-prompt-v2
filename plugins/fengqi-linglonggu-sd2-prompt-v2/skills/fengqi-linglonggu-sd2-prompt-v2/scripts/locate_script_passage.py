from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path


PAGE_MARKER_RE = re.compile(r"^<<<PDF_PAGE:\d{3}>>>$")
NOISE_LINE_RE = re.compile(
    r"^\s*(?:AI\s*组\s*专\s*享|\d{1,3}/\d{1,3}|260628)\s*$",
    re.IGNORECASE,
)


def sha256_bytes(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def normalize(text: str) -> str:
    value = unicodedata.normalize("NFKC", text).lower()
    return "".join(char for char in value if char.isalnum())


def ngrams(text: str, size: int) -> set[str]:
    if len(text) < size:
        return {text} if text else set()
    return {text[index : index + size] for index in range(len(text) - size + 1)}


def load_index(corpus_root: Path) -> list[dict[str, object]]:
    index_path = corpus_root / "scene-index.jsonl"
    return [
        json.loads(line)
        for line in index_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def load_scene_texts(
    corpus_root: Path, records: list[dict[str, object]]
) -> list[str]:
    cache: dict[str, list[str]] = {}
    scenes: list[str] = []
    for record in records:
        source_file = str(record["source_file"])
        if source_file not in cache:
            cache[source_file] = (
                corpus_root / "episodes" / source_file
            ).read_text(encoding="utf-8").splitlines()
        lines = cache[source_file]
        start = int(record["start_line"]) - 1
        end = int(record["end_line"])
        visible = [
            line
            for line in lines[start:end]
            if line.strip()
            and not PAGE_MARKER_RE.match(line)
            and not NOISE_LINE_RE.match(line)
        ]
        scenes.append("\n".join(visible))
    return scenes


def context_signal(query_norm: str, record: dict[str, object]) -> float:
    terms: list[str] = [str(record.get("heading", ""))]
    terms.extend(str(value) for value in record.get("present_characters", []))
    terms.extend(str(value) for value in record.get("speaker_cues", []))
    normalized_terms = [normalize(term) for term in terms]
    direct = [term for term in normalized_terms if len(term) >= 2 and term in query_norm]
    if direct:
        return 1.0
    heading_parts = re.split(r"[/／\s-]+", str(record.get("heading", "")))
    if any(
        len(part_norm := normalize(part)) >= 2 and part_norm in query_norm
        for part in heading_parts
    ):
        return 0.7
    return 0.0


def classify(score: float, exact: bool) -> str:
    if exact:
        return "exact_text"
    if score >= 0.78:
        return "near_verbatim"
    if score >= 0.56:
        return "strong_candidate"
    if score >= 0.32:
        return "candidate"
    return "weak_candidate"


def locate(
    corpus_root: Path,
    query: str,
    top: int,
    episode_filter: int | None,
) -> dict[str, object]:
    records = load_index(corpus_root)
    if episode_filter is not None:
        records = [
            record for record in records if int(record["episode"]) == episode_filter
        ]
    scene_texts = load_scene_texts(corpus_root, records)
    normalized_scenes = [normalize(text) for text in scene_texts]
    query_norm = normalize(query)
    if len(query_norm) < 4:
        raise ValueError("Query must contain at least four searchable characters")

    sizes = [size for size in (2, 3, 4) if len(query_norm) >= size]
    query_grams = {size: ngrams(query_norm, size) for size in sizes}
    document_frequency: Counter[tuple[int, str]] = Counter()
    scene_gram_sets: list[dict[int, set[str]]] = []
    for scene_norm in normalized_scenes:
        per_size = {size: ngrams(scene_norm, size) for size in sizes}
        scene_gram_sets.append(per_size)
        for size, grams_for_size in query_grams.items():
            for gram in grams_for_size & per_size[size]:
                document_frequency[(size, gram)] += 1

    total_documents = max(len(records), 1)
    denominator = 0.0
    weights: dict[tuple[int, str], float] = {}
    for size, grams_for_size in query_grams.items():
        for gram in grams_for_size:
            idf = math.log((total_documents + 1) / (document_frequency[(size, gram)] + 1)) + 1
            weight = (size - 1) * idf
            weights[(size, gram)] = weight
            denominator += weight

    ranked: list[dict[str, object]] = []
    for record, scene_norm, per_size in zip(records, normalized_scenes, scene_gram_sets):
        exact = query_norm in scene_norm or (
            len(scene_norm) >= 12 and scene_norm in query_norm
        )
        matched_weight = 0.0
        for size, grams_for_size in query_grams.items():
            for gram in grams_for_size & per_size[size]:
                matched_weight += weights[(size, gram)]
        lexical_coverage = matched_weight / denominator if denominator else 0.0
        matcher = SequenceMatcher(None, query_norm, scene_norm, autojunk=False)
        longest = matcher.find_longest_match(0, len(query_norm), 0, len(scene_norm))
        contiguous_coverage = longest.size / len(query_norm)
        ordered_coverage = (
            sum(block.size for block in matcher.get_matching_blocks()) / len(query_norm)
        )
        context = context_signal(query_norm, record)
        score = (
            1.0
            if exact
            else min(
                0.99,
                0.50 * lexical_coverage
                + 0.30 * ordered_coverage
                + 0.12 * contiguous_coverage
                + 0.08 * context,
            )
        )
        ranked.append(
            {
                "episode": record["episode"],
                "scene_id": record["scene_id"],
                "scene_label": record["scene_label"],
                "heading": record["heading"],
                "source_file": record["source_file"],
                "source_pdf": record["source_pdf"],
                "source_pdf_pages": [
                    record["source_pdf_page_start"],
                    record["source_pdf_page_end"],
                ],
                "line_range": [record["start_line"], record["end_line"]],
                "first_anchor": record["first_anchor"],
                "last_anchor": record["last_anchor"],
                "score": round(score, 6),
                "match_type": classify(score, exact),
                "signals": {
                    "lexical_coverage": round(lexical_coverage, 6),
                    "ordered_coverage": round(ordered_coverage, 6),
                    "contiguous_coverage": round(contiguous_coverage, 6),
                    "context": round(context, 6),
                },
            }
        )
    ranked.sort(
        key=lambda item: (
            -float(item["score"]),
            int(item["episode"]),
            str(item["scene_id"]),
        )
    )
    selected = ranked[: max(1, top)]
    best_score = float(selected[0]["score"]) if selected else 0.0
    second_score = float(selected[1]["score"]) if len(selected) > 1 else 0.0
    margin = best_score - second_score
    best_type = str(selected[0]["match_type"]) if selected else "none"
    exact_count = sum(1 for item in ranked if item["match_type"] == "exact_text")
    if len(query_norm) < 6:
        confidence = "MEDIUM" if best_type == "exact_text" and exact_count == 1 else "INSUFFICIENT"
    elif best_type == "exact_text" or (best_score >= 0.85 and margin >= 0.10):
        confidence = "HIGH"
    elif best_score >= 0.62 and margin >= 0.04:
        confidence = "MEDIUM"
    elif best_score >= 0.32:
        confidence = "LOW"
    else:
        confidence = "INSUFFICIENT"
    return {
        "status": "candidates_only",
        "confidence": confidence,
        "top_score_margin": round(margin, 6),
        "source_verification_required": True,
        "generator_facing": False,
        "candidates": selected,
    }


def validate(corpus_root: Path) -> dict[str, object]:
    manifest_path = corpus_root / "corpus-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []

    episode_files = sorted((corpus_root / "episodes").glob("episode-*.txt"))
    expected_names = [f"episode-{number:02d}.txt" for number in range(1, 25)]
    if [path.name for path in episode_files] != expected_names:
        errors.append("Episode files are not exactly episode-01.txt through episode-24.txt")

    source_hashes: list[str] = []
    source_pages: dict[str, int] = {}
    for source in manifest["sources"]:
        path = corpus_root / "originals" / source["file"]
        actual = sha256_bytes(path)
        source_hashes.append(actual)
        source_pages[str(source["file"])] = int(source["pages"])
        if actual != source["sha256"]:
            errors.append(f"Source hash mismatch: {source['file']}")

    episode_hashes: list[str] = []
    episode_lines: dict[str, list[str]] = {}
    page_ranges: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for episode in manifest["episodes"]:
        path = corpus_root / "episodes" / episode["file"]
        text = path.read_text(encoding="utf-8")
        actual = sha256_text(text)
        episode_hashes.append(actual)
        episode_lines[episode["file"]] = text.splitlines()
        if actual != episode["sha256"]:
            errors.append(f"Episode hash mismatch: {episode['file']}")
        page_start, page_end = (int(value) for value in episode["source_pdf_pages"])
        page_ranges[str(episode["source_pdf"])].append((page_start, page_end))

    for source_file, page_count in source_pages.items():
        covered: list[int] = []
        for start, end in sorted(page_ranges[source_file]):
            covered.extend(range(start, end + 1))
        if covered != list(range(1, page_count + 1)):
            errors.append(f"Source page coverage mismatch: {source_file}")

    index_path = corpus_root / manifest["scene_index"]["file"]
    index_text = index_path.read_text(encoding="utf-8")
    index_hash = sha256_text(index_text)
    if index_hash != manifest["scene_index"]["sha256"]:
        errors.append("Scene index hash mismatch")
    records = [json.loads(line) for line in index_text.splitlines() if line.strip()]
    scene_ids: set[str] = set()
    records_by_episode: dict[int, list[dict[str, object]]] = defaultdict(list)
    for record in records:
        scene_id = str(record["scene_id"])
        if scene_id in scene_ids:
            errors.append(f"Duplicate scene_id: {scene_id}")
        scene_ids.add(scene_id)
        records_by_episode[int(record["episode"])].append(record)
        lines = episode_lines[str(record["source_file"])]
        start = int(record["start_line"]) - 1
        end = int(record["end_line"])
        if not (0 <= start < end <= len(lines)):
            errors.append(f"Invalid line range: {scene_id}")
            continue
        body_lines = [
            line
            for line in lines[start:end]
            if line.strip() and not PAGE_MARKER_RE.match(line)
        ]
        if sha256_text("\n".join(body_lines)) != record["text_sha256"]:
            errors.append(f"Scene text hash mismatch: {scene_id}")

    episode_scene_counts = {
        int(episode["episode"]): int(episode["scene_count"])
        for episode in manifest["episodes"]
    }
    for episode, episode_records in sorted(records_by_episode.items()):
        ordered = sorted(episode_records, key=lambda record: int(record["scene_order"]))
        expected_orders = list(range(1, len(ordered) + 1))
        actual_orders = [int(record["scene_order"]) for record in ordered]
        if actual_orders != expected_orders:
            errors.append(f"Scene order mismatch: episode {episode}")
        if len(ordered) != episode_scene_counts.get(episode):
            errors.append(f"Episode scene count mismatch: episode {episode}")
        for index, record in enumerate(ordered):
            previous_id = ordered[index - 1]["scene_id"] if index else None
            next_id = ordered[index + 1]["scene_id"] if index + 1 < len(ordered) else None
            if record.get("previous_scene_id") != previous_id:
                errors.append(f"Previous-scene link mismatch: {record['scene_id']}")
            if record.get("next_scene_id") != next_id:
                errors.append(f"Next-scene link mismatch: {record['scene_id']}")

    root_payload = json.dumps(
        {
            "sources": source_hashes,
            "episodes": episode_hashes,
            "scene_index": index_hash,
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )
    if sha256_text(root_payload) != manifest["corpus_root_sha256"]:
        errors.append("Corpus root hash mismatch")
    if len(records) != int(manifest["scene_count"]):
        errors.append("Scene count does not match manifest")

    return {
        "status": "PASS" if not errors else "FAIL",
        "episode_count": len(episode_files),
        "source_pdf_count": len(manifest["sources"]),
        "source_page_count": manifest["source_page_count"],
        "scene_count": len(records),
        "corpus_root_sha256": manifest["corpus_root_sha256"],
        "errors": errors,
    }


def main() -> None:
    skill_root = Path(__file__).resolve().parent.parent
    corpus_root = skill_root / "references" / "scripts"
    parser = argparse.ArgumentParser(
        description="Validate or reverse-locate passages in the 风起玲珑骨 script corpus."
    )
    parser.add_argument("query", nargs="?", help="Storyboard or plot text to locate")
    parser.add_argument("--query-file", type=Path)
    parser.add_argument("--episode", type=int, choices=range(1, 25))
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args()

    if args.validate:
        result = validate(corpus_root)
    else:
        query = args.query
        if args.query_file:
            query = args.query_file.read_text(encoding="utf-8")
        if not query:
            parser.error("Provide query text, --query-file, or --validate")
        result = locate(corpus_root, query, args.top, args.episode)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result.get("status") == "FAIL":
        raise SystemExit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover - command-line failure path
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
