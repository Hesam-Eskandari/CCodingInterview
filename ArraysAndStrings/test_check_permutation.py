import unittest

class TestCheckPermutation(unittest.TestCase):
  def setUp(self):
    self.input_1 = ["", " "]
    self.input_2 = ["1", "2"]
    self.input_3 = ["a", "a"]
    self.input_4 = ["123qweasd", "dsaewq321"]
    self.input_5 = [""]