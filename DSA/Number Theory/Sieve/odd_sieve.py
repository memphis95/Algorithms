"""
resource: GFG Bitwise Sieve
Simple Sieve algorithm optimize over the auxillary memory required by
removing all the even numbers(divisible by 2) from the array as they are not prime numbres 
except 2.
"""

def optimiseSieve(n):
    # is_prime[] boolean array, each index corresponds to the odd number(i*2 +1)
    is_prime = [1 for i in range(int(n/2)+1)]
    # starting from the number 3
    i = 3
    while i*i <= n:
        if is_prime[int(i/2)]:
            for j in range( i**2, n+1, i*2):
                # check if multiple of i is not even number
                if j%2 != 0:
                    is_prime[int(j/2)] = 0
        # print("value of i is :", i, "value of i/2 is: ",int(i/2)," value of the array is: ", is_prime)
        i += 2
    print( 2, end = " ")
    for i in range(3, n+1, 2):
        if is_prime[int(i/2)]:
            print(i, end = " ")


# driver code
n = 100
optimiseSieve(n)