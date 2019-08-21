# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!






def show_excitement():
    # Your code goes here!
    #Creating an empty list that will be used to store the string required
    myList=[]

    for item in range(5):
    #Adding the string onto the empty list
        myList.append("I am super excited for this course! ")

   #converting the values in the list into a string only and returning it to the user
    return "".join(myList)



print(show_excitement())
