class DelteMiddleSolution:
    
    def deleteMiddle(head):
        if head is None or head.next is None:
            return None
        
        slowPtr = head
        fastPtr = head
        prev = None
        
        while fastPtr is not None and fastPtr.next is not None:
            fastPtr = fastPtr.next.next
            prev = slowPtr
            slowPtr = slowPtr.next
            
        prev.next = prev.next.next
        
        return head
       
    
        
    