"""
 String Compression
 Cracking the coding interview, 6th edition, page 91
"""


class StringCompression:
    def __init__(self, string: str) -> None:
        self.string = string

    def compress(self) -> str:
        if len(self.string) <= 2:
            return self.string
        list_string: list[str] = list(self.string)
        list_compress: list[str or int] = list()
        count_char: int = 0
        for i in range(len(list_string)):
            count_char += 1
            if i + 1 >= len(list_string) or list_string[i] != list_string[i+1]:
                list_compress.extend([list_string[i], str(count_char)])
                count_char = 0
        if len(list_string) <= len(list_compress):
            return self.string
        return ''.join(list_compress)

