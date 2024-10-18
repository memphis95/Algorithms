class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):
        # code here
        """
        """
        for i in range(n - 1):
            for j in range(0, n - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


Solution().bubbleSort([4, 1, 3, 9, 7], 5)
