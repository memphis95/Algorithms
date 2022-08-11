class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

    
# searching for the element in the linked list
def search(head, x):
    cur = head
    pos = 1
    if cur == None:
        return -1
    while(cur != None):
        if (cur.key == x):
            return pos
        else:
            pos += 1
            cur = cur.next
    return -1

def printList(head):
    cur = head
    if cur == None:
        return
    while(cur != None):
        print(cur.key, end = " ")
        cur = cur.next

def insertBeginning(head, key):
    tempNode = Node(key)
    # if (head == None):
    #     head = tempNode  
    # else:
    #     tempNode.next = head
    #     head = tempNode
    # return head
    tempNode.next = head
    return tempNode

def insertEnd(head, key):
    tempNode = Node(key)
    if(head == None):
        head = tempNode
    else:
        cur = head
        while (cur.next != None):
            cur = cur.next
        cur.next = tempNode
    return head

def insertPosition(head, pos, data):
    tempNode = Node(data)
    cur = head
    # inserting at the head of linked list
    if pos == 1:
        tempNode.next = head
        return tempNode
    
    for i in range(pos-2):
        cur = cur.next
        if cur == None:
            return head
    tempNode.next = cur.next
    cur.next = tempNode
    return head

def deleteFNode(head):
    if (head == None):
        return None
    head = head.next
    return head

def deleteLNode(head):
    if head == None or head.next == None:
        return None
    cur = head 
    while(cur.next.next != None):
        cur = cur.next
    cur.next = None
    return head

def sortedInsert(head, data):
    tempNode = Node(data)
    if head == None:
        return tempNode
    elif data < head.key:
        tempNode.next = head
        return tempNode
    cur = head 
    while(cur.next !=None and cur.next.key < data ):
        cur = cur.next
    tempNode.next = cur.next
    cur.next = tempNode
    return head

def reverseList(head):
    stack = []
    cur = head
    while cur is not None:
        stack.append(cur.key)
        cur = cur.next 
    cur = head
    while cur is not None:
        cur.key = stack.pop()
        cur = cur.next
    return head

# driver code for the insert at the beginning
head = None
# head = insertBeginning(head, 10)
# head = insertBeginning(head, 20)
# head = insertBeginning(head, 30)
head = insertEnd(head, 10)
head = insertEnd(head, 20)
head = insertEnd(head, 30)
printList(head)

# temp1 = Node(10)
# temp2 = Node(20)
# temp3 = Node(30)
# temp1.next = temp2
# temp2.next = temp3
# head = temp1
# printList(head)
# print(search(head, 20))

