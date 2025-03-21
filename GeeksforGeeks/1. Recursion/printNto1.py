def printNto1(n):
    if n <= 0:
        return
    print(n)
    printNto1(n-1)
    
    
printNto1(3)

"""
Time Complexity: O(N)

Auxiliary Space: O(N)

Explaination of this code:

Function Definition:
def printNto1(n): defines a Python function named printNto1 that takes an integer n as an argument. This function aims to print numbers from n down to 1.
Base Case:
if n <= 0: checks if n is less than or equal to 0. This is the stopping condition for the recursion. When n is 0 or negative, the function stops further recursive calls.
Printing the Value:
print(n) prints the current value of n.
Recursive Call:
printNto1(n - 1) invokes the printNto1 function again with the argument n - 1. This recursively reduces the value of n until it reaches 0, adhering to the base case.
Execution:
When printNto1(3) is called:
n is initially 3.
The function prints 3, then calls printNto1(2).
n is now 2.
The function prints 2, then calls printNto1(1).
n is now 1.
The function prints 1, then calls printNto1(0).
n is now 0, so the function returns and stops further recursion.

"""