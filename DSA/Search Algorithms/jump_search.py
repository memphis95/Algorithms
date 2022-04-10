import math


def jump_search(arr, ele, n):
    print("inside function")
    step = int(math.sqrt(n))
    prev =0
    print("intial value of : ",step)
    # finding the indexes of subarray which might contains the
    # element
    while(arr[step]< ele):
        print(prev, step, arr[step])
        prev = step
        step += int(math.sqrt(n))
        print("after update: ")
        print(prev, step, arr[step])
    # linear search in the selected sub array
    for i in range(prev, step+1):
        if arr[i] == ele:
            return i
    # when element is not present in the sub array
    return -1

if __name__ == "__main__":
    arr = [2,3,4,10,12,24,35,45,50,55]
    ele = 24
    print("index of the element is :",jump_search(arr, ele, len(arr)-1))

