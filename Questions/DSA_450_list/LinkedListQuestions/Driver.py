from LinkedList import LinkedList, printList
from SortedAlternatingly import Solution


if __name__ == '__main__':
    # arr = [int(x) for x in input().split()]
    
    inputFile = open("input.txt", "r")
    # outputFile = open("output.txt", "w")
    inputData = [line for line in inputFile]
    
    Llist = LinkedList()
    tail = None
    for nodeData in [int(ele) for ele in inputData[0].split()]:
        tail = Llist.insert(nodeData, tail)
        
    # printList(Llist.head)
    sol = Solution().sort1(Llist.head)
    printList(sol)
  
    
    # inputFile.close()
    # outputFile.close()

