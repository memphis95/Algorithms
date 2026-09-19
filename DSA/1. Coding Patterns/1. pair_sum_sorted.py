from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums)-1 
    # if sum is smaller, increment the left pointer
    # if sum is larger, increment the right pointer
    if sum < target:
        left += 1
    elif sum > target:
        right -= 1
    # if the sum == target, return the pair
    else:
        return [left, right]
    """
        Complexity Analysis
            Time Complexity  : O(n) n iterations using two-pointer technique in the worst case
            Space Complexity : O(1) allocated a constant number of variables
    """

    return []

"""
        Test Cases
    1. an empty array []
    2. an array with just one element [1]
    3. an array with two element that sums to the target [a,b]
    4. an array with two elements that doesn't contain a pair that sum to target [a, b]
    5. an array with duplicate values
    6. an array with negative value, and includes in the target
    7. an array with negative values, and both the values of pair includes in the target

"""