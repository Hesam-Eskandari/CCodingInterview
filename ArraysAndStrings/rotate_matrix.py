"""
Rotate Matrix
Cracking the coding interview, 6th edition, page 91
"""


class RotateMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix
        self.validate_matrix()

    def validate_matrix(self) -> None:
        length: int = len(self.matrix)
        if not length:
            return
        for i, row in enumerate(self.matrix):
            if len(row) != length:
                raise ValueError("given input is not a square matrix, row {row_index} should be of size {size},\
                 matrix: {matrix}".format(row_index=i, size=length, matrix=self.matrix))

    def get_matrix(self) -> list[list[int]]:
        self.validate_matrix()
        return self.matrix

    def rotate(self) -> None:
        # rotates a square matrix 90 deg clockwise in place
        for start in range(len(self.matrix)//2):
            end: int = len(self.matrix)-start-1
            for pose in range(start, end):
                top: int = self.matrix[start][pose]
                self.matrix[start][pose] = self.matrix[end-pose][start]
                self.matrix[end-pose][start] = self.matrix[end][end-pose]
                self.matrix[end][end-pose] = self.matrix[pose][end]
                self.matrix[pose][end] = top
