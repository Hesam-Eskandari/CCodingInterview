from LinkedLists.linked_list import LinkedListSingly

"""
Remove Dups
Cracking the coding interview, 6th edition, page 94
"""


class RemoveDuplicates:
    def __init__(self, linked_list: LinkedListSingly):
        self.linked_list = linked_list

    def __call__(self, no_additional_structure=True) -> LinkedListSingly:
        if no_additional_structure:
            return self._get_removed_dups_with_no_additional_structure
        else:
            return self._get_remove_dups_using_additional_structure

    @property
    def _get_removed_dups_with_no_additional_structure(self) -> LinkedListSingly:
        node = self.linked_list
        if node is None:
            raise ValueError("error validating linked list. None is not a linked list")
        while node.next is not None:
            node_inner = node.next
            while node_inner.data == node.data:
                node.next = node.next.next
                if node.next is None:
                    return self.linked_list
                node_inner = node.next
            while node_inner.next is not None:
                if node_inner.next.data == node.data:
                    node_inner.next = node_inner.next.next
                    if node_inner.next is None:
                        break
                node_inner = node_inner.next
            node = node.next
        return self.linked_list

    @property
    def _get_remove_dups_using_additional_structure(self) -> LinkedListSingly:
        hmap: dict[any, bool] = dict()
        node = self.linked_list
        if node is None:
            raise ValueError("error validating linked list. None is not a linked list")
        hmap[node.data] = True
        while node.next is not None:
            if hmap.get(node.next.data, False):
                node.next = node.next.next
                if node.next is None:
                    break
            else:
                hmap[node.next.data] = True
            node = node.next
        return self.linked_list
