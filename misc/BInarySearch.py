'''
Implementing a binary search Algorithm
Credits go to Grokking Algorithms.
This code is used for learning purposes!
'''

#passing the 2 arguments for the binarySearch method
#there aruguments include 1.The sorted list 2.The Token/Number we will be looking for in the sorted list
#this method will return the index of the Token we are looking for, if it doesn't exist then we return None
def binarySearch(sortedList, NumberToGues):
    #keeping track of which part of the list we will search in
    lowValue = 0
    highValue = len(list) - 1

    #while we still have not found the element
    while lowValue <= highValue:
        #checking the middle element
        midValue = (lowValue + highValue)
        guessValue = list[midValue]
        #if we have found the Number we need to Guess
        if guessValue == NumberToGues:
            return midValue

        #if our guessValue is too high
        if guessValue > NumberToGues:
            #we will reduce our highValue(upper bound) by subtracting 1 from the midValue
            highValue = midValue - 1

        #the guess was too low
        else:
            lowValue = midValue + 1
    #if the NumberToGues we want to search for does NOT exist in the list
    return None


#Sample list
myList = [1, 3, 5, 7, 9]
print(binarySearch(myList, 3))
