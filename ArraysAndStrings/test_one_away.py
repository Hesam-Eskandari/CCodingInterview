import unittest
from one_away import OneAway

class TestOneAway(unittest.TestCase):
  def setUp(self):
    self.inputs_true = [['abcd','afcd'],['abcd','bcd'],['abc','abc ']]
    self.inputs_false = [['abcd','abdc'],['abcd','acd'],['abc','ab c']]

  def test_is_one_away(self):
    for n in range(len(self.inputs_true)):
      with self.subTest(n):
        self.assertTrue(OneAway(self.inputs_true[n][0],self.inputs_true[n][1])())

    for n in range(len(self.inputs_false)):
      with self.subTest(n):
        self.assertFalse(OneAway(self.inputs_false[n][0],self.inputs_false[n][1])())