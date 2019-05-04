class Node(object):
    # Initializing a new node element
    def __init__(self, value):

        self.value = value  # each Node comes with a value associated with it
        # each Node comes with a variable/pointer field which points to the "next" element in the linked list
        self.next = None


# Creating the LinkedList class


class LinkedList(object):
    """Initializing the LinkedList with it's properties
    which includes it's Head Node, which is the first element in the list.
    if we make a new linked list with out a head, then the linked list default value will be None.
    """

    def __init__(self, head=None):
        # self.head=None, because the first node(head node) is NOT pointing to another node.
        self.head = None

    # Creating a method to add elements to our LinkedList
    def append(self, new_Node):
        currentNode = self.head

        # checking if the LinkedList already has a head then we do the following:
        if self.head:
            # go through all the nodes using the "next" reference in every Node until we get to the end of the list
            while currentNode.next:
                # setting the currentNode to the next node
                currentNode = currentNode.next
            # setting the nextNode which is the end of our list to be the newNode
            currentNode.next = new_Node
        else:
            # if the head node is empty, then we assign a the New Node to it
            self.head = new_Node
