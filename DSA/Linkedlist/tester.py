from Linkedlist import Node
from Linkedlist import LinkedList

#  main function 
if __name__ == '__main__':
    #  sample data 
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second;
    second.next = third;
    # intial Linked List
    llist.printList()

    #  Inserting node at the front 
    llist.push(0)

    # updating the Linked List
    print("new updated list after adding element at the stating of the list")
    llist.printList()

    # Inserting element after specific element
    llist.insertAfterData(2, 4)
    print("updated linked list after insertion after the given node")
    llist.printList()

    llist.insertAfterNode(second, 5)
    print("updated linked list after insertion after the given node")
    llist.printList()

    llist.append(6)
    print("updated list after appending data")
    llist.printList()

    llist.delete(9)
    print("updated list after deleting an element")
    llist.printList()
