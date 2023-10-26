class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self,data):
        newNode = StackNode(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.head is None:
            return
        
        self.head = self.head.next

    def top(self):
        if self.isEmpty():
            return
        
        currentNode = self.head
        print(currentNode.value)

    def printStack(self):
        if self.isEmpty():
            return
        
        currentNode = self.head
        print("Stack Values:")
        while(currentNode):
            print(currentNode.value)
            currentNode = currentNode.next

if __name__ == "__main__":
    St = Stack()
    print(St.isEmpty())
    St.push(1)
    St.push(2)
    St.push(3)
    St.push(4)
    St.push(5)
    print(St.isEmpty())
    St.top()
    St.printStack()
    St.pop()
    St.printStack()



