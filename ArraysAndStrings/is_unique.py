"""
Reference: Cracking The Coding Interview, 6th Edition, Page 90
Question: Implement an algorithm to determine if a string has all unique characters. What if you cannot use an additional datastructure?
"""
class IsUnique():
  
  def __init__(self, string: str) -> None:
    self.string = string

  def __call__(self, additional_structure = False) -> bool:
    if additional_structure:
      return self.structure_map()
    else:
      return self.structure_none()

  def structure_map(self) -> bool:
    # O(n)
    hmap = dict()
    for val in self.string:
      if hmap.get(val,False):
        hmap[val] += 1
      else:
        hmap[val] = 1
    for value in hmap.values():
      if value > 1:
        return False
    return True

  def structure_none(self) -> bool:
    # O(n^2)
    for i in range(len(self.string)-1):
      for j in range(i+1,len(self.string)):
        if self.string[i] == self.string[j]:
          return False
    return True