#User function Template for python3
import sys


class Solution:
    def maxPossibleValue(self, N, A, B): 
        #code here
        # creating frequency dict
        # freq = {}
        # for i in range(N):
        #     if A[i] not in freq:
        #         freq[A[i]] = B[i]
        #     else:
        #         freq[A[i]] += B[i]
            

        
        # print("Frequency dictionary: ", freq)
        # dict2 = {}
        # # choosing the lengths with freq >= 2 
        # for i in freq:
        #     if freq[i] >= 2:
        #         dict2[i] = freq[i]
        
        # print("dict2 befor processing: ", dict2)
        # square_sum = 0
        # square_side = 0
        # rect_sum = 0
        # # constructing square
        # for i in dict2:
        #     if dict2[i] >= 4 and i > square_side:
        #         if 4*dict2[i] > square_sum:
        #             square_sum = 4*i
        #             square_side = i
        # # updating freq dict - rducing the freq of selected
        # # length of side
        # if square_side > 0:
        #     dict2[square_side] -= 4
        # print("dictionary 2: ", dict2)
        # dict3 = {}
        # for i in dict2:
        #     if dict2[i] >= 2:
        #         dict3[i] = dict2[i]
        # print("dictionary is: ", dict3, type(dict3))
        # # constructing rectangle
        # sort_dict = sorted(dict3.items(), reverse=True)
        # print("sorted dict: ", sort_dict, type(sort_dict))
 
        # rect_sum = 2* (sort_dict[0][0] + sort_dict[1][0])
        # print(square_sum, rect_sum)
        # return square_sum + rect_sum

        total_sum = 0
        total_sticks = 0

        min_length_stick = sys.maxsize

        for i in range(N):
            len = A[i]
            units = B[i]
            if(units%2 != 0):
                units -= 1
            if units >= 2:
                min_length_stick = min(len, min_length_stick)
            total_sum += len * units
            total_sticks += units
            
        if total_sticks%4 != 0:
            total_sum -= min_length_stick * (total_sticks%4)
        
        return total_sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPossibleValue(N, A, B)
        print(ans)

# } Driver Code Ends