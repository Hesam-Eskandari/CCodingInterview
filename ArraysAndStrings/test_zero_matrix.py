import unittest
from ArraysAndStrings import zero_matrix


class TestZeroMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.inputs: list[list[list[int]]] = [
            [],
            [[1]],
            [[0]],
            [[1, 2], [0, 4]],
            [[0, 2, 3], [4, 1, 0], [2, 1, 3]],
            [[1, 2, 3], [4, 0, 6], [7, 8, 9]],
            [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
        ]
        self.expected: list[list[list[int]]] = [
            [],
            [[1]],
            [[0]],
            [[0, 2], [0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
            [[1, 0, 3], [0, 0, 0], [7, 0, 9]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ]

    def test_to_zero_matrix(self) -> None:
        for pose, element in enumerate(self.inputs):
            with self.subTest(element):
                self.assertEqual(zero_matrix.ZeroMatrix(element)(), self.expected[pose])
