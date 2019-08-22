# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
# %% [markdown]
# # Bubble sort
# Algorithm complexity : O(n^2), where n, is the number of items to itter through and sort
#
# ## Example
# Sort the following list: 6,8,1,4,10,7,8,9,3,2,5
# ## Solution
# Start iteration 0: 6,8,1,4,10,7,8,9,3,2,5
#
# After iteration 1: 6,1,4,8,7,8,9,3,2,5,10
# After iteration 2: 1,4,6,7,8,8,3,2,5,9,10
# Sorted list :      1,2,3,4,5,6,7,8,8,9,10

# %%


# Bubble Sort Implementation

def BubbleSort(arr):
    # Comparing the first [0th index] with the second[1th index] element
    # print(myList[0] > myList[1])

    # Going through all the elements in the array -1, the reason we do -1
    # because we cannot compare the last element '5' with any element ahead of it, since it's the last element in the list

    # for num in range(len(arr)-1):
    #     print(arr[num], arr[num+1])

    print(arr[0], arr[1])
    arr[0], arr[1] = arr[1], arr[0]
    print(arr)


myList = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
BubbleSort(myList)
