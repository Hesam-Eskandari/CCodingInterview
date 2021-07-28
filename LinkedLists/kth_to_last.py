from LinkedLists.linked_list import LinkedListSingly


class KthToLast:
    def __init__(self, linked_list: LinkedListSingly) -> None:
        self.linked_list: LinkedListSingly = linked_list
        self.k: int = 1

    def __call__(self, k: int, method: int = 0) -> LinkedListSingly or None:
        if type(k) != int:
            raise TypeError("k must be integer, got {t}".format(t=type(k)))
        if k < 0:
            raise ValueError("expected \"k\" to be a none-negative integer, got {v}".format(v=k))
        if k > 0:
            self.k = k
        if method == 0:
            return self.known_length()
        else:
            return self.two_pointer()

    def known_length(self) -> LinkedListSingly or None:
        length: int = len(self.linked_list)
        if not length or self.k > length:
            return None
        node = self.linked_list
        for i in range(length-self.k):
            node = node.next
        return node

    def two_pointer(self) -> LinkedListSingly or None:
        node_ahead: LinkedListSingly = self.linked_list
        node_delay: LinkedListSingly = self.linked_list
        if node_ahead is None:
            return None
        count: int = 1
        while node_ahead.next is not None:
            if count >= self.k:
                node_delay = node_delay.next
            node_ahead = node_ahead.next
            count += 1
        if count < self.k:
            return None
        return node_delay

