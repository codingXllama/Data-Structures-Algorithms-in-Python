class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    # this method stores data into the Node of the linked list
    def append(self, data):
        new_node = Node(data)
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = new_node

    def length(self):
        currentNode = self.head
        totalNodes = 0
        while currentNode.next != None:
            totalNodes += 1
            currentNode = currentNode.next

    # figuring out the length of the linked list

