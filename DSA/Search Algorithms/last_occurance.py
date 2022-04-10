#naive solution
def last_occurance(arr, x):
    # pos = -1
    # for i in range(len(arr)):
    #     if arr[i] == x:
    #         pos = i 
    # return pos
    for i in reversed(range(len(arr))):
        if arr[i] == x :
            return i

# Efficient solution

def last_occurance_binary(arr, x):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        print(low, high, mid)
        if (arr[mid] < x ):
            low = mid +1
        elif (arr[mid] > x):
            high = mid - 1
        elif arr[mid] == x:
            if ((mid == len(arr)-1) or (arr[mid] != arr[mid+1]) ):
                return mid
            else:
                low = mid+1
    return -1

if __name__ == "__main__":
    arr = [10, 15, 20, 20, 40, 40]
    x = 40
    print(last_occurance_binary(arr,x))