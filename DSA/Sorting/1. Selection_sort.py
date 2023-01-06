def SelectionSort(arr):
    # iterating the array
    for i in range(len(arr)):
        # taking the minimum value index as i
        min_index = i
        for j in range(i+1, len(arr)):
            # if jth index value is smaller than the min_index value, 
            if arr[j]<arr[min_index]:
                # replace the min_index value with j
                min_index = j
        # swapping the ith value with the min_index value of the array
        arr[min_index], arr[i] = arr[i], arr[min_index]
    print("Array after sorting: ", arr)

if __name__ == "__main__":
    arr = [12,4,9,5,3]
    SelectionSort(arr)

