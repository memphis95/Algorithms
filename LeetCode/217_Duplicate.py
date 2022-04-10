class Solution:
    """
    Given an integer array nums, return true if any 
    value appears at least twice in the array,
     and return false if every element is distinct.
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        # solution 1
#         nums.sort()
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
#         return False
    
    
        # solution 2
            
#         dict1 = {}
#         for i in range(len(nums)):
#             if nums[i] not in dict1:
#                 dict1[nums[i]] = 1
#             else:
#                 dict1[nums[i]] += 1
#         for key, value in dict1.items():
#             if value > 1:
#                 return True
            
#         return False

    # solution 3
        return len(nums)> len(set(nums))