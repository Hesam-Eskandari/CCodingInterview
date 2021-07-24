import unittest
from ArraysAndStrings import is_unique


class TestIsUnique(unittest.TestCase):
    def setUp(self) -> None:
        self.inputs_true: list[str] = ["", "a", "1234qwer."]
        self.inputs_false: list[str] = ["12345167890."]

    def test_structure_map(self) -> None:
        for n in range(len(self.inputs_true)):
            with self.subTest(n):
                self.assertTrue(is_unique.IsUnique(self.inputs_true[n])(additional_structure=True))
        for n in range(len(self.inputs_false)):
            with self.subTest(n):
                self.assertFalse(is_unique.IsUnique(self.inputs_false[n])(additional_structure=True))

    def test_structure_none(self) -> None:
        for n in range(len(self.inputs_true)):
            with self.subTest(n):
                self.assertTrue(is_unique.IsUnique(self.inputs_true[n])(additional_structure=False))
        for n in range(len(self.inputs_false)):
            with self.subTest(n):
                self.assertFalse(is_unique.IsUnique(self.inputs_false[n])(additional_structure=False))
