import unittest
from urlify import URLify

class TestURLify(unittest.TestCase):
  def setUp(self):
    self.input_1 = ['', 0]
    self.input_2 = ['   ', 1]
    self.input_3 = ['Mr John Smith    ', 13]
    self.input_4 = ['Mr John Smith       ',14]
    self.input_5 = [' Mr John Smith      ', 14]
    self.input_6 = [' Mr John  Smith        ', 15]

  def test_urlify_str(self):
    self.assertEqual(URLify(self.input_1[0],self.input_1[1])(False),'')
    self.assertEqual(URLify(self.input_2[0],self.input_2[1])(False),'%20')
    self.assertEqual(URLify(self.input_3[0],self.input_3[1])(False),'Mr%20John%20Smith')
    self.assertEqual(URLify(self.input_4[0],self.input_4[1])(False),'Mr%20John%20Smith%20')
    self.assertEqual(URLify(self.input_5[0],self.input_5[1])(False),'%20Mr%20John%20Smith')
    self.assertEqual(URLify(self.input_6[0],self.input_6[1])(False),'%20Mr%20John%20%20Smith')

  def test_urlify_list(self):
    self.assertEqual(URLify(self.input_1[0],self.input_1[1])(True),[''])
    self.assertEqual(URLify(self.input_2[0],self.input_2[1])(True),['%','2','0'])
    self.assertEqual(URLify(self.input_3[0],self.input_3[1])(True),['M','r','%','2','0','J','o','h','n','%','2','0','S','m','i','t','h'])
    self.assertEqual(URLify(self.input_4[0],self.input_4[1])(True),['M','r','%','2','0','J','o','h','n','%','2','0','S','m','i','t','h','%','2','0'])
    self.assertEqual(URLify(self.input_5[0],self.input_5[1])(True),['%','2','0','M','r','%','2','0','J','o','h','n','%','2','0','S','m','i','t','h'])
    self.assertEqual(URLify(self.input_6[0],self.input_6[1])(True),['%','2','0','M','r','%','2','0','J','o','h','n','%','2','0','%','2','0','S','m','i','t','h'])