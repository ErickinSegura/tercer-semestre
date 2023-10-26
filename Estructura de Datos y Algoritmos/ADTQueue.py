class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front ==  None
    
    def enqueue(self, data):
        temp = Node(data)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None


if __name__ == "__main__":
    q = Queue()
    q.enqueue(95)
    q.enqueue(97)
    q.enqueue(87)
    q.enqueue(93)
    q.enqueue(91)
    q.enqueue(100)
    q.dequeue()
    q.dequeue()

    print("Front: "+ str(q.front.value if q.front != None else -1))
    print("Rear: "+ str(q.rear.value if q.rear != None else -1))
    


