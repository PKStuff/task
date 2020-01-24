from linked_list import LinkedList
class Stack(object):

    def __init__(self):
        self.top = None
        self.node = LinkedList()
    
    def push(self, data):
        self.node.create(data)
    
    def pop(self):
        return self.node.delete_at_first()
    
    def top_data(self):
        if self.node.head:
            return self.node.head.data
        else:
            return -1

if __name__ == '__main__':
    st1 = Stack()
    st1.push(2)
    print(st1.top_data())
    print(st1.pop())
    print(st1.top_data())
      