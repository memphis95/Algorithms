from LinkedList import Node

class Solution:
    # solution1
    def sort(self, head) -> None:
        '''
        Approach:
        1. create a empty list
        2. Iterate over the linked list
            2.A. append the data of the current node
                to the list
        3. using sort function to sort the list
        4. Iterate over linkedlist
            4.A replace the current node data with the list[i] element
        5. return the head
        
        time complexity - O(n) we are iterating over linked list
        space complexity - O(n) space required for the list
        '''
        dummyList = []
        current = head
        while current:
            dummyList.append(current.data)
            current = current.next
        dummyList.sort()
        current2 = head
        i = 0
        while current2:
            current2.data = dummyList[i]
            current2 = current2.next
            i += 1
            
        
        return head
    
    #  solution 2
    def sort1(self, head) -> None:
        '''
        Approach: create separate linked list for ascending and descending
                    reverse the descending list and append the reverse list 
                    to the ascending list
        
        1. create dummy node for the  ascending and descending linked list
        2. iterate over the original llinked list
            2.A append the current node to the ascending list tail node
            2.B update the current with current.next
            2.C update the ascending list tail node to next of tail node
            2.D if current is not none
                2.D.I  append the current node to the descending lsit 
                2.D.II update the tail node of descending list
                
        3. reverse the descending list
        4. append the tail of the ascending list to the head of the descending list
        5. return the head of the ascending list
        
        time complexity - O(N) - only iterating over the linked list
        space complexity - O(1) - extra space required for storing the dummy node
            
        
        '''
        aHead = Node(0)
        aTail = aHead
        aHead.next = None
        
        dHead = Node(0)
        dTail = dHead
        dHead.next = None
        
        # print("ahead pointer: ", aHead.data)
        # print("dHead : ", dHead.data)
        
        current = head
        while current:
            newNode = current
            current = current.next
            aTail.next = newNode
            aTail = aTail.next
            
            if current:
                newNode = current
                current = current.next
                dTail.next = newNode
                dTail = dTail.next 
                
        aHead, aTail.next = aHead.next, None
        dHead, dTail.next = dHead.next, None
        
        # print("ahead pointer: ", aHead.data)
        # print("dHead : ", dHead.data)
        
        prev = None
        current1 = dHead
        while current1:
            next = current1.next
            current1.next = prev 
            prev = current1
            current1 = next
        dHead = prev
        aTail.next = dHead
    
        return aHead