def uniqueRow(row, col, M):
    #complete the function
    # create an empty array
        ans = []
        # iterate from the last row to the first rwow of matrix
        for i in range(row-1, -1 , -1):
            # assuning that the current row is unique
            unique = True
            # for rows from 0th index to the selected row
            for ele in M[0:i]:
                # if sum of result of bitwise operations of row elements is equal to 
                if sum([M[i][j]^ele[j] for j in range(col)]) == 0:
                    unique = unique and False
                else:
                    unique = unique and True
            if unique:
                ans.insert(0, M[i])
        # if M[i] not in ans:
        #     ans.insert(0, M[i])
        print(ans)
    
uniqueRow(3,4,[[1,1,0,1],[1,0,0,1],[1,1,0,1]])
# print([[1,1,0,1],[1,0,0,1],[1,1,0,1]].index([1,1,0,1]))

# uniqueRow(10,1,[[1], [1], [0], [0], [0], [1], [0], [1], [0], [1]])
