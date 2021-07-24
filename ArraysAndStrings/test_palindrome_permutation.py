import unittest
from palindrome_permutation import PalindromePermutation


class TestPalindromePermutation(unittest.TestCase):
    def setUp(self):
        self.input_true_method_true = ['Taco act', 'T1\'a2co a ct ', 'taco act']
        self.input_false_method_true = ['Taco acta', 'tacoacta', ' Tacooactta']
        self.input_true_method_false = ['tacoact', 'taco  act', 'TacoacT']
        self.input_false_method_false = ['Tacoact', 'taco act', 'Taco act']

    def test_is_palindrome_permutation_method_false(self):
        for n in range(len(self.input_true_method_false)):
            with self.subTest(n):
                self.assertTrue(PalindromePermutation(self.input_true_method_false[n])(False))
        for n in range(len(self.input_false_method_false)):
            with self.subTest(n):
                self.assertFalse(PalindromePermutation(self.input_false_method_false[n])(False))

    def test_is_palindrome_permutation_method_ture(self):
        for n in range(len(self.input_true_method_true)):
            with self.subTest(n):
                self.assertTrue(PalindromePermutation(self.input_true_method_true[n])(True))
        for n in range(len(self.input_false_method_true)):
            with self.subTest(n):
                self.assertFalse(PalindromePermutation(self.input_false_method_true[n])(True))
