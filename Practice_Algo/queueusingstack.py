class Queue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []
    

    def enqueue(self, data):

        self.st2.append(data)
    
        while self.st1:
            self.st2.append(self.st1.pop())
        
        s = self.st1
        self.st1 = self.st2
        self.st2 = s
    
    def dequeue(self):
        if self.st1:
            return self.st1.pop()
        else:
            return -1


q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)

print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
