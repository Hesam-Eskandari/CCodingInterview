import unittest
from ArraysAndStrings import check_permutation


class TestCheckPermutation(unittest.TestCase):
    def setUp(self) -> None:
        self.inputs_true: list[list[str]] = [["a", "a"], ["123qweasd", "dsaewq321"]]
        self.inputs_false: list[list[str]] = [["", " "], ["1", "2"], ["\'", "\""]]

    def test_are_permute(self) -> None:
        for n in range(len(self.inputs_true)):
            with self.subTest(n):
                self.assertTrue(check_permutation.CheckPermutation(self.inputs_true[n][0], self.inputs_true[n][1])())
        for n in range(len(self.inputs_false)):
            with self.subTest(n):
                self.assertFalse(check_permutation.CheckPermutation(self.inputs_false[n][0], self.inputs_false[n][1])())
