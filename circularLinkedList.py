from __future__ import annotations


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    # this code adds element from the front eg 1->2->3->1 prepend(0) = 0->1->2->3->0

    def prepend(self, data) -> None:
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head
        if self.head is None:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node
        self.size += 1

    # this code adds element from the back eg 1->2->3->1 prepend(4) = 1->2->3->4->1

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

    # this function removes element from every possible case .

    def remove(self, key) -> None:
        if self.head is None:
            raise ValueError('CircularLinked list is empty')

        elif self.head == self.head.next and self.head.data == key:
            self.head = None

        elif self.head.data == key:
            if self.head.next is not None:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                cur.next = self.head.next
                print('This is the cur', cur.data)
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
        self.size -= 1

    # this method removes by specifying a node directly but doesnt work atall.

    def remove_node(self, node):
        if self.head == node:
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
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next
        self.size -= 1

    # this method slices the circular-linkedlist by using the length property.

    def split_list(self) -> None:
        if self.size == 0:
            return None
        if self.size == 1:
            return self.head

        mid = self.size // 2
        prev = None
        count = 0
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        scllist = CircularLinkedList()  # creates a new List to store the othe part
        while cur.next is not self.head:
            scllist.append(cur.data)
            cur = cur.next
        scllist.append(cur.data)

        self.print_list()  # calling the print_statemnt.
        print("\n")
        scllist.print_list()

    def josephus_problem(self, step) -> None:
        cur = self.head
        while self.size > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("Kill", str(cur.data))
            self.remove_node(cur)
            cur = cur.next

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

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


cllist = CircularLinkedList()

cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
print(len(cllist))


cllist.josephus_problem(2)
cllist.print_list()
