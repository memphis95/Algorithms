# 
def nCr(n, r):
    res = 1 
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res 

# variation 1 : print the Pascal Traingle
def printPascalTriangle(rowNumber):
    for i in range(1, rowNumber+1):
        tmp = []
        for j in range(1, i+1):
            tmp.append(nCr(i-1,j-1))
        print(tmp)


# variation 2:  Given row number r and column number c. 
# Print the element at position (r, c) in Pascal’s triangle.
def printElement(rowNumber, colNumber):
    print(nCr(rowNumber-1,colNumber-1))

# variation 3: Fiven the row number r. Print the nth-row
def printNRow(rowNumber):
    tmp = []
    for j in range(1, rowNumber+1):
        tmp.append(nCr(rowNumber-1,j-1))
    print(tmp)

if __name__ == "__main__":
    printPascalTriangle(5)
    printElement(5,3)
    printNRow(7)


