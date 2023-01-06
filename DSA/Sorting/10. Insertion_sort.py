def InsertionSort(arr):
    # iterating over the length of array
    #  sorted - arr[0]
    #  unsorted - arr[1:len(arr)]
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        print('iteration no: ', i)
        while j>=0 and key < arr[j]:
            # moving values of array to the right
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)
        print("value of j: ",j)
    print(arr)


if __name__ == "__main__":
    arr = [12,4,9,5,3]
    InsertionSort(arr)