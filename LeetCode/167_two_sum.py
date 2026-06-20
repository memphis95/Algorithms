def twoSum(self, numbers: List[int], target: int) -> List[int]:
    """
    Given an array of integers sorted in ascending order aAd a 
    target value, 
    return the index~s of any pair of numbers in the array that 
    sum to the tar-get. The order of the indexes 
    In the result doesn't matter. 
    If no pair is found, return an empty array.
    """
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total < target:
                # if sum is smaller, increment the left pointer
                left += 1
            elif total > target:
                # if sum is greater, decrement the right pointer
                right -= 1
            else:
                # if the pair is found, return its indexes
                return [left+1, right+1]
        return []