class Solution:
    """
    Given an integer array nums and an integer k, 
    return true if there are two distinct indices i and j in the array 
    such that nums[i] == nums[j] and abs(i - j) <= k.
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # solution 1 : Time Limit Exceeded
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] == nums[j]) and (abs(i-j)<= k): 
        #             return True
        # return False
        """
        time complexity - O(n^2)
        """
        
#         solution 2 : Time Limit Exceeded
        # for i in range(len(nums)-1):
        #     for j in range(1,k+1):
        #         # print(i,j)
        #         if (i+j<= len(nums)-1) and (nums[i] == nums[i+j]):
        #             return True
        # return False
        """
        time complexity - O(nk)
        """
        
        if not nums:
            return False
        elif len(nums) == 1:
            return False
        elif len(nums) == 2:
            if nums[0] != nums[1]:
                return False
            elif nums[0] == nums[1] and k >= 1:
                return True
            else:
                return False
        else:
            index_dict = {}
            for i in range(len(nums)):
                if nums[i] in index_dict:
                    prev_index = index_dict[nums[i]]
                    if i - prev_index <= k:
                        return True
                index_dict[nums[i]] = i
            return False
        """
        time complexity - O(n)
        auxillary space - O(n)
        """
                
        