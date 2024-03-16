
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def insert(self, data, tail):
        node = Node(data)
        
        if not self.head:
            self.head = node
            return node
        tail.next = node
        return node
    
    def deleteNode(head, pos):
        if head is None:
            return None
    
        index = 0
        cur = head
        while cur.next and index < pos:
            prev = cur
            cur = cur.next
            index += 1
        
        if index < pos:
            return head
        elif index == 0:
            return head.next
        else:
            prev.next = cur.next
            return head
        
def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
            
