"""
Given : an array arr and a number num.

compute the prime factors and their power of the num ((p^a)(q^b)(r^c)).
return the sum : a*arr[p] + b*arr[q] + ...
"""
import math
def sumPrimeFactorArray(arr, num):
    # intializing dictionary to store prime factors as keys and their powers as values.
    primeDict = {} 
    # intial count 
    count = 0
    # if number is divisible by 2(first prime number) add the {2, power of 2 } in the dict

    while(num%2 == 0):
        count +=1
        num = num/2
    if count>0:
        primeDict[2] = count
#  as all the even number are divisible by 2, only odd numbers are left
#  iterate from 3 to sqrt(number)
    for i in range(3, int(math.sqrt(num)+1), 2):
        count = 0
        while(num%i == 0):
            count += 1
            num = num / i
        if count>0:
            primeDict[i] = count
    sum = 0
    for key,value in primeDict.items():
        sum = sum + value * arr[key]
    print(primeDict, sum)

arr = [1,2,3,4,5,6,7,8,9,10]
num = 900
sumPrimeFactorArray(arr, num)