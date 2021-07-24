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


class URLify:
    def __init__(self, string: str, length: int) -> None:
        self.list_string: list[str] = list(string)
        self.length: int = length

    def __call__(self, modified_version=False) -> str or list[str]:
        if self.validate():
            return self.urlify(modified_version)

    def __repr__(self) -> str:
        return ''.join(self.list_string)

    @property
    def get_list_string(self) -> list:
        if type(self.list_string) == list:
            if self.list_string == list():
                return ['']
            return self.list_string

    def validate(self) -> bool:
        valid_spaces: int = 0
        total_spaces: int = 0
        for idx in range(len(self.list_string)):
            if self.list_string[idx] == ' ':
                total_spaces += 1
                if idx < self.length:
                    valid_spaces += 1
        if total_spaces == 3 * valid_spaces:
            return True
        else:
            raise ValueError('Invalid input: mismatch in the number of spaces in the input string: \
            {total_spaces} != 3 * {valid_spaces}'.format(total_spaces=total_spaces, valid_spaces=valid_spaces))

    def urlify(self, modified_version=False) -> str or list[str]:
        j: int = len(self.list_string) - 1
        # loop backward and relocate elements
        for idx in range(len(self.list_string)-1, -1, -1):
            if self.list_string[idx] != ' ':
                temp: str = self.list_string[j]
                self.list_string[j] = self.list_string[idx]
                self.list_string[idx] = temp
                j -= 1
            elif self.list_string[idx] == ' ' and idx < self.length:
                j -= 3

        # replace three adjacent spaces with '%20'
        for idx in range(len(self.list_string)):
            if self.list_string[idx] == ' ':
                self.list_string[idx:idx+3] = ['%', '2', '0']
        if modified_version:
            return self.get_list_string
        else:
            return self.__repr__()
