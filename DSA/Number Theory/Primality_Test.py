import math


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True


if __name__ == "__main__":
    t = int(input())
    for i in range(0,t):
        n = int(input())
        result = isPrime(n)
        if result:
            print("yes")
        else:
            print("no")