import unittest
from LinkedLists.linked_list import LinkedListSingly
from LinkedLists.linked_list import LinkedListDoubly


class TestLinkedListSingly(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_inputs: list[list[int]] = [
            [1],
            [2, 1, 2],
            [1, 2, 3, 4, 5, 2]
        ]
        self.inputs: list[LinkedListSingly] = [LinkedListSingly.create_linked_lists(lst) for lst in self.raw_inputs]
        self.list_linked_lists: list[list[int]] = self.raw_inputs
        self.length_linked_lists: list[int] = [1, 3, 6]
        self.list_added_linked_lists: list[list[int]] = [
            [1, 18],
            [2, 1, 2, 18],
            [1, 2, 3, 4, 5, 2, 18]
        ]
        self.list_deleted_linked_lists: list[list[int]] = [
            [1],
            [1],
            [1, 3, 4, 5]
        ]

    def test_list_linked_list(self):
        for i in range(len(self.inputs)):
            with self.subTest([i, self.inputs[i]]):
                self.assertEqual(self.inputs[i].to_list(), self.list_linked_lists[i])

    def test_get_length(self):
        for i in range(len(self.inputs)):
            with self.subTest([i, self.inputs[i]]):
                self.assertEqual(self.inputs[i].length(), self.length_linked_lists[i])

    def test_add_to_tail(self):
        for i in range(len(self.inputs)):
            with self.subTest([i,self.inputs[i]]):
                added_data = self.inputs[i]
                added_data.add_to_tail(18)
                self.assertEqual(added_data.to_list(), self.list_added_linked_lists[i])

    def test_delete_node(self):
        for i in range(len(self.inputs)):
            with self.subTest([i, self.inputs[i]]):
                delete_data = self.inputs[i]
                head = delete_data.delete_node_to_right(2)
                self.assertEqual(head.to_list(), self.list_deleted_linked_lists[i])


class TestLinkedListDoubly(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_inputs: list[list[int]] = [
            [1],
            [2, 1, 2],
            [1, 2, 3, 4, 5, 2]
        ]
        self.inputs: list[LinkedListDoubly] = [LinkedListDoubly.create_linked_lists(lst) for lst in self.raw_inputs]
        self.list_linked_lists: list[list[int]] = self.raw_inputs
        self.length_linked_lists: list[int] = [1, 3, 6]
        self.list_add_to_head: list[list[int]] = [
            [18, 1],
            [18, 2, 1, 2],
            [18, 1, 2, 3, 4, 5, 2]
        ]
        self.list_add_to_tail: list[list[int]] = [
            [1, 18],
            [2, 1, 2, 18],
            [1, 2, 3, 4, 5, 2, 18]
        ]
        self.list_deleted_linked_lists: list[list[int]] = [
            [1],
            [1],
            [1, 3, 4, 5]
        ]

    def test_list_linked_list(self):
        for i in range(len(self.inputs)):
            with self.subTest([i, self.inputs[i]]):
                self.assertEqual(self.inputs[i].to_list(), self.list_linked_lists[i])

    def test_get_length(self):
        for i in range(len(self.inputs)):
            with self.subTest([i, self.inputs[i]]):
                self.assertEqual(self.inputs[i].length(), self.length_linked_lists[i])

    def test_add_to_tail(self):
        for i in range(len(self.inputs)):
            with self.subTest([i, self.inputs[i]]):
                added_data = self.inputs[i]
                added_data.add_to_tail(18)
                self.assertEqual(added_data.to_list(), self.list_add_to_tail[i])

    def test_add_to_head(self):
        for i in range(len(self.inputs)):
            with self.subTest([i, self.inputs[i]]):
                added_data = self.inputs[i]
                added_data.add_to_head(18)
                self.assertEqual(added_data.to_list(), self.list_add_to_head[i])

    def test_delete_node(self):
        for i in range(len(self.inputs)):
            with self.subTest([i, self.inputs[i]]):
                delete_data = self.inputs[i].delete_node(2)
                self.assertEqual(delete_data.to_list(), self.list_deleted_linked_lists[i])

    def test_get_left_node(self):
        for i in range(len(self.inputs)):
            with self.subTest([i, self.inputs[i]]):
                left_node = self.inputs[i].get_left_head()
                self.assertEqual(left_node.data, self.raw_inputs[i][0])

    def test_get_right_node(self):
        for i in range(len(self.inputs)):
            with self.subTest([i, self.inputs[i]]):
                left_node = self.inputs[i].get_right_head()
                self.assertEqual(left_node.data, self.raw_inputs[i][-1])
