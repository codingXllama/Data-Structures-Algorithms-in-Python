"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counterIndex = 1
        currentNode = self.head
        if position < 1:
            return None

        while currentNode and counterIndex <= position:
            # print("the position is:", position)
            if counterIndex == position:
                return currentNode
            currentNode = currentNode.next
            counterIndex += 1

        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        counterIndex = 1
        currentNode = self.head
        if position > 1:
            while currentNode and counterIndex <= position:
                if counterIndex == position - 1:
                    new_element.next = currentNode.next
                    currentNode.next = new_element
                currentNode = currentNode.next
                counterIndex += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        currentNode = self.head
        previousNode = None

        # as long as the currentNode.value (which is the value of the head node) is not equal to the value we want to remove
        # and also the currentNode we are on has a next node attached to it (referencing to a node)
        while currentNode.value != value and currentNode.next:
            previousNode = currentNode
            currentNode = currentNode.next
        #checking to see if the currentNode has a value which we are wanting to delete
        if currentNode.value == value:
            #we check if that currentNode which contains a value we want to remove is linking to a previousNode
            if previousNode:
                #pointing at the next value from the currentNode.next
                previousNode.next=currentNode.next
            else:
                #creating a previous node, my making the currentNode(self.head) point the node ahead of it
                self.head=currentNode.next




# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5=Element("hello")
# Start setting up a LinkedList
ll = LinkedList()
ll.append(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
# print(ll.get_position(3).value)

# Test insert
# ll.insert(e4, 3)
# Should print 4 now
# print(ll.get_position(3).value)

# Test delete
ll.delete(3)
# Should print 2 now
# print(ll.get_position(1).value)
# Should print 4 now
# print(ll.get_position(2).value)
# Should print 3 now
# print(ll.get_position(3).value)


