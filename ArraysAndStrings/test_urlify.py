import unittest
from ArraysAndStrings import urlify


class TestURLify(unittest.TestCase):
    def setUp(self):
        self.inputs = [
            ['', 0],
            ['   ', 1],
            ['Mr John Smith    ', 13],
            ['Mr John Smith       ', 14],
            [' Mr John Smith      ', 14],
            [' Mr John  Smith        ', 15]]

    def test_urlify_str(self):
        output = [
            '',
            '%20',
            'Mr%20John%20Smith',
            'Mr%20John%20Smith%20',
            '%20Mr%20John%20Smith',
            '%20Mr%20John%20%20Smith']
        for n in range(len(self.inputs)):
            with self.subTest(n):
                self.assertEqual(urlify.URLify(self.inputs[n][0], self.inputs[n][1])(False), output[n])

    def test_urlify_list(self):
        output = [
            [''],
            ['%','2','0'],
            ['M', 'r', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', 'S', 'm', 'i', 't', 'h'],
            ['M', 'r', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', 'S', 'm', 'i', 't', 'h', '%', '2', '0'],
            ['%', '2', '0', 'M', 'r', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', 'S', 'm', 'i', 't', 'h'],
            ['%', '2', '0', 'M', 'r', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', '%', '2', '0', 'S', 'm', 'i', 't', 'h']
        ]
        for n in range(len(self.inputs)):
            with self.subTest(n):
                self.assertEqual(urlify.URLify(self.inputs[n][0], self.inputs[n][1])(True), output[n])
