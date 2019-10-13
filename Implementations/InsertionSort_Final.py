#Insertion Sort implementation

def InsertionSort(arr):
    for outside_num in range(1, len(arr)):
        if arr[outside_num] < arr[outside_num - 1]:
            #sorting the inner group of numbers
            inside_num = outside_num
            while inside_num > 0 and arr[inside_num] < arr[inside_num - 1]:
                #swap the 2 numbers
                arr[inside_num], arr[inside_num - 1] = arr[inside_num - 1], arr[inside_num]
                #incrementing the loop
                inside_num-=1
    return arr


testCase1 = [4, 5, 1, 50]
print(InsertionSort(testCase1))

testCase2= [10,2,44,13,19]