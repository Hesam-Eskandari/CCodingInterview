from LinkedLists.linked_list import LinkedListSingly

"""
    The last node cannot be deleted.
    Head is never given. Only the node to delete is given
"""


class DeleteMiddleNodeSingly:
    def __init__(self, node: LinkedListSingly) -> None:
        self.node: LinkedListSingly = node

    def delete_node(self) -> bool:
        if self.node is None or self.node.next is None:
            return False
        next_node = self.node.next
        self.node.data = next_node.data
        self.node.next = next_node.next
        return True
