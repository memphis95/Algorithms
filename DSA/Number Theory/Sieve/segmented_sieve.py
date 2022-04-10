"""
Resource : GFG segmented Sieve
"""

import math
# holds the prime numbers in range [2, sqrt(n)]
prime = []

def simpleSieve(limit):
    # intialize the is_prime array with the True boolean values
    is_prime = [True for i in range(limit+1)]
    # setting boolean for 0 and 1 as false as they are not prime numbers
    is_prime[0] = is_prime[1] = False
    i = 2
    while( i*i <= limit):
        if(is_prime[i]):
            for j in range(i **2, limit+1, i):
                is_prime[j] = False
        i += 1
    
    # code for entering the prime values into the prime array
    for i in range(limit+1):
        if is_prime[i]:
            prime.append(i)
            print(i, end = " ")

    

    

def segmentedSieve(n):
    segment_len = int(math.floor(math.sqrt(n))+1)
    print("segment length is: ", segment_len)
    # calculating primes in 1st segment
    simpleSieve(segment_len)

    low = segment_len
    high = low + segment_len

    while low < n :
        #  if the value of high is greater than the number 
        if high> n:
            high = n

        # taking an boolean array is_prime[] 
        is_prime = [True for i in range(segment_len+1)]
        for i in range(len(prime)):

            #first number in segment divisible  by current prime number
            loLim = int(math.floor(low/prime[i])*prime[i])
            if loLim < low:
                loLim += prime[i]

            for j in range(low, high, prime[i]):
                is_prime[j-low] = False
            
        # printing the prime values in the current segment
        for i in range(low, high):
            if is_prime[i-low]:
                print(i, end = " ")


        # updating the value of the low and high
        low += segment_len
        high += segment_len




#  driver code
n = 100
print("Primes smaller than", n, ": ")
segmentedSieve(100)
