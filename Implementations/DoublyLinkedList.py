class DoublyLinkedList:
    def __init__(self):
        # Creating the head and tail of the DLL
        self.headNode = None
        self.tailNode= None

        # Creating the method for searching for a node
        def SearchForNode(self, targetValue):
            currentNode = self.headNode

            while currentNode!= None and currentNode != targetValue:
                currentNode = currentNode.next;
            
            return currentNode!=None