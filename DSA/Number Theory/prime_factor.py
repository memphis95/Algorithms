"""
"""
# naive approach
def primeFact(n):
    for i in range(2, n+1):
        if (n %i == 0):
            cnt = 0
            while (n%i == 0):
                cnt += 1
                n = n/i
            print(i,"^",cnt, end = " * ")


# driver code
n = 1210
primeFact(n)
