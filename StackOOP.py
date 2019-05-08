'''
Author: CodingXllama (Osama A)
Purpose: To implement a Stack ADT
Date: May 7,2019

'''




# Creating the stack Class and initializing a list for it
class Stack_LIFO:
    def __init__(self):  # initializing the class
        self.myStack = []  # creating the class list, which is used to store all the user string values

    # This method is used for viewing all the items from the stack from top to bottom
    def view(self):  #Time complexity O(n) where n is the number of elements inside the stack
        for item in range(len(self.myStack)):
            print("item Number", item + 1, " Value:", self.myStack[item])

    # This method is used for Adding items to the stack
    def push(self):
        item = input("Please Enter a stack value: ")
        self.myStack.append(item)

    # This method is used for Removing items from the stack, Note since this is a stack then the last added value will be firstly removed (LIFO)
    def pop(self):
        item = self.myStack.pop(-1)
        print("Item popped is: ", item)

    # This method is for checking if the stack is empty or not
    def isEmpty(self):
        return self.myStack == []


# Creating an instance of our Stack Class
myFirstStack = Stack_LIFO()

# to ensure that we are still running the program
keepRunningProgram = True
while keepRunningProgram:

    print("")
    print("")
    print("Press 1 to View Stack")
    print("Press 2 to Push element from  Stack")
    print("Press 3 to Pop element from  Stack")
    print("Press 4 to check if stack is Empty")
    userOption = int(input("Enter your choice: "))  # user prompt
    print("")

    # Depending on what the user inputs we will call a specific method
    if userOption == 1:
        myFirstStack.view()
    elif userOption == 2:
        myFirstStack.push()
    elif userOption == 3:
        myFirstStack.pop()
    elif userOption == 4:
        # storing the boolean value to check if the stack is empty or not
        stackFullStatus = myFirstStack.isEmpty()

        # checking the stack condition
        if stackFullStatus:
            print("The Stack is Not Empty!")
        else:
            print("The Stack still has space")

    # if the user inputs a choice number outside of what we provided then we warn them to try again or check if they want to exit the app
    else:
        print("Please try again! ")
        userOption = int(input("Press 0 to Exit the program! "))
        if userOption == 0:
            keepRunningProgram = False  # closing the App
        else:
            keepRunningProgram = True  # Keep looping through
print("Thank you for using the program today! ")
