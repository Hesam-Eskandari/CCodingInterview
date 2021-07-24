class OneAway:
    def __init__(self, string1: str, string2: str) -> None:
        self.string1: str = string1
        self.string2: str = string2

    def __call__(self) -> bool:
        if len(self.string1) == len(self.string2):
            count: int = 0
            for idx, item in enumerate(self.string1):
                if self.string2[idx] != item:
                    count += 1
            return count <= 1
        elif len(self.string1) > len(self.string2):
            return self.is_substring(self.string1, self.string2)
        else:
            return self.is_substring(self.string2, self.string1)

    def is_substring(self, string: str, substring: str) -> bool:
        if len(substring) == 0:
            return True
        elif len(substring) == 1:
            for item in string:
                if substring[0] == item:
                    return True
            else:
                return False
        elif substring == string[1:] or substring == string[:-1]:
            return True
        return False
