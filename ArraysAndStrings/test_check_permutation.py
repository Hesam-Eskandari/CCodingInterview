import unittest
from check_permutation import CheckPermutation

class TestCheckPermutation(unittest.TestCase):
  def setUp(self):
    self.input_1 = ["", " "]
    self.input_2 = ["1", "2"]
    self.input_3 = ["a", "a"]
    self.input_4 = ["123qweasd", "dsaewq321"]
    self.input_5 = ["\'", "\""]

  def test_are_permute(self):
    self.assertFalse(CheckPermutation(self.input_1[0],self.input_1[1])())
    self.assertFalse(CheckPermutation(self.input_2[0],self.input_2[1])())
    self.assertTrue(CheckPermutation(self.input_3[0],self.input_3[1])())
    self.assertTrue(CheckPermutation(self.input_4[0],self.input_4[1])())
    self.assertFalse(CheckPermutation(self.input_5[0],self.input_5[1])())