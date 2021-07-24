import unittest
from ArraysAndStrings import palindrome_permutation


class TestPalindromePermutation(unittest.TestCase):
    def setUp(self) -> None:
        self.input_true_method_true: list[str] = ['Taco act', 'T1\'a2co a ct ', 'taco act']
        self.input_false_method_true: list[str] = ['Taco acta', 'tacoacta', ' Tacooactta']
        self.input_true_method_false: list[str] = ['tacoact', 'taco  act', 'TacoacT']
        self.input_false_method_false: list[str] = ['Tacoact', 'taco act', 'Taco act']

    def test_is_palindrome_permutation_method_false(self) -> None:
        for n in range(len(self.input_true_method_false)):
            with self.subTest(n):
                self.assertTrue(palindrome_permutation.PalindromePermutation(self.input_true_method_false[n])(False))
        for n in range(len(self.input_false_method_false)):
            with self.subTest(n):
                self.assertFalse(palindrome_permutation.PalindromePermutation(self.input_false_method_false[n])(False))

    def test_is_palindrome_permutation_method_ture(self) -> None:
        for n in range(len(self.input_true_method_true)):
            with self.subTest(n):
                self.assertTrue(palindrome_permutation.PalindromePermutation(self.input_true_method_true[n])(True))
        for n in range(len(self.input_false_method_true)):
            with self.subTest(n):
                self.assertFalse(palindrome_permutation.PalindromePermutation(self.input_false_method_true[n])(True))
