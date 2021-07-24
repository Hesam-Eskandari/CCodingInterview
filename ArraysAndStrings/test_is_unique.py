import unittest
from is_unique import IsUnique


class TestIsUnique(unittest.TestCase):
    def setUp(self):
        self.inputs_true = ["", "a", "1234qwer."]
        self.inputs_false = ["12345167890."]

    def test_structure_map(self):
        for n in range(len(self.inputs_true)):
            with self.subTest(n):
                self.assertTrue(IsUnique(self.inputs_true[n])(additional_structure=True))
        for n in range(len(self.inputs_false)):
            with self.subTest(n):
                self.assertFalse(IsUnique(self.inputs_false[n])(additional_structure=True))

    def test_structure_none(self):
        for n in range(len(self.inputs_true)):
            with self.subTest(n):
                self.assertTrue(IsUnique(self.inputs_true[n])(additional_structure=False))
        for n in range(len(self.inputs_false)):
            with self.subTest(n):
                self.assertFalse(IsUnique(self.inputs_false[n])(additional_structure=False))
