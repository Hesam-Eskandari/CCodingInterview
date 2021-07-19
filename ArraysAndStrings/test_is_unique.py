import unittest
from is_unique import IsUnique

class TestIsUnique(unittest.TestCase):
  def setUp(self):
    self.input_1 = ""
    self.input_2 = "a"
    self.input_3 = "1234qwer."
    self.input_4 = "12345167890."

  def test_structure_map(self):
    self.assertTrue(IsUnique(self.input_1)(additional_structure=True))
    self.assertTrue(IsUnique(self.input_2)(additional_structure=True))
    self.assertTrue(IsUnique(self.input_3)(additional_structure=True))
    self.assertFalse(IsUnique(self.input_4)(additional_structure=True))

  def test_structure_none(self):
    self.assertTrue(IsUnique(self.input_1)(additional_structure=True))
    self.assertTrue(IsUnique(self.input_2)(additional_structure=True))
    self.assertTrue(IsUnique(self.input_3)(additional_structure=True))
    self.assertFalse(IsUnique(self.input_4)(additional_structure=True))