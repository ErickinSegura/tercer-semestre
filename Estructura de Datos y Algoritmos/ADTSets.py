class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Sets:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.itsEmpty():
            self.head = Node(data)
            return
        current_node=self.head
        while current_node.next:
            if current_node.value == data or current_node.next.value == data:
                return False
            current_node=current_node.next
        current_node.next=Node(data)


    def remove(self,data):
        if self.itsEmpty():
            return
        
        currentNode = self.head
        if currentNode.value == data:
            self.head = currentNode.next
            return
        
        while(currentNode.next):
            if currentNode.next.value == data:
                currentNode.next = currentNode.next.next
                return
            else:
                currentNode = currentNode.next
        return False
                

    def itsEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def contains(self, data):
        if self.itsEmpty():
            return
        
        currentNode = self.head
        if currentNode.value == data:
            return True
        
        while(currentNode.next):
            if currentNode.next.value == data:
                return True
            else:
                currentNode = currentNode.next
        return False
        

    def size(self):
        if self.itsEmpty():
            return 0
        
        currentNode = self.head
        count = 1
        while(currentNode.next):
            count += 1
            currentNode = currentNode.next
        print(f"Size:{count}")

    def printSet(self):
        if self.itsEmpty():
            return
        
        
        currentNode = self.head
        print("Set Values:")
        while(currentNode):
            print(currentNode.value)
            currentNode = currentNode.next

    def Union(self, set2):
        
        if self.itsEmpty() or set2.itsEmpty():
            return
        
        currentNode = set2.head
        while(currentNode):
            St.add(currentNode.value)
            currentNode = currentNode.next

    def Substract(self, set2):
        if self.itsEmpty() or set2.itsEmpty():
            return
        
        currentNode = set2.head
        while(currentNode):
            if self.contains(currentNode.value):
                self.remove(currentNode.value)
            currentNode = currentNode.next

    def Intersect(self, set2):
        if self.itsEmpty() or set2.itsEmpty():
            return
        Inter = Sets()
        currentNode = set2.head
        while(currentNode):
            if self.contains(currentNode.value):
                Inter.add(currentNode.value)
            currentNode = currentNode.next
        Inter.printSet()
            
        


if __name__ == "__main__":
    St = Sets()
    St2 = Sets()
    St.add(97)
    St.add(95)
    St2.add(1)
    St2.add(2)
    St2.add(97)
    St.Union(St2)
    St.printSet()

    St.Intersect(St2)
    St.Substract(St2)

    St.printSet()
    