def print1toN(n):
    if n == 0:
        return
    print1toN(n-1)
    print(n)
    
    
print1toN(3)

"""
Time Complexity: O(N)

Auxiliary Space: O(N)


Explaination of above code:

Function Definition:
def print1toN(n): defines a Python function named print1toN that takes an integer n as an argument. This function aims to print numbers from 1 to n.

Base Case:
if n == 0: checks if n equals 0. This is the stopping condition for the recursion. When n reaches 0, the function stops further recursive calls.

Recursive Call:
print1toN(n - 1) invokes the print1toN function again with the argument n - 1. This recursively reduces the value of n until it reaches 0, adhering to the base case.

Printing Numbers:
print(n, end=" ") prints the current value of n after the recursive call returns. This ensures that the numbers are printed in ascending order from 1 to n.
Execution:
When print1toN(3) is called:
n is initially 3.
It recursively calls print1toN(2), print1toN(1), and print1toN(0).
After reaching print1toN(0), it starts printing values: 1 2 3.

"""