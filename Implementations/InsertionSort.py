# Algorithm Complexity : O(n^2)
# This algorithm check a keyValue which is index+1 with previous index item. If it's greater than swap else move the index+1


def InsertionSort(arr):
    key_Index = 0
    for key_Index in range(key_Index, len(arr)):
        if arr[key_Index] < arr[key_Index - 1]:
            arr[key_Index], arr[key_Index - 1] = arr[key_Index - 1], arr[key_Index]
        print(arr)


myList = [6, 1, 8, 4, 10]
InsertionSort(myList)
