from typing import List

def largest_container(heights: List[int]) -> int:
    max_water = 0
    left, right = 0, len(heights) - 1
    while (left < right):
        # calculate the water contained between the
        # current pair od lines
        water = min(heights[i], heights[j]) * (right-left)
        max_water = max(max_water, water)

        # move the pointer inwards
        # move the pointer at the shorter line
        # move both pointer if they have same height
        if (heights[left]<heights[right]):
            left += 1
        elif (heights[left]>heights[right]):
            right -= 1
        else:
            left += 1
            right -= 1
    return max_water  
"""
    Complexity Analysis:
        Time Complexity: O(n) -> perform n interations using two pointer approach
        Space Complexity: O(1) -> allocated constant number of variables

"""

""" 
    Test Cases:
        1. an empty array
        2. an array with just one element
        3. an array with no containers that can contain water
        4. an array with strictly increasing heights
        5. an array with strictly decreasing heights


"""