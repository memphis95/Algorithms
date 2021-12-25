"""
solution 1: iterative approach
1. for 0 to middle elements of the array
    i. replace the starting index element with ending index element



"""
def sol1(arr):
    for i in range(len(arr)//2+1):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    
    print(arr)

# solution 2: iterative approach
def sol2(arr):
    start = 0
    end = len(arr)-1
    while start < end :
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    print(arr)



if __name__ == "__main__":
    # print("hello world")
    arr = [1,2,3,4,5]
    sol1(arr)
    sol2(arr)
    