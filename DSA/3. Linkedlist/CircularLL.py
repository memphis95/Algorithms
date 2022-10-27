class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def append(self, data):
        new_node = Node(data)

        # condition 1: if the list is empty
        if self.head == None:
            self.head = new_node 
            new_node.next = self.head

        # condition 2: if the list is not empty
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = cur

        # condition 1: if list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        # condition 2: if list is not empty
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node


