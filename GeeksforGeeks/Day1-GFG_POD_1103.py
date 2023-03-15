from typing import List



class Solution:
    
    def numCount(self, A: List[int], number: int):
        count = 0
        for item in A:
            if item == number:
                count += 1
        
        return count
        
    def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        # code here
        ans = []
        for item in Q:
            l,r,k = item[0], item[1], item[2]
            eleCount = 0
            for i in range(l, r+1):
                print("value of i is:", i)
                
                print("count of element ",self.numCount(A[i:N],A[i]) )
                # if self.numCount(A[i:N],A[i]) == k:
                #     eleCount += 1
                # print(eleCount)
                if A[i:N].count(A[i]) == k:
                    eleCount += 1
            ans.append(eleCount)
            
        return ans
                
                    
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        num = int(input())
        
        
        A=IntArray().Input(N)
        
        
        Q=IntMatrix().Input(num, 3)
        
        obj = Solution()
        res = obj.solveQueries(N, num, A, Q)
        
        IntArray().Print(res)
        

# } Driver Code Ends