# Selection sort implementation
# Algorithm complexity: O(n^2)


def SelectionSort(arr):
    spot_Marker = 0
    iteration_Number = 1
    while spot_Marker < len(arr):
        for index in range(spot_Marker, len(arr)):
            if arr[spot_Marker] > arr[index]:

                arr[spot_Marker], arr[index] = arr[index], arr[spot_Marker]
        spot_Marker += 1
        print('Iteration number', iteration_Number, ':', arr)
        iteration_Number += 1


    # Input and output example
    # input : 6 8 1 4 10 7 8 9 3 2 5
    # ouput: 1 2 3 4 5 6 7 8 8 9 10
'''
input : input : 6 8 1 4 10 7 8 9 3 2 5



'''
myList = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
SelectionSort(myList)
