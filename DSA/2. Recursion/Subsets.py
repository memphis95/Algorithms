def PowerSet(string):
    n = len(string)
    powSize = pow(2, n)
    for counter in range(0, powSize):
        for j in range(0, n):
            print(counter, j ,(1 << j), (counter & (1 << j)))
            if((counter & (1 << j)) > 0):
                print(string[j], end="")
            print("")
        print(" ")

PowerSet('abc')
