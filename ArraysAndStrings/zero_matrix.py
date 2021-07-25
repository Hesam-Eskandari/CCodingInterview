
"""
 Zero Matrix 
 Cracking the coding interview, 6th edition, page 91
"""


class ZeroMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix: list[list[int]] = matrix

    def __call__(self) -> list[list[int]]:
        self._to_zero_matrix()
        return self.matrix

    def _to_zero_matrix(self) -> None:
        if not len(self.matrix):
            return
        is_first_row_zero: bool = 0 in self.matrix[0]
        is_first_col_zero: bool = False

        for row in self.matrix:
            if not row[0]:
                is_first_col_zero = True
                break

        for row_index in range(len(self.matrix)):
            for col_index in range(len(self.matrix[row_index])):
                if not self.matrix[row_index][col_index]:
                    self.matrix[0][col_index] = 0
                    self.matrix[row_index][0] = 0

        for row_index in range(len(self.matrix)):
            if row_index and not self.matrix[row_index][0]:
                for col_index in range(len(self.matrix[row_index])):
                    self.matrix[row_index][col_index] = 0

        for col_index in range(len(self.matrix[0])):
            if col_index and not self.matrix[0][col_index]:
                for row_index in range(len(self.matrix)):
                    self.matrix[row_index][col_index] = 0

        if is_first_row_zero:
            for col_index in range(len(self.matrix[0])):
                self.matrix[0][col_index] = 0

        if is_first_col_zero:
            for row_index in range(len(self.matrix)):
                self.matrix[row_index][0] = 0
