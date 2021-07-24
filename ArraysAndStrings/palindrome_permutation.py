"""
Reference: Cracking the Coding Intervire, 6th Edition, Page 60
Palindrome Permutation:
Given a string, write a function to check if it is a permutation of a Palindrome. You can ignore casing and non-letter characters
Method one: consider casing and non-letter characters
Method two: ignore casing and non-letter characters
"""

class PalindromePermutation():
  def __init__(self, string: str):
    self.string = string
    self.letter = dict()

  def __call__(self, method_ignore=False):
    string = self.string
    if method_ignore:
      string = string.lower()
      for char in "abcdefghijklmnopqrstuvwxyz":
        self.letter[char] = True
    return self.is_palindrome_permutation(string)


  def is_palindrome_permutation(self, string) -> bool:
    hmap = dict()
    for char in string:
      if self.letter.get(char, False) or len(self.letter.values()) == 0:
        if hmap.get(char, False):
          hmap[char] += 1
        else:
          hmap[char] = 1
    odd = 0
    for value in hmap.values():
      if value % 2 != 0:
        odd += 1
    return odd <= 1