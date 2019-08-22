# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
# %%


# %%
# Bubble sort implementation


def bubbleSort(arr):

    swap_happened = True

    while swap_happened:
        print("Bubble sort status: "+str(arr))
        swap_happened = False

        for item in range(len(arr)-1):
            if(arr[item] > arr[item+1]):
                arr[item], arr[item+1] = arr[item+1], arr[item]
                swap_happened = True


myList = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubbleSort(myList)


# %%


# %%


# %%
print("hi")


# %%


# %%
