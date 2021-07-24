import unittest
from ArraysAndStrings import one_away


class TestOneAway(unittest.TestCase):
    def setUp(self):
        self.inputs_true: list[list[str]] = [['abcd', 'afcd'], ['abcd', 'bcd'], ['abc', 'abc ']]
        self.inputs_false: list[list[str]] = [['abcd', 'abdc'], ['abcd', 'acd'], ['abc', 'ab c']]

    def test_is_one_away(self):
        for n in range(len(self.inputs_true)):
            with self.subTest(n):
                self.assertTrue(one_away.OneAway(self.inputs_true[n][0], self.inputs_true[n][1])())

        for n in range(len(self.inputs_false)):
            with self.subTest(n):
                self.assertFalse(one_away.OneAway(self.inputs_false[n][0], self.inputs_false[n][1])())
