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
    def insertAfterNode(self, node, new_data):
        #  if the given node doesnot exist in the list
        if node is None:
            print("node doesn't exist")
            return
        # else if the node exist in the list 
        # create a new node 
        new_node = Node(new_data)
        # point the node's next to the new node's next
        new_node.next = node.next
        # point the next of the node to the new_node
        node.next = new_node

    # case2(b): when the data of the previous node is given
    def insertAfterData(self, data, new_data):
        # if the prev_data is not exist in the linked list
        temp = self.head
        # traversing the linked list for finding the data's position in linked list
        while(temp):
            if temp.data == data:
                break;
            else:
                temp = temp.next;

        if(temp):
            #  creating a new node with the new_data
            new_node = Node(new_data)
            #  point the new_node's next to the current node's next
            new_node.next = temp.next
            # point the current node to the new_node
            temp.next = new_node 

    
    # case 3: time complexity O(n) bc cost of traversing the list
    def append(self, new_data):
        # creating a new node with new_data
        new_node = Node(new_data)

        # if the list is empty, assigning the head to the new node
        if(self.head is None):
            self.head = new_node
            return
        # currNode as temp variable for traversing the list.
        currNode = self.head
        while(currNode.next):
            currNode = currNode.next
        # assigning the last node's next to the the new node.
        currNode.next = new_node
            
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
        # temp node pointing to head node
        temp = self.head
        # intialize count equal to zero
        count = 0
        # traverse till the position is reached or till the last node of the list
        while temp.next and count != position:
            temp =  temp.next
            count += 1
        # if the the temp node is last node of the the list
        if temp.next is None:
            return 
        # point temp node's next to the the next of next of temp node
        temp.next = temp.next.next

        