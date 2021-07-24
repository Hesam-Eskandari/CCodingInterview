import unittest
from ArraysAndStrings import string_rotation


class TestStringRotation(unittest.TestCase):
    def setUp(self) -> None:
        self.inputs_true: list[list[str]] = [
            ["", ""],
            ["aAAa", "aaAA"],
            ["abcdefg", "cdefgab"],
        ]
        self.inputs_false: list[list[str]] = [
            ["a", "ab"],
            ["", " "],
            ["aaAA", "aAaA"],
        ]

    def test_string_rotation(self) -> None:
        for element in self.inputs_true:
            with self.subTest(element):
                self.assertTrue(string_rotation.StringRotation(element[0], element[1])())
        for element in self.inputs_false:
            with self.subTest(element):
                self.assertFalse(string_rotation.StringRotation(element[0], element[1])())

