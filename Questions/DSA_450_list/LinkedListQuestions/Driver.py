from LinkedList import LinkedList, printList, Node
from SortedAlternatingly import Solution
from DeleteWithOutPointer import DeleteSolution
from DeleteMiddle import DelteMiddleSolution

if __name__ == '__main__':
    # arr = [int(x) for x in input().split()]
    
    inputFile = open("input.txt", "r")
    # outputFile = open("output.txt", "w")
    inputData = [line for line in inputFile]
    
    arr = [int(ele) for ele in inputData[0].split()]
    arrlen = len(arr)
    arrDict = {}
    for i in range(arrlen):
        if arr[i] in arrDict.keys():
            arrDict[arr[i]] = arrDict[arr[i]] + 1 
        else:
            arrDict[arr[i]] = 1 
    ans = 0
    for i in range(1, len(arr)):
        cnt = 0
        aj = arr[len(arr)-i]
        # print("value of aj :", aj)
        if aj == 1:
            continue
        if aj > 1 and ((3*aj)%(aj-1) ==0):
            ai = 3*aj / (aj-1)
        
        if ai in arrDict.keys():
            ans += arrDict[ai]
        
    print(ans)
        
    
    # Llist = LinkedList()
    # tail = None
    # for nodeData in [int(ele) for ele in inputData[0].split()]:
    #     tail = Llist.insert(nodeData, tail)
        
    # printList(Llist.head)
    # sol = Solution().sort1(Llist.head)
    # printList(sol)
    # node = Node(int(inputData[1]))
    # DeleteSolution.deleteNode(node)
    # printList(Llist.head)
    
    # sol = DelteMiddleSolution.deleteMiddle(Llist.head)
    # printList(sol)
     


