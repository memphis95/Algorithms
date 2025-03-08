class Solution:
    def bruteForceSolution(arr):
        for i in range(len(arr)):
            count = 1
            for j in range(i + 1, len(arr)):
                if arr[j] == arr[i]:
                    count += 1
            print(arr[i], count)
            if count % 2 == 1:
                return arr[i]


Solution.bruteForceSolution([1, 1, 2, 2, 2])
