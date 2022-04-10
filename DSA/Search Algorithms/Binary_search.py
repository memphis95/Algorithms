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


if __name__ == "__main__":
    arr = [2,3,4,10,12,24,35,45,50,55]
    ele = 45
    print(binary_search(arr, 0, len(arr)-1, ele))