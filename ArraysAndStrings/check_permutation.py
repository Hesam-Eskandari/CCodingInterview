"""
Reference: Cracking The Coding Interview, 6th Edition, Page 90
Given two strings, check if one is a permutation of the other
"""
class CheckPermutation():
  def __init__(self, string_1: str, string_2: str) -> None:
    self.string_1 = string_1
    self.string_2 = string_2

  def __call__(self) -> bool:
    return self.are_permute()

  def are_permute(self) -> bool:
    if len(self.string_1) != len(self.string_2):
      return False
    for indx in range(len(self.string_1)):
      if self.string_1[indx] != self.string_2[len(self.string_2)-indx-1]:
        return False
    else:
      return True
