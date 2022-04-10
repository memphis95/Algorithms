"""
PS  : to calculate the number of bit strings of length n
 
"""
import math
def calculate_bit_strings(n):
    MOD = 1000000007
    """
    The below approach works as 
    """
    answer = 1
    for i in range(1, n+1):
        answer *= 2
        answer %= MOD
    return answer

if __name__ == "__main__":
    number = int(input())
    print(calculate_bit_strings(number))
