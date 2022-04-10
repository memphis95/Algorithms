
# iterative approach
def interpolation_search(arr, x):
    """
    Given a sorted array of n uniformly distributed values arr[],
     write a function to search for a particular element x in the array. 
    """
    print("inside the function")
    # intialize the low and high with the start and end index of array
    low = 0
    high = len(arr)-1
    # if array is null, return empty array
    if not arr:
        print("inside if")
        return "Array is Empty"
    # if the element x lies between smallest and greatest element of the sorted array
    elif x >= arr[low] and x <= arr[high]:
        while(low <= high):
            pos = low + ((high -low)*(x-arr[low]))//(arr[high] - arr[low])
            # if element x present at probe position
            if arr[pos] == x:
                return pos
            # if the element x is less than probe position element
            elif arr[pos]<x:
                low = pos + 1
            # if the element x is greater than probe position element 
            elif arr[pos]>x:
                high = pos -1
    # if the x is not lies between the smallest and greatest element in the
    # sorted array
    else:
        return -1

# recursive approach
def interpolation_search_binary(arr, x, low, high):
    if not arr:
        return "Array is Empty"
    elif x >= low and x>= high:
        if low <= high:
            pos = low + ((high -low)*(x-arr[low]))//(arr[high] - arr[low])
            if arr[pos] == x:
                return pos
            elif arr[pos] > x:
                return interpolation_search_binary(arr, x, low, pos-1)
            elif arr[pos] < x:
                return interpolation_search_binary(arr, x, pos+1, high)
        else:
            return -1
    else:
        return -1



if __name__ == "__main__":
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    x = 18
    print(interpolation_search(arr, x))
    print(interpolation_search_binary(arr, x, 0, len(arr)-1))