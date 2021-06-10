class Node:
# Node class
    # default constructor
    def __init__(self, data):
        self.data = data
        self.next = None


#  Linked List class
class LinkedList:
    # default constructor
    def __init__(self):
        self.head = None

    # print function for the Linked List
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    # Linked List Insertion 
    # case 1. At the front of the linked list
    # csae 2. After a given name
    # case 3. At the end of the linked list

    # case 1 : time complexity O(1) bc of constant work 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 

    # case 2: time complexity O(1) bc of constant work 
    # case 2(a): when the previous node is given
    def insertAfterNode(self, prev_node, new_data):
        #  if the given prev_node doesnot exist in the list
        if prev_node is None:
            print("previous node doesn't exist")
            return
        # else if the prev_node exist in the list 
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # case2(b): when the data of the previous node is given
    def insertAfterData(self, prev_data, new_data):
        # if the prev_data is not exist in the linked list
        temp = self.head
        while(temp):
            if temp.data == prev_data:
                break;
            else:
                temp = temp.next;

        if(temp):
            new_node = Node(new_data)
            new_node.next = temp.next
            temp.next = new_node 

    
    # case 3: time complexity O(n) bc cost of traversing the list
    def append(self, new_data):
        new_node = Node(new_data)

        # if the list is empty
        if(self.head is None):
            self.head = new_node
            return

        last_node = self.head
        while(last_node.next):
            last_node = last_node.next

        last_node.next = new_node
            
    # case 4: linked list deletion of a node
    # case 4(a): iterative method
    def delete(self, key):
        temp = self.head
        
        # if the node in consideration is head node
        # Step 1: if the temp node is not empty
        if(temp != None):
            #  Step 2: if the data of head node is equal to the 
            # data need to be deleted. point the self to the next of 
            # temp node and delete the node
            if(temp.data == key):
                self = temp.next
                temp = None
                return

        while(temp != None):
            if (temp.data == key):
                break
            prev = temp
            temp = temp.next
        
        # if the node is not present in the list
        if(temp == None):
            print("No node present in the list having data as ", key)
            return

        prev.next = temp.next
        temp = None

    
    #  delete the the given position node
    def deleteNode(self, position):
        temp = self.head

        # if the position =0, the head node of the list to be deleted
        