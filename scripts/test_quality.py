"""Regressioni della rubrica statica e delle sue rappresentazioni pubbliche."""

import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from build_catalog import build_catalog, validate_catalog
from build_readme import render_row, sort_key
from quality import CRITERIA, quality_rubric, readiness_label, readiness_score

ROOT = Path(__file__).resolve().parent.parent
BASE_SERVER = {
    "name": "Server di esempio",
    "repository_url": "https://example.org/server",
    "author": "example",
    "language": "Python",
    "license": None,
    "stars": 0,
    "category": "dati-statistiche",
    "description": "Un server MCP di esempio per i test.",
    "tags": ["dati", "esempio"],
}


def assessed(status="complete"):
    server = copy.deepcopy(BASE_SERVER)
    server["quality"] = {
        "rubric_version": 1,
        "reviewed_at": "2026-09-05",
        "status": "assessed",
        "criteria": {
            key: {
                "status": status,
                "evidence": ["https://example.org/documentazione"],
                "notes": "Evidenza dimostrativa per i test.",
            }
            for key in CRITERIA
        },
    }
    return server


def unassessed():
    server = copy.deepcopy(BASE_SERVER)
    server["quality"] = {
        "rubric_version": 1,
        "reviewed_at": "2026-09-05",
        "status": "unassessed",
        "reason": "Documentazione non consultabile.",
        "evidence": ["https://example.org/documentazione"],
    }
    return server


class QualityTests(unittest.TestCase):
    def test_weighted_scores(self):
        self.assertEqual(sum(weight for _, weight in CRITERIA.values()), 100)
        for status, expected in [("absent", 0), ("partial", 50), ("complete", 100)]:
            with self.subTest(status=status):
                self.assertEqual(readiness_score(assessed(status)), expected)

    def test_each_criterion_uses_its_weight(self):
        for key, (_, weight) in CRITERIA.items():
            with self.subTest(criterion=key):
                server = assessed("absent")
                server["quality"]["criteria"][key]["status"] = "partial"
                self.assertEqual(readiness_score(server), weight / 2)

    def test_unknown_is_not_zero(self):
        self.assertIsNone(readiness_score(BASE_SERVER))
        self.assertIsNone(readiness_score(unassessed()))
        self.assertEqual(readiness_label(BASE_SERVER), "Non valutato")
        self.assertEqual(readiness_label(assessed("absent")), "0/100")

    def test_unsupported_rubric_is_not_silently_rescored(self):
        server = assessed()
        server["quality"]["rubric_version"] = 2
        with self.assertRaises(ValueError):
            readiness_score(server)

    def test_editorial_and_popularity_signals_do_not_change_score_or_sort(self):
        server = assessed("partial")
        decorated = copy.deepcopy(server)
        decorated.update(stars=100000, featured=True, mcp_endpoint="https://example.org/mcp")
        self.assertEqual(readiness_score(server), readiness_score(decorated))
        self.assertEqual(sort_key(server), sort_key(decorated))

    def test_sort_places_zero_before_unknown_and_breaks_ties_by_name(self):
        high = assessed()
        zero = assessed("absent")
        unknown = copy.deepcopy(BASE_SERVER)
        unknown.update(name="A non valutato", stars=100000, featured=True)
        beta = assessed()
        beta["name"] = "Beta"
        result = sorted([unknown, zero, high, beta], key=sort_key)
        self.assertEqual(result, [beta, high, zero, unknown])

    def test_readme_links_to_evidence_and_displays_review_date(self):
        server = assessed("partial")
        server["_path"] = Path("servers/esempio.json")
        server["name"] = '<Esempio & "MCP">'
        row = render_row(server)
        self.assertIn('href="servers/esempio.json"', row)
        self.assertIn("50/100", row)
        self.assertIn("2026-09-05", row)
        self.assertIn("&lt;Esempio &amp; &quot;MCP&quot;&gt;", row)
        self.assertNotIn('<Esempio & "MCP">', row)
        self.assertIn("Non valutato", render_row(BASE_SERVER))

    def test_readme_distinguishes_inaccessible_documentation(self):
        server = unassessed()
        server["_path"] = Path("servers/esempio.json")
        row = render_row(server)
        self.assertIn('href="servers/esempio.json"', row)
        self.assertIn("Non valutato", row)
        self.assertNotIn("0/100", row)

    def test_catalog_preserves_assessment_and_derives_score(self):
        server = assessed("partial")
        server["_path"] = Path("servers/esempio.json")
        catalog = build_catalog([BASE_SERVER, server, unassessed()])
        validate_catalog(catalog)
        self.assertEqual(catalog["quality_rubric"], quality_rubric())
        self.assertEqual([s["readiness_score"] for s in catalog["servers"]], [50, None, None])
        entry = catalog["servers"][0]
        self.assertEqual(entry["quality"], server["quality"])
        self.assertEqual(entry["url"], server["repository_url"])
        self.assertNotIn("_path", entry)
        self.assertNotIn("readiness_score", server)


class QualitySchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema = json.loads((ROOT / "schema/server.schema.json").read_text())
        Draft202012Validator.check_schema(schema)
        cls.validator = Draft202012Validator(schema, format_checker=FormatChecker())

    def test_optional_and_complete_assessments_are_valid(self):
        for server in [BASE_SERVER, assessed(), assessed("partial"), assessed("absent"), unassessed()]:
            with self.subTest(server=server):
                self.assertEqual(list(self.validator.iter_errors(server)), [])

    def test_all_criteria_and_evidence_are_required(self):
        for key in CRITERIA:
            server = assessed()
            del server["quality"]["criteria"][key]
            with self.subTest(missing=key):
                self.assertFalse(self.validator.is_valid(server))
        for field in ["status", "evidence", "notes"]:
            server = assessed()
            del server["quality"]["criteria"]["installation"][field]
            with self.subTest(missing=field):
                self.assertFalse(self.validator.is_valid(server))

    def test_rejects_invalid_criterion_values(self):
        for field, value in [
            ("status", "unknown"),
            ("evidence", []),
            ("evidence", ["http://example.org/docs"]),
            ("evidence", ["javascript:alert(1)"]),
            ("evidence", ["https://"]),
            ("evidence", ["https://example.org/with space"]),
            ("evidence", ["https://example.org", "https://example.org"]),
            ("notes", ""),
            ("notes", "   "),
        ]:
            with self.subTest(field=field, value=value):
                server = assessed()
                server["quality"]["criteria"]["installation"][field] = value
                self.assertFalse(self.validator.is_valid(server))

    def test_rejects_invalid_dates_and_versions(self):
        for field, value in [
            ("reviewed_at", "2026-02-30"),
            ("reviewed_at", "05/09/2026"),
            ("rubric_version", 2),
            ("status", "healthy"),
        ]:
            with self.subTest(field=field, value=value):
                server = assessed()
                server["quality"][field] = value
                self.assertFalse(self.validator.is_valid(server))

    def test_rejects_contradictory_assessment_states(self):
        unknown_with_criteria = unassessed()
        unknown_with_criteria["quality"]["criteria"] = assessed()["quality"]["criteria"]
        assessed_with_reason = assessed()
        assessed_with_reason["quality"]["reason"] = "Non valutato"
        for server in [unknown_with_criteria, assessed_with_reason]:
            self.assertFalse(self.validator.is_valid(server))
        for field in ["reason", "evidence"]:
            server = unassessed()
            del server["quality"][field]
            self.assertFalse(self.validator.is_valid(server))

    def test_rejects_manually_assigned_scores(self):
        server = assessed()
        server["readiness_score"] = 100
        self.assertFalse(self.validator.is_valid(server))
        del server["readiness_score"]
        server["quality"]["score"] = 100
        self.assertFalse(self.validator.is_valid(server))


if __name__ == "__main__":
    unittest.main()
