
'''Inserting john, ben, mathew in linkedlist'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # initial node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        currentNode = self.head

        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    

firstNode = Node("john")
linkedList = LinkedList()
linkedList.insert(firstNode)

secondNode = Node("ben")
linkedList.insert(secondNode)

thirdNode = Node("mathew")
linkedList.insert(thirdNode)

linkedList.printList()



