""" max heapify code """

def max_heapify(Arr, n, i):
    largest =i
    left = 2*i + 1
    right = 2*i + 2
    
    # when left child node is greater than the root node
    if(left<n and Arr[largest]<Arr[left]):
        largest = left
    if(right<n and Arr[largest]<Arr[right]):
        largest = right
    if largest != i:
        Arr[i], Arr[largest] = Arr[largest], Arr[i]
        print("Array before recursive call :", Arr)
        max_heapify(Arr, n, largest) 

# driver code 
Arr = [2, 66, 30, 5, 9, 10]
n = len(Arr)

for i in range(n//2 -1, -1, -1):
    print("executing for loop :", i)
    max_heapify(Arr, n, i)

print("Max Heap is :")
for i in range(n):
    print(Arr[i])