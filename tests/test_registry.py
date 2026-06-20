import unittest

from scriptsv1 import ScriptEntry, validate_registry


class RegistryTests(unittest.TestCase):
    def test_accepts_documented_low_risk_script(self):
        errors = validate_registry([ScriptEntry("report", "print report", "low", False)])

        self.assertEqual(errors, [])

    def test_rejects_high_risk_without_dry_run(self):
        errors = validate_registry([ScriptEntry("deploy", "deploy service", "high", False)])

        self.assertTrue(any("dry_run" in error for error in errors))

    def test_rejects_duplicate_names(self):
        errors = validate_registry(
            [
                ScriptEntry("same", "one", "low", False),
                ScriptEntry("same", "two", "low", False),
            ]
        )

        self.assertTrue(any("duplicates" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

