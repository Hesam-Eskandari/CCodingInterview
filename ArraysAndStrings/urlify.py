"""
Reference: Cracking The Coding Interview, 6th Edition, Page 90
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additionel characters, 
and that yu are given the 'true' length of the string.
Example: 
  Input: 'Mr John Smith   ', 13
  Output: 'Mr%20John%20Smith'
Modified version: input is a list of characters (strings in Python). Make changes in place
  Input: ['M','r',' ','J','o','h','n',' ','S','m','i','t','h',' ',' ',' ',' ']
  Output: ['M','r','%','2','0','J','o','h','n','%','2','0','S','m','i','t','h']
"""

class URLify():
  def __init__(self, string: str, length: int):
    self.listString = list(string)
    self.length = length

  def __call__(self, modified_version = False) -> str or list(str):
    if self.validate():
      return self.urlify(modified_version)

  def __repr__(self) -> str:
    return ''.join(self.listString)

  @property
  def get_listString(self) -> list:
    if type(self.listString) == list:
      if self.listString == list():
        return ['']
      return self.listString


  def validate(self) -> bool:
    validSapces = 0
    totalSpaces = 0
    for idx in range(len(self.listString)):
      if self.listString[idx] == ' ':
        totalSpaces += 1
        if idx < self.length:
          validSapces += 1
    if totalSpaces == 3 * validSapces:
      return True
    else:
      raise ValueError('Invalid input: mismatch in the number of spaces in the input string: \
      {totalSpaces} != 3 * {validSapces}'.format(totalSpaces=totalSpaces, validSapces=validSapces))

  def urlify(self, modified_version = False) -> str or list(str):
    j = len(self.listString)-1
    # loop backward and relocate elements 
    for idx in range(len(self.listString)-1,-1,-1):
      if self.listString[idx] != ' ':
        temp = self.listString[j]
        self.listString[j] = self.listString[idx]
        self.listString[idx] = temp
        j -= 1
      elif self.listString[idx] == ' ' and idx < self.length:
        j -= 3

    # replace three adjacent spaces with '%20' 
    for idx in range(len(self.listString)):
      if self.listString[idx] == ' ':
        self.listString[idx:idx+3] = ['%','2','0']
    if modified_version:
      return self.get_listString
    else:
      return self.__repr__()
