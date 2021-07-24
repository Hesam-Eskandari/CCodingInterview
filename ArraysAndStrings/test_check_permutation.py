import unittest
from ArraysAndStrings import check_permutation


class TestCheckPermutation(unittest.TestCase):
    def setUp(self):
        self.inputs_true = [["a", "a"], ["123qweasd", "dsaewq321"]]
        self.inputs_false = [["", " "], ["1", "2"], ["\'", "\""]]

    def test_are_permute(self):
        for n in range(len(self.inputs_true)):
            with self.subTest(n):
                self.assertTrue(check_permutation.CheckPermutation(self.inputs_true[n][0], self.inputs_true[n][1])())
        for n in range(len(self.inputs_false)):
            with self.subTest(n):
                self.assertFalse(check_permutation.CheckPermutation(self.inputs_false[n][0], self.inputs_false[n][1])())
