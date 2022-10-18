class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    #  traversing the linked list
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    # appending a node in the linked list
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            cur = self.head
            while(cur.next is not None):
                cur = cur.next

            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
        return self.head

    # adding a node at the starting of the doubly linkedlist
    def insertBeginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = None
            new_node.prev = None
        else:
            cur = self.head
            new_node.next = cur
            cur.prev = new_node
            new_node.prev = None
            self.head = new_node
        return self.head

    # deleting a node in the doubly linked list
    def deleteNode(self, data):
        cur = self.head
        while cur:
            # case 1: deleting the node from the beginning
            if cur.data == data and cur == self.head:
                #  case 1.a linked list contains only one node
                if cur.next is None:
                    cur = None
                    self.head = None
                    return 
                # case 1.b linked list contains more than one node
                else:
                    next_node = cur.next
                    cur.next = None
                    next_node.prev = None
                    self.head = next_node
                    return 
            elif cur.data == data:
                # case 2: delete the node from middle
                if cur.next is not None:
                    # getting the previous and next node of the current node
                    next_node = cur.next
                    prev_node = cur.prev
                    # setting the prev and next pointer of the current node to null
                    cur.next = None
                    cur.prev = None
                    # assigning prev_node's next to the next_node.
                    prev_node.next = next_node
                    # assigning
                    next_node.prev = prev_node
                    return
                # case 3: delete the node from the last
                else:
                    prev_node = cur.prev
                    prev_node.next = None
                    cur.prev = None
                    return
            cur = cur.next
            
             

