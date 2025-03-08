class Solution:
    def removeDuplicates(self, arr):
        # code here
        indexArray = [j for j in range(101)]
        solArr = []
        print(indexArray)
        i = 0
        while i < len(arr):
            if indexArray[arr[i]] != 1:
                solArr.append(arr[i])
                indexArray[arr[i]] = 1
            else:
                pass
            print("current array is: ", solArr)
            i += 1


Solution().removeDuplicates([2, 3, 3, 7, 5, 2])
