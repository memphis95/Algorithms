class PallindromeSolution:
    def checkPallindrome(head):
        if head is None:
            return None
            
        tempList = []
        
        temp = head
        
        while temp:
            tempList.append(temp.data)
            temp = temp.next
            
        for i in range(len(tempList)//2 +1):
            if tempList[i] == tempList[len(tempList)-i-1]:
                pass
            else:
                return 0
        return 1
    
    def checkPallindromeOptimal(head):
        if head is None:
            return 0
        
        
        
        