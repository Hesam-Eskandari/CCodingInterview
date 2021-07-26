class LinkedListSingly:
    def __init__(self, data: any) -> None:
        self.data: any = data
        self.next: LinkedListSingly or None = None

    def __len__(self) -> int:
        # self must be pointing to the head of the linked list
        node = self
        count = 0
        if node is None:
            return count
        count += 1
        while node.next is not None:
            node = node.next
            count += 1
        return count

    def length(self) -> int:
        return self.__len__()

    def add_to_tail(self, data: any):
        temp = self
        while temp.next is not None:
            temp = temp.next
        else:
            temp.next = LinkedListSingly(data)
        return self

    def delete_node_to_right(self, data: any):
        head = self
        if head is None:
            return
        if head.data == data:
            head = head.next
        temp = head
        if temp is None:
            return None
        while temp is not None and temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
            temp = temp.next
        return head

    def to_list(self) -> list[any]:
        # return a list of data starting from the current node
        node = self
        lst = list()
        if node is not None:
            lst.append(node.data)
        while node.next is not None:
            lst.append(node.next.data)
            node = node.next
        return lst

    @classmethod
    def create_linked_lists(cls, lst: list[any]):
        if len(lst) == 0:
            raise ValueError("error creating a linked list, linked lists cannot be empty,"
                             " given: {list_num}".format(list_num=lst))
        head = LinkedListSingly(lst[0])
        node = head
        for i in range(len(lst)-1):
            node.next = LinkedListSingly(lst[i+1])
            node = node.next
        return head


class LinkedListDoubly:
    def __init__(self, data: any):
        self.data = data
        self.next: LinkedListDoubly or None = None
        self.prev: LinkedListDoubly or None = None

    def __len__(self) -> int:
        node = self.get_left_head()
        count = 0
        if node is None:
            return count
        count += 1
        while node.next is not None:
            node = node.next
            count += 1
        return count

    def get_left_head(self):
        node = self
        if node is None:
            return None
        while node.prev is not None:
            node = node.prev
        return node

    def get_right_head(self):
        node = self
        if node is None:
            return None
        while node.next is not None:
            node = node.next
        return node

    def length(self) -> int:
        return self.__len__()

    def length_to_right(self) -> int:
        node = self
        count = 0
        if node is None:
            return count
        count += 1

        while node.next is not None:
            node = node.next
            count += 1
        return count

    def length_to_left(self) -> int:
        node = self
        count = 0
        if node is None:
            return count
        count += 1

        while node.prev is not None:
            node = node.prev
            count += 1
        return count

    def add_to_head(self, data: any):
        head = self.get_left_head()
        head.prev = LinkedListDoubly(data)
        head.prev.next = head
        return head.prev

    def add_to_tail(self, data: any):
        end = self.get_right_head()
        end.next = LinkedListDoubly(data)
        end.next.prev = end
        return end.next

    def delete_node(self, data: any):
        head = self.get_left_head()
        if head is None:
            return None
        elif head.data == data and head.next is not None:
            head = head.next
            head.prev = None
        node = self
        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next
                if node.next is None:
                    break
                node.next.next.prev = node
            node = node.next
        return head

    def to_list(self) -> list[any]:
        lst = list()
        node = self.get_left_head()
        if node is None:
            return lst
        if node is not None:
            lst.append(node.data)
        while node.next is not None:
            lst.append(node.next.data)
            node = node.next
        return lst

    @classmethod
    def create_linked_lists(cls, lst: list[any]):
        if len(lst) == 0:
            raise ValueError("error creating a linked list, linked lists cannot be empty,"
                             " given: {list_num}".format(list_num=lst))
        head = LinkedListDoubly(lst[0])
        node = head
        for i in range(len(lst)-1):
            node.next = LinkedListDoubly(lst[i+1])
            node.next.prev = node
            node = node.next
        return head
