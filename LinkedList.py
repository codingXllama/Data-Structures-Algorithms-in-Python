"""
steps: 
1. Create ndoes
2. Create a linked list
3. Add nodes to the linked list
4. Print linked list

"""


class Node:
    # initializing the class
    def _init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # creating the insert method, which takes the newNode to be inserted
    # checking if the head node is empty, if it's then we will make the newNode to become the HeadNode

    """Outcome
    head=>john
    john=>None
    
    """

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            """this is not good becuase we are only pointing the head node to the next node and not the
            # nodes in between. Suppose you already have 3 nodes and you want to insert a 4th node,
            # well with this statement you will only have the head node pointing to the last node and
              forgetting to point to the 2nd and 3rd node in between
            """

            #  head=> john->Ben->None
            # self.head.next = newNode

            # traversing through all the nodes in the list
            lastNode = self.head
            while True:
                # this indicates that we are at the last node of the list
                if lastNode.next is None:
                    break
                lastNode = lastNode.next

            # breaking the nodes by making the nextNode to be pointing at the next node
            lastNode.next = newNode

    def printList(self):
        # Head=>John->Ben->Mathew->None
        currentNode = self.head
        while True:
            # this means that we are the end of the LinkedList
            if currentNode is None:
                break
            # printing data at the head node
            print(currentNode.data)
            # we move the next node and print it's data and so on, until the currentNode is None
            currentNode = currentNode.next


"""
Each node has 2 fields. 1.Data field and 2.Next/pointer/refrence field
"""

"""
firstNode values
# firstNode.data => John
# firstNode.next=> None
"""
firstNode = Node("John")


"""
Adding nodes to our linked list, but before we can do that we must create an object of our LinkedList class
"""

# we don't pass anything into our LinkedList, because it's empty
# We have to ensure that since our LinkList is Empty, that the Head(first element in linklist) is None.
# We can achieve this step by creating an init method inside the LinkedList class
# Inside the init method we will assign the Head to None, becuase it does not contain any data
myLinkedListObject = LinkedList()


# inserting a node to our LinkedList, so we must have an insert method for our linked list class

myLinkedListObject.insert(firstNode)


# Creating 2nd LinkedList
secondNode = Node("Ben")
myLinkedListObject.insert(secondNode)

thirdNode = Node("Matheew")
myLinkedListObject.insert(thirdNode)

# printing the list
myLinkedListObject.printList()
