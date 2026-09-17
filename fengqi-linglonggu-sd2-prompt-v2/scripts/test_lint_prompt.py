#!/usr/bin/env python3
"""Regression tests for delivery-package linting."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

from lint_prompt import lint_document


FIXTURES = Path(__file__).resolve().parent / "fixtures"


def error_findings(text: str):
    return [finding for finding in lint_document(text) if finding.level == "ERROR"]


class DeliveryPackageLintTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.good = (FIXTURES / "known-good.txt").read_text(encoding="utf-8")
        cls.bad = (FIXTURES / "known-bad.txt").read_text(encoding="utf-8")

    def test_known_good_passes(self) -> None:
        self.assertEqual(error_findings(self.good), [])

    def test_known_bad_fails(self) -> None:
        self.assertTrue(error_findings(self.bad))

    def test_every_package_is_validated(self) -> None:
        errors = error_findings(self.good + "\n" + self.bad)
        self.assertTrue(any("交付包2" in finding.message for finding in errors))

    def test_missing_shot_headers_is_blocking(self) -> None:
        candidate = re.sub(r"(?m)^镜头\d+｜.*\n", "", self.good)
        errors = error_findings(candidate)
        self.assertTrue(any(finding.rule == "shot-headers" for finding in errors))

    def test_duplicate_inner_heading_is_blocking(self) -> None:
        candidate = self.good.replace("负面限制：", "参考图角色分工：\n负面限制：", 1)
        errors = error_findings(candidate)
        self.assertTrue(any(finding.rule == "inner-headings" for finding in errors))


if __name__ == "__main__":
    unittest.main()
