class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None
        self.top = None
        self.limit = 0
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    
    def isFull(self):
        if self.limit > 10:
            return True
        else:
            return False
    
    def Top(self):
        return self.top.data
    
    def push(self, data):
        new_node = Node(data)
        if not self.isFull():
            if self.head == None:
                self.head = new_node
                self.top = self.head
                self.limit+=1
            else:
                self.top.next = new_node
                self.top = self.top.next
                self.limit+=1
        else:
            print("Overflow!!!!!")
    
    def pop(self):
        if not self.isEmpty():
            temp = self.head
            if temp.next != None:
                while(temp.next!=self.top):
                    temp = temp.next
                data = self.top.data
                temp1 = self.top
                self.top = temp
                temp.next = None
                del temp1
                return data
            else:
                temp1 = self.head
                data = temp1.data
                self.top = None
                self.head = None
                del temp1
                return data
        else:
            return 'Overflow!!!'

    def display(self):
        temp = self.head
        if not self.isEmpty():
            while(temp!=self.top):
                print(str(temp.data)+"->",end="")
                temp = temp.next
            print(temp.data)
        else:
            print("Empty Stack!!!")
    