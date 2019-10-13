
def InsertionSort(arr):
    for x in range(1, len(arr) - 1):
        y = x
        print("when x is: {} the arr is {} ".format(x,arr))

        # comparing the inner values
        while y > 0 and arr[y]<arr[y-1]:
            print("when x is: {}, y is {} and the unchanged arr is {}".format(x,y,arr))
            arr[y - 1], arr[y] = arr[y], arr[y - 1]
            print("when x is: {}, y is {} and the changed arr is {}".format(x,y,arr))
            y -= 1
            
    return arr

myList = [6, 1, 8, 4, 10]
x=InsertionSort(myList)
print(x)