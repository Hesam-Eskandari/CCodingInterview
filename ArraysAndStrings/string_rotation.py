"""
Cracking the coding interview, 6th edition, page 91
"""


class StringRotation:
    def __init__(self, first_string: str, second_string: str) -> None:
        self.first_string = first_string
        self.second_string = second_string

    def __call__(self) -> bool:
        if len(self.first_string) != len(self.second_string):
            return False
        self.first_string = 2 * self.first_string
        return self.is_substring()

    def is_substring(self) -> bool:
        indx = self.first_string.find(self.second_string)
        return indx != -1
