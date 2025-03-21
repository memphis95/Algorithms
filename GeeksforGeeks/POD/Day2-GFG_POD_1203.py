class Solution:
    def findMaxRow(self, mat, N):
        # Code here
        # Approach - as the matrix is binary we can take sum of the rows 
        ans = [0]*2
        row_number = -1
        max_count = 0

        for i in range(N):
            if sum(mat[i]) > max_count:
                max_count = sum(mat[i])
                row_number = i
        ans[0] = row_number
        ans[1] = max_count

        return ans

        # complexity ~ O(N^2)




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat = []
        for i in range(n):
            A = [int(x) for x in input().split()]
            mat.append(A)
        ob=Solution()
        ans = []
        ans = ob.findMaxRow(mat, n)
        for i in range(2):
            print(ans[i], end =" ")
        print()
# } Driver Code Ends