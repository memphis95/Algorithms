class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node

    def __str__(self):
        return self.get_data()
        

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        node = Node(data)
        if self.get_head() == None:
            self.__head = node
            self.__tail = node
        else:
            self.get_tail().set_next(node)
            self.__tail = node
    
    def display(self):
        pass
        
    
    def find_node(self,data):
        '''
        find the node with the given data in the linked list.

        1. create a temporary node with the head of the linked list.
        2. while temp head node is not None
            a. if the given data is equal to the temp node data:
                return the temp node
            b. move the temp to next node
        3. if node is not found in the linked list return none.
        '''
        temp = self.get_head()
        while(temp is not None):
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None
       

    def insert(self,data,data_before):
        '''
        
        '''
        node = Node(data)
        node_before = self.find_node(data_before)
        if node_before is None:
            print(data_before, " is not present in the Linked List")
        elif data_before is None:
            self.__head = node
            self.__tail = node
        else:
            node.set_next(node_before.get_next())
            node_before.set_next(node)
            if node_before.get_next() == None:
                self.__tail = node
    
    def delete(self,data):
        delete_node = self.find_node(data)
        if delete_node == None:
            print(data," is not found in the Linkedlist")
        else:
            if self.get_head() == delete_node:
                self.__head = self.get_head().get_next()
                if self.__tail == delete_node:
                    self.__tail = None
            else:
                temp = self.get_head()
                while(temp is not None):
                    if temp.get_next() == delete_node:
                        temp.set_next(delete_node.get_next())
                        if delete_node == self.__tail:
                            self.__tail = temp
                            delete_node.set_next(None)
                        break
                    temp = temp.get_next()
                
                
                    
                
                    
        #Remove pass and write the logic to delete an element.
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


list1=LinkedList()
#Add all the required element(s)
#Delete the required element.
list1.add("Egg")
list1.add("Milk")
list1.add("Sugar")
list1.add("Rice")
print(list1)
list1.delete("Sugar")
print(list1)

list1.delete("Rice")
print(list1)  

list1.delete("Egg")
print(list1)  

list1.delete("Milk")
print(list1)  
