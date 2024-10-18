class Solution: 
    def select(self, arr, i):
        # code here
        min_ele = arr[i]
        min_ele_index = i
        for j in range(i, len(arr)):
            if min_ele > arr[j]:
                min_ele = arr[j]
                min_ele_index = j
        return min_ele_index
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min_ele_index = self.select(arr, i)
            arr[i], arr[min_ele_index] = arr[min_ele_index], arr[i]
            print("array after cbanging array: ",arr)
            
            
            
Solution().selectionSort([4, 1, 3, 9, 7], 5)