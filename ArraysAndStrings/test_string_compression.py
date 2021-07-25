import unittest
from ArraysAndStrings import string_compression


class TestStringCompression(unittest.TestCase):
    def setUp(self) -> None:
        self.inputs: list[str] = [
            "",
            "a",
            "aa",
            "aabb",
            "aaabb",
            "aaaaaaaaaaa"
        ]
        self.outputs: list[str] = [
            "",
            "a",
            "aa",
            "aabb",
            "a3b2",
            "a11"
        ]

    def test_compress(self) -> None:
        for i, string in enumerate(self.inputs):
            with self.subTest([i, string]):
                self.assertEqual(string_compression.StringCompression(string).compress(), self.outputs[i])
