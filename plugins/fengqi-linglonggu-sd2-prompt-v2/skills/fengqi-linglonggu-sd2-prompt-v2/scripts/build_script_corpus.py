from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

import pypdf
from pypdf import PdfReader


EPISODE_HEADING_RE = re.compile(r"第\s*([0-9一二三四五六七八九十百]+)\s*集")
NUMBERED_SCENE_RE = re.compile(
    r"^\s*(\d+(?:\s*[-—－]\s*\d+)?[A-Za-z]?)\s*[.．、]\s*(\S.*?)\s*$"
)
BARE_NUMBERED_SCENE_RE = re.compile(
    r"^\s*(\d+(?:\s*[-—－]\s*\d+)?[A-Za-z]?)\s+(\S.*?)\s*$"
)
PREFACE_SCENE_RE = re.compile(
    r"^\s*(序(?:\s*[-—]\s*\d+)?)\s+(\S.*?)\s*$"
)
PRESENT_CHARACTERS_RE = re.compile(r"^\s*在场角色\s*[：:]\s*(.+?)\s*$")
SPEAKER_CUE_RE = re.compile(r"^\s*([^：:\n]{1,24})\s*[：:]\s*\S")
PAGE_MARKER_RE = re.compile(r"^<<<PDF_PAGE:(\d{3})>>>$")
NOISE_LINE_RE = re.compile(
    r"^\s*(?:AI\s*组\s*专\s*享|\d{1,3}/\d{1,3}|260628)\s*$",
    re.IGNORECASE,
)

SCENE_HEADING_END_RE = re.compile(
    r"(?:凌晨|清晨|黄昏|傍晚|晨|昏|夕|日|夜)"
    r"(?:转(?:凌晨|清晨|黄昏|傍晚|晨|昏|夕|日|夜))?"
    r"(?:[/／](?:日|夜))?\s+"
    r"(?:内到外|外到内|内|外)(?:[/／](?:内|外))?\s*$"
)

CN_DIGITS = {
    "零": 0,
    "〇": 0,
    "一": 1,
    "二": 2,
    "两": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
}
CN_UNITS = {"十": 10, "百": 100}


@dataclass(frozen=True)
class EpisodeStart:
    episode: int
    source_pdf: Path
    page_index: int


