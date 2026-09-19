from typing import List


def triplet_sum_brute_force(nums: List[int]) -> List[List[int]]:
    n = len(nums)

    # using hashset to ensure no duplicate triplets
    triplets = set()
    # interates through the indexes of all triplets
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    # sort the triplet before including it in the hash set
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(triplet)
    return [list(triplet) for triplet in triplets]

    """
        Complexity Analysis
            Time Complexity : O(n3)
    """