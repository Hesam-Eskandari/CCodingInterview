import unittest
from LinkedLists.linked_list import LinkedListSingly
from LinkedLists.remove_dups import RemoveDuplicates


class TestRemoveDups(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_inputs: list[list[int]] = [
            [1],
            [1, 2, 3, 2, 5, 3, 4, 1, 5],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]
        self.inputs: list[LinkedListSingly] = [LinkedListSingly.create_linked_lists(lst) for lst in self.raw_inputs]
        self.expected: list[list[int]] = [
            [1],
            [1, 2, 3, 5, 4],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]

    def remove_dupes(self, no_additional_datastructures=True):
        for i, linked_list in enumerate(self.inputs):
            with self.subTest([i, linked_list]):
                self.assertEqual(RemoveDuplicates(linked_list)(no_additional_datastructures).to_list(), self.expected[i])

    def test_remove_dups_no_additional_datastructures(self):
        self.remove_dupes(True)

    def test_remove_dups_using_additional_datastructures(self):
        self.remove_dupes(True)