def sha256_bytes(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def chinese_number_to_int(raw: str) -> int:
    value = unicodedata.normalize("NFKC", raw).strip()
    if value.isdigit():
        return int(value)
    total = 0
    current = 0
    for char in value:
        if char in CN_DIGITS:
            current = CN_DIGITS[char]
        elif char in CN_UNITS:
            unit = CN_UNITS[char]
            total += (current or 1) * unit
            current = 0
        else:
            raise ValueError(f"Unsupported Chinese numeral: {raw!r}")
    return total + current


def find_episode_number(text: str) -> int | None:
    # A real episode title appears near the top of a fresh PDF page. Restricting
    # the search avoids treating dialogue about another episode as a boundary.
    head = text[:500]
    match = EPISODE_HEADING_RE.search(head)
    if not match:
        return None
    return chinese_number_to_int(match.group(1))


def scene_header(line: str) -> tuple[str, str] | None:
    match = (
        NUMBERED_SCENE_RE.match(line)
        or BARE_NUMBERED_SCENE_RE.match(line)
        or PREFACE_SCENE_RE.match(line)
    )
    if not match:
        return None
    label = re.sub(r"\s+", "", match.group(1)).replace("—", "-")
    heading = match.group(2).strip()
    if len(heading) > 160:
        return None
    if label.startswith("序") or SCENE_HEADING_END_RE.search(heading):
        return label, heading
    return None


def clean_anchor(line: str, limit: int = 100) -> str:
    compact = re.sub(r"\s+", " ", line).strip()
    return compact if len(compact) <= limit else compact[: limit - 1] + "…"


def split_people(raw: str) -> list[str]:
    people = re.split(r"[、,，/／\s]+", raw.strip())
    return [person for person in people if person]


def build_scene_records(
    episode: int,
    episode_file: Path,
    source_pdf_name: str,
    lines: list[str],
) -> list[dict[str, object]]:
    page_for_line: list[int | None] = []
    current_page: int | None = None
    starts: list[tuple[int, str, str, int | None]] = []
    for index, line in enumerate(lines):
        marker = PAGE_MARKER_RE.match(line)
        if marker:
            current_page = int(marker.group(1))
        page_for_line.append(current_page)
        parsed = scene_header(line)
        if parsed:
            starts.append((index, parsed[0], parsed[1], current_page))

    records: list[dict[str, object]] = []
    for order, (start, label, heading, start_page) in enumerate(starts, start=1):
        end = starts[order][0] - 1 if order < len(starts) else len(lines) - 1
        body_lines = [
            line
            for line in lines[start : end + 1]
            if line.strip() and not PAGE_MARKER_RE.match(line)
        ]
        visible_body = body_lines[1:] if len(body_lines) > 1 else body_lines
        search_body = [line for line in visible_body if not NOISE_LINE_RE.match(line)]
        present_characters: list[str] = []
        speaker_cues: list[str] = []
        for line in search_body:
            present = PRESENT_CHARACTERS_RE.match(line)
            if present:
                present_characters.extend(split_people(present.group(1)))
            speaker = SPEAKER_CUE_RE.match(line)
            if speaker:
                cue = re.sub(r"\s+", " ", speaker.group(1)).strip()
                if cue not in speaker_cues:
                    speaker_cues.append(cue)
        first_anchor = clean_anchor(search_body[0]) if search_body else ""
        last_anchor = clean_anchor(search_body[-1]) if search_body else ""
        scene_text = "\n".join(body_lines)
        end_page = next(
            (page for page in reversed(page_for_line[start : end + 1]) if page is not None),
            start_page,
        )
        records.append(
            {
                "schema_version": "1.0",
                "corpus_version": "final-episodes-01-24-v1",
                "episode": episode,
                "scene_id": f"E{episode:02d}-S{order:03d}",
                "scene_order": order,
                "scene_label": label,
                "heading": heading,
                "source_file": episode_file.name,
                "source_pdf": source_pdf_name,
                "source_pdf_page_start": start_page,
                "source_pdf_page_end": end_page,
                "start_line": start + 1,
                "end_line": end + 1,
                "present_characters": list(dict.fromkeys(present_characters)),
                "speaker_cues": speaker_cues,
                "first_anchor": first_anchor,
                "last_anchor": last_anchor,
                "text_sha256": sha256_text(scene_text),
            }
        )
    for index, record in enumerate(records):
        record["previous_scene_id"] = records[index - 1]["scene_id"] if index else None
        record["next_scene_id"] = (
            records[index + 1]["scene_id"] if index + 1 < len(records) else None
        )
    return records


def build(skill_root: Path) -> dict[str, object]:
    corpus_root = skill_root / "references" / "scripts"
    originals_dir = corpus_root / "originals"
    episodes_dir = corpus_root / "episodes"
    episodes_dir.mkdir(parents=True, exist_ok=True)

    pdf_paths = sorted(originals_dir.glob("*.pdf"), key=lambda path: path.name)
    if not pdf_paths:
        raise FileNotFoundError(f"No source PDFs found in {originals_dir}")

    pdf_data: dict[Path, dict[str, object]] = {}
    all_starts: list[EpisodeStart] = []
    source_manifest: list[dict[str, object]] = []
    for pdf_path in pdf_paths:
        reader = PdfReader(str(pdf_path))
        page_texts = [(page.extract_text() or "") for page in reader.pages]
        starts: list[dict[str, int]] = []
        for page_index, text in enumerate(page_texts):
            episode = find_episode_number(text)
            if episode is None:
                continue
            starts.append({"episode": episode, "page": page_index + 1})
            all_starts.append(EpisodeStart(episode, pdf_path, page_index))
        pdf_data[pdf_path] = {"reader": reader, "page_texts": page_texts}
        source_manifest.append(
            {
                "file": pdf_path.name,
                "bytes": pdf_path.stat().st_size,
                "sha256": sha256_bytes(pdf_path),
                "pages": len(reader.pages),
                "episode_starts": starts,
            }
        )

    seen: dict[int, EpisodeStart] = {}
    for start in all_starts:
        if start.episode in seen:
            raise ValueError(
                f"Duplicate episode heading for episode {start.episode}: "
                f"{seen[start.episode].source_pdf.name} and {start.source_pdf.name}"
            )
        seen[start.episode] = start
    expected = set(range(1, 25))
    actual = set(seen)
    if actual != expected:
        raise ValueError(
            f"Episode coverage mismatch; missing={sorted(expected - actual)}, "
            f"unexpected={sorted(actual - expected)}"
        )

    episode_manifest: list[dict[str, object]] = []
    all_scene_records: list[dict[str, object]] = []
    for pdf_path, data in pdf_data.items():
        page_texts = data["page_texts"]
        assert isinstance(page_texts, list)
        pdf_starts = sorted(
            (start for start in all_starts if start.source_pdf == pdf_path),
            key=lambda start: start.page_index,
        )
        for position, start in enumerate(pdf_starts):
            end_index = (
                pdf_starts[position + 1].page_index
                if position + 1 < len(pdf_starts)
                else len(page_texts)
            )
            output_path = episodes_dir / f"episode-{start.episode:02d}.txt"
            output_lines: list[str] = []
            for page_index in range(start.page_index, end_index):
                output_lines.append(f"<<<PDF_PAGE:{page_index + 1:03d}>>>")
                output_lines.extend(str(page_texts[page_index]).splitlines())
                output_lines.append("")
            output_text = "\n".join(output_lines).rstrip() + "\n"
            output_path.write_text(output_text, encoding="utf-8", newline="\n")
            scene_records = build_scene_records(
                start.episode,
                output_path,
                pdf_path.name,
                output_text.splitlines(),
            )
            all_scene_records.extend(scene_records)
            episode_manifest.append(
                {
                    "episode": start.episode,
                    "file": output_path.name,
                    "sha256": sha256_text(output_text),
                    "chars": len(output_text),
                    "lines": len(output_text.splitlines()),
                    "source_pdf": pdf_path.name,
                    "source_pdf_pages": [start.page_index + 1, end_index],
                    "scene_count": len(scene_records),
                }
            )

    episode_manifest.sort(key=lambda item: int(item["episode"]))
    all_scene_records.sort(
        key=lambda item: (int(item["episode"]), int(item["scene_order"]))
    )
    index_path = corpus_root / "scene-index.jsonl"
    index_text = "".join(
        json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
        for record in all_scene_records
    )
    index_path.write_text(index_text, encoding="utf-8", newline="\n")

    scene_index_sha256 = sha256_text(index_text)
    root_payload = json.dumps(
        {
            "sources": [source["sha256"] for source in source_manifest],
            "episodes": [episode["sha256"] for episode in episode_manifest],
            "scene_index": scene_index_sha256,
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )
    manifest = {
        "project": "风起玲珑骨",
        "corpus_role": "evidence_only",
        "authority": "copied source PDFs; searchable text is a mechanical extraction",
        "episode_coverage": [1, 24],
        "episode_count": len(episode_manifest),
        "source_pdf_count": len(source_manifest),
        "source_page_count": sum(int(source["pages"]) for source in source_manifest),
        "scene_count": len(all_scene_records),
        "text_extractor": f"pypdf {pypdf.__version__}",
        "sources": source_manifest,
        "episodes": episode_manifest,
        "scene_index": {
            "file": index_path.name,
            "sha256": scene_index_sha256,
        },
        "corpus_root_sha256": sha256_text(root_payload),
    }
    manifest_path = corpus_root / "corpus-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return manifest


def main() -> None:
    default_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description="Build the searchable 风起玲珑骨 episode corpus from preserved PDFs."
    )
    parser.add_argument("--skill-root", type=Path, default=default_root)
    args = parser.parse_args()
    manifest = build(args.skill_root.resolve())
    print(
        json.dumps(
            {
                "episode_count": manifest["episode_count"],
                "source_page_count": manifest["source_page_count"],
                "scene_count": manifest["scene_count"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover - command-line failure path
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
