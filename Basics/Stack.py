# Stack Implementation


class Stack:
    def __init__(self):
        self.myStack = []

    def push(self, val):
        return self.myStack.append(val)

    def pop(self):
        return self.myStack.pop()

    def view(self):
        return self.myStack

    def isEmpty(self):
        return self.myStack == []


# Creating a method to check if  a pren is matched or not

"""'
[(]
"""


def CheckParen(arr):

    parens = []
    # Edge cases
    if len(arr) % 2 != 0:
        return "Not Balanced"
    else:
        for index in range(len(arr)):
            if arr[index] == "[" or arr[index] == "(" or arr[index] == "{":
                parens.append(arr[index])
    return parens


# # Creating a stack object
# stack1 = Stack()
# stack1.push(10)
# print(stack1.view())

myArr = ["[({})]"]
print(CheckParen(myArr))
