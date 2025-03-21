import sys

class Solution():
   
    
    def specialPalindrome(self,s1, s2):
        #your code goes here  cxz
        # base case 1
        if len(s1) < len(s2):
            return -1
        # base case 2
        
        
        # generating all possible s1 strings with s2 as a substring
        cost_arr= []
        temp_arr = []
        min_cost = sys.maxsize
        for i in range(0,(len(s1)- len(s2)+1)):
            s =s1[0:i] + s2 + s1[i+len(s2)-1:-1]
            for cha in s:
                print(cha, end=" ")
            print()
            cost = 0
            for j in range(i, i+len(s2)):
                if s1[j]!=s[j]:
                    cost += 1
            print(cost)
            isPallindrome = True
            for k in range(len(s)):
                if s[k] == s[len(s) - k-1]:
                    pass
                else:
                    isPallindrome =  False
                    break
            print(isPallindrome)
            
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s1, s2 = input().split()
        obj = Solution()
        print(s1,s2)
        print(obj.specialPalindrome(s1,s2))
# } Driver Code Ends