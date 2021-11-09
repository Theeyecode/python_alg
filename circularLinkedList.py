from __future__ import annotations


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def prepend(self, data):
        if not self.head:
            anew_node = Node(data)
            self.head = anew_node
            self.head.next = self.head
        else:
            new_node = Node(data)

            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def append(self, data) -> None:
        if not self.head:
            anew_node = Node(data)
            self.head = anew_node
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node

            new_node.next = self.head
        self.size += 1

    def remove(self, key) -> None:
        if self.head is None:
            raise ValueError('CircularLinked list is empty')
        elif self.head.data == key:
            if self.head.next is not None:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def print_list(self):
        if self.head is None:
            print('Empty')
        cur = self.head
        while cur:
            print(cur.data, end='->')
            cur = cur.next
            if cur.next == self.head:
                print(cur.data, '->', self.head.data)
                break

        # print('')


cllist = CircularLinkedList()
cllist.prepend('0')
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.remove("C")


cllist.print_list()
