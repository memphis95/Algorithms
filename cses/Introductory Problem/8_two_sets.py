"""
PS: To divide the numbers 1,2,...,n into two sets of equal sum
"""
def is_two_set(n):
    a = []
    b = [] 
    sum_n = (n * (n+1))//2
    if sum_n%2 == 0:
        for i in range(n,0, -1):
            if sum(a) > sum(b):
                b.append(i)
            elif sum(a) < sum(b):
                a.append(i)
            else:
                a.append(i)

        if sum(a) == sum(b):
            print("YES")
            print(len(a))
            print(*a, sep=' ')
            print(len(b))
            print(*b, sep=' ')
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    number = int(input())
    is_two_set(number)

"""
Problem faced by the above approach is that for large numbers it result in the TLE
example : 260443
"""