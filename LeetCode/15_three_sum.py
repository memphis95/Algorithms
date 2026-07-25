def threeSum(self, nums: list[int]) -> list[list[int]]:
    """
        Given an integer array nums, return all the triplets
        [nums[i], nums[j], nums[k]] such taht  i != j, and
        i != k and j != k, and nums[i] + nums[j] + nums[k] == 0.
    note :- solution set must not contain duplicate triplets.
    """
    """ BRUTE FORCE APPROACH 
        using three nested loops 
        time complexity ~ O(N^3)
    """
    """
        Optmal Appraoch:
            step 1 : sort the array in ascending order 
            step 2 : Iterate through first element 
                    Ennumerate each element as the first element
                    of a potential triplet, loop runs from index 0 to n-2
                    atleast three element for the triplet
            step 3: Early termination 
                    if nums[i] > 0, break immediately, since the array is
                    sorted, all subsequent elements will also be positive
                    impossible to find three numbers that sum to zero.
            step 4: Skip duplicates for the first element
            step 5: two-pointer search
                    for each valid nums[i], initialize two pointers
                        left pointer j = i+1 (starts right after the fixed element)
                        right pointer k  = n-1 (starts at the end of the array)
            step 6: find the valid Triplets 
                    while j < k 
                        calculcate sum = nums[i] + nums[j] + nums[k]
                        if sum < 0 -> the sum is too small, increment j to get a bigger value
                        if sum > 0 -> the sum is too large, decrement k to get a smaller value
                        if sum == 0 -> found a valid triplet 
                            add [nums[i], nums[j], nums[k]] to result

            step 7: Handle duplicates for two pointers
                    ~ increment j while j < k and nums[j] = nums[j-1]
                    ~ decrement k while j < k and nums[k] = nums[k+1]

            return result array
    """
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n-2):
        if nums[i] > 0:
            # early termination: if the smallest number is positive, no zero sum possible
            break
        # skip duplicate values for the first element to aviod duplicates triplets
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, n-1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            # current sum is too small, increase left pointer           
            if current_sum < 0:
                left += 1
            # current sum is too large, decrease right pointer
            elif current_sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # skip duplicate values
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1  
        return result

