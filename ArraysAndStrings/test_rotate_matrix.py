import unittest
from ArraysAndStrings import rotate_matrix


class TestRotateMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.inputs: list[list[list[int]]] = [
            [],
            [[1]],
            [[1, 2], [3, 4]],
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ]
        self.expected: list[list[list[int]]] = [
            [],
            [[1]],
            [[3, 1], [4, 2]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        ]

    def test_rotate(self) -> None:
        for i, element in enumerate(self.inputs):
            with self.subTest([i, element]):
                sample: rotate_matrix.RotateMatrix = rotate_matrix.RotateMatrix(element)
                sample.rotate()
                self.assertEqual(sample.get_matrix(), self.expected[i])
