# Naive solution
def find_first_index(arr, x):
    for i in range(len(arr)):
        if (arr[i] == x):
            return i
    return -1
# Efficient solution
#  based on binary search algorithm
def first_index(arr, x):
    low = 0
    high = len(arr) -1

    while low<=high:
        
        mid = (low+high)//2
        print(low, high, mid)
        if (arr[mid] > x):
            high = mid-1
        elif(arr[mid] < x):
            low = mid+1
        elif ( arr[mid-1] != x ):
            return mid
        else:
            high = mid-1
    return -1






if __name__ == "__main__":
    arr = [1,1,10,10,10,20,20,40]
    x = 0
    # print(find_first_index(arr, x))
    print(first_index(arr, x))