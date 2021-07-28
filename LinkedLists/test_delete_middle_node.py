import unittest
from LinkedLists.linked_list import LinkedListSingly
from LinkedLists.delete_middle_node import DeleteMiddleNodeSingly


class TestDeleteMiddleNode(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_input: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.input: LinkedListSingly = LinkedListSingly.create_linked_lists(self.raw_input)
        self.out_bool: list[bool] = [True] * (len(self.raw_input)-1) + [False]
        self.out: list[list[int]] = \
            [[self.raw_input[i] for i in range(len(self.raw_input)) if i > j] for j in range(len(self.raw_input))]
        self.out[-1].append(self.raw_input[-1])

    def test_delete_node(self) -> None:
        iterate: int = 0
        while len(self.raw_input[iterate:]) != 0:
            node = LinkedListSingly.create_linked_lists(self.raw_input[iterate:])
            with self.subTest(node.data):
                delete_middle_node: DeleteMiddleNodeSingly = DeleteMiddleNodeSingly(node)
                out_bool: bool = delete_middle_node.delete_node()
                out: LinkedListSingly = delete_middle_node.node
                self.assertEqual(out_bool, self.out_bool[iterate])
                self.assertEqual(out.to_list(), self.out[iterate])
            iterate += 1


