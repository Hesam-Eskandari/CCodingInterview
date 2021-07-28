import unittest
from LinkedLists.linked_list import LinkedListSingly
from LinkedLists.kth_to_last import KthToLast


class TestKthToLast(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_input: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.input: LinkedListSingly = LinkedListSingly.create_linked_lists(self.raw_input)
        self.k_list: list[int] = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.node_data: list[int or None] = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def test_known_length(self) -> None:
        for i, k in enumerate(self.k_list):
            with self.subTest(k):
                node_known_length = KthToLast(self.input)(k, method=0)
                self.assertEqual(node_known_length.data
                                 if node_known_length is not None else None, self.node_data[i])
                node_two_pointers = KthToLast(self.input)(k, method=1)
                self.assertEqual(node_two_pointers.data
                                 if node_two_pointers is not None else None, self.node_data[i])
