def linearSearch(arr, a, b):
    for i in range(a):
        if(arr[i] == b):
            return i
    return -1

arr = [18, 5, 13, 9, 12, 22, 7, 16]
length = len(arr)
num = 9

index = linearSearch(arr, length ,num)
if(index == -1):
    print("Given element is not present in the array.")
else:
    print("Given element is present at position:", index+1)
