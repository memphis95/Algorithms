class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        while position > 1:
            current = current.next
            position = position-1
        if current is not None:
            return current
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        cur = self.head
        if position == 1:
            new_element.next = cur
            self.head = new_element
        while cur.next is not None:
            position = position - 1
            if position == 1:
                new_element.next, cur.next = cur.next, new_element
            else:
                cur = cur.next
            
    
    def delete(self, value):
        """Delete the first node with a given value."""
        prev = self.head
        if prev.value == value:
            self.head = prev.next
        cur = prev.next
        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                break
            else:
                prev, cur = cur, cur.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)