
#  brute force solution 
# def setZeros(matrix) -> None:
# 	# Write your code here.
# for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j] == 0:
#                     for k in range(len(matrix)):
#                         if matrix[k][j] != 0:
#                             matrix[k][j] = None
#                     for l in range(len(matrix[i])):
#                         if matrix[i][l] != 0:
#                             matrix[i][l] = None

#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if(matrix[i][j] == None):
#                     matrix[i][j] = 0
## Time complexity - (len(row) * len(column)) + (len(row)+len(col)) + (len(row)+len(col))
## TIme complexity ~ O(n^3)

def setZerosBetter(matrix) -> None:
    row_mask = [0] * len(matrix)
    col_mask = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row_mask[i] = 1
                col_mask[j] = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(row_mask[i] or col_mask[j]):
                matrix[i][j] = 0


    print(matrix)

    # Time complexity - O(m*n) ~ O(n^2)
    # Space complexity : O(n) + O(m)


# def setZerosOptimal(matrix) -> None:
#     col0 = 1

#     for i in range(len(matrix)):
#         if matrix[i][0] == 0:
#             col0 = 0
#     print("value of col0 is: ", col0)

#     for i in range(len(matrix[0])):
#         if matrix[0][i] == 0:
#             matrix[0][0] = 0

#     for i in range(1, len(matrix), 1):
#         for j in range(1, len(matrix[i]), 1):
#             if matrix[i][j] == 0:
#                 matrix[i][0] = 0
#                 matrix[0][j] = 0

    

#     print("matrix before applying change is: ",matrix)
        
#     for i in range(1,len(matrix)):
#         for j in range(1, len(matrix[i])):
#             if matrix[i][j] != 0:
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0
    
    
        
#     if matrix[0][0] == 0:
#         for i in range(len(matrix[0])):
#             matrix[0][i] = 0

#     if col0 == None:
#         for i in range(len(matrix)):
#             matrix[i][0] = 0  
        
#     print("matrix after change is: ", matrix)

def setZerosOptimal(matrix) -> None : 
    rows, cols = len(matrix), len(matrix[0])
    row_zero = False

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True
    print(row_zero)
    print(matrix)
    for r in range(1, rows):
        for c in range(1, cols):
            if(matrix[r][c] != 0):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0
    print(matrix)
            
    if row_zero:
        for c in range(cols):
            matrix[0][c] = 0
    print(matrix)
    

def setZerosBetter1(matrix):
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)


    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in rows or j in cols:
                matrix[i][j] = 0





if __name__ == "__main__":
    # print("hello world")
    arr = [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
    # arr = [[1, 0],[2, 7], [3, 0], [4, 8],[3, 3]]
    # setZerosBetter(arr)
    setZerosOptimal(arr)
