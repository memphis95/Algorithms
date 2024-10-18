from LinkedList import LinkedList, Node
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        temp1, temp2 = '', ''
        while l1:
            temp1 += str(l1.data)
            l1 = l1.next
        while l2:
            temp2 += str(l2.data)
            l2 = l2.next
        print(temp1[::-1], temp2[::-1])
        print(int(temp1), int(temp2))
        op = int(temp1[::-1]) + int(temp2[::-1])
        print('output :', op )
        op = str(op)[::-1]
        print(op)
        for i in op:
            print(i)

         
    
if __name__ == '__main__':
    arr1 = [2,4,3]
    arr2 = [5,6,4]
    
    l1 = LinkedList()
    l2 = LinkedList()
    tail1 = None
    tail2 = None
    for i in arr1:
        tail1 = l1.insert(i, tail1)
    for i in arr2:
        tail2 = l2.insert(i, tail2)
    sol = Solution()
    sol.addTwoNumbers(l1.head, l2.head)