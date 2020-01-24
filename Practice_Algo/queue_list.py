from linked_list import LinkedList

class Queue(object):

    def __init__(self):
        self.l1 = LinkedList()
    
    def isempty(self):
        if self.l1.head == None:
            return True
        else:
            return False
    
    def enqueue(self, data):
        self.l1.create(data)
    
    def dequeue(self):
        return self.l1.delete_at_last()

if __name__ == '__main__':
    q1 = Queue()
    print(q1.isempty())
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)
    print(q1.dequeue())
    print(q1.dequeue())
    print(q1.dequeue())
    print(q1.dequeue())
    #print(q1.dequeue())
