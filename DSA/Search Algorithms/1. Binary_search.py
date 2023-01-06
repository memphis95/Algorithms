def binary_search(arr, low, high, ele):
    if low <= high:
        mid = low + (high-low)//2
       
        if (arr[mid] == ele):
            return mid
        elif (arr[mid] > ele):
            
            return binary_search(arr, low, mid-1, ele)
        else:
           
            return binary_search(arr, mid+1, high, ele)
    else:
        return -1
    
def binary_search2(arr, n, ele):
    low = 0
    high = n-1

    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == ele:
            return mid
        elif arr[mid]>ele:
            high = mid - 1
        else:
            low = mid + 1
    return - 1

def binary_search_cn(array, element, debug=False):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound)//2
        if debug:
            print("lower bound :", lower_bound)
            print("upper bound: ", upper_bound)
            print("middle: ", middle)
        if element == array[middle]:
            return middle
        elif element < array[middle]: #lesser condition
            # no change in the lower bound
            upper_bound = middle - 1
        else: # greater condition
            # no change in the upper bound
            lower_bound = middle + 1
    return -1



if __name__ == "__main__":
    arr = [2,3,4,10,12,24,35,45,50,55]
    ele = 45
    # print(binary_search(arr, 0, len(arr)-1, ele))
    print(binary_search2(arr, len(arr), ele))