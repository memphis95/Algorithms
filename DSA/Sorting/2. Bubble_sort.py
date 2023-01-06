def BubbleSort(arr):
    for i in range(len(arr)):
        print("THis pass is :", i+1)
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        print("array after every pass: ", arr)

    print("sorted array is: ", arr)

def OptimisedBubbleSort(arr):
    for i in range(len(arr)-1):
        print("this pass is: ", i)
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        print("array after pass completion: ", arr)
    print(arr)
if __name__ == "__main__":
    arr = [12,4,9,5,3]
    OptimisedBubbleSort(arr)