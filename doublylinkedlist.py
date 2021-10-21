from __future__ import annotations


class Node:
    def __init__(self, value=int, next: Node = None, prev: Node = None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class doublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def addBegining(self, data=int) -> None:
        if self.head is None and self.tail is None:
            node = Node(data)
            node.prev = None
            self.head = node
        else:
            current = self.head
            new_node = Node(data)
            current.prev = new_node
            new_node.next = current
            self.head = new_node
            new_node.prev = None

        self.size += 1

    def addEnd(self, data=int) -> None:
        if self.head is None and self.tail is None:
            new_node = self.head = self.tail = Node(data)
            new_node.prev = None
        else:
            current = self.tail
            new_node = Node(data)
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None

        self.size += 1

    def delete(self, key) -> None:
        current = self.head
        while current:
            if current.value == key and current == self.head:
                if current.next is None:
                    current = None
                    self.head = None
                    return
                else:
                    next = current.next
                    next.prev = None
                    current.next = None
                    current = None
                    self.head = next
                    return
            elif current.value == key:
                if current.next != None:
                    # next_node = current.next
                    # prev_node = current.prev

                    # current.prev = None
                    # next_node.prev = prev_node
                    # current.next = None
                    current = None
                    current.prev = None
                    current.next = None
                    return

                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return

            current = current.next
        size -= 1

    def display(self) -> None:
        if self.head is None and self.tail is None:
            raise ValueError('Linked list is empty')
        current = self.head
        while current is not None:
            # if current.prev is not None:
            #     print('->', previous.value, current.value, end='')

            print(current.value, end='')

            if current.next is not None:
                print(' -> ', end='')
            previous = current.prev
            current = current.next

        print(' ')

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next


dll = doublyLinkedList()

dll.addBegining(2)
dll.addBegining(3)
dll.addBegining(13)

dll.addBegining(5)
dll.addBegining(10)
# dll.delete(13)


dll.print_list()
