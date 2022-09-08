from __future__ import annotations


class Node:
    def __init__(self, value: int = 0, next: Node = None) -> None:
        self.value = value
        self.next = next


class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def addFirst(self, newdata=int) -> None:
        if self.head is None:
            self.head = self.tail = Node(newdata)
        else:
            newnode = Node(newdata)
            newnode.next = self.head
            self.head = newnode
            self.size += 1
        return

    def addLast(self, newdata=int) -> None:
        if self.head is None:
            self.head = self.tail = Node(newdata)
        else:
            node = Node(newdata)
            self.tail.next = node
            self.tail = node
            self.size += 1

    def insertAfterNode(self, initial_node=int, inserted_node=int) -> None:
        if self.head is None and initial_node is None:
            self.head = self.tail = Node(inserted_node)
        else:
            cur = self.head
            newnode = Node(inserted_node)
            while cur:
                if cur.value == initial_node:
                    nextnode = cur.next
                    cur.next = newnode
                    newnode.next = nextnode
                cur = cur.next

    def swap(self, firstNode=int, secondNode=int) -> None:

        if (firstNode == secondNode):
            return
        else:
            prev_1 = None
            cur_1 = self.head

            while cur_1 and cur_1.value != firstNode:
                prev_1 = cur_1
                cur_1 = cur_1.next

            prev_2 = None
            cur_2 = self.head
            while cur_2 and cur_2.value != secondNode:
                prev_2 = cur_2
                cur_2 = cur_2.next

            if not cur_1 or not cur_2:
                return
            if prev_1:
                prev_1.next = cur_2
            else:
                self.head = cur_2
            if prev_2:
                prev_2.next = cur_1
            else:
                self.head = cur_1

            cur_1.next, cur_2.next = cur_2.next, cur_1.next

    def display(self) -> None:
        if self.head is None:
            raise ValueError('Linked list is empty')
        current = self.head
        while current is not None:
            print(current.value, end='')
            if current.next is not None:
                print(' -> ', end='')
            current = current.next
        print(' ')

    # def removeduplicate(self) -> None:
    #     if self.head is None:
    #         raise ValueError('Linked list is empty')
    #     current = self.head
    #     while current.next



x = LinkedList()
x.addFirst(4)
x.addFirst(3)
x.addFirst(2)
x.addFirst(1)
x.addLast(5)


x.insertAfterNode(3, 8)
x.display()

x.swap(3, 4)
x.display()
