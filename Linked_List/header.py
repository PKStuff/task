class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist(object):

    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node

    def delete_first(self):
        
        if self.head.next == None:
            temp = self.head
            self.head = None
            del temp
            return
        else:
            temp = self.head
            self.head = temp.next
            del temp
    
    def delete_last(self):

        if self.head.next == None:
            self.delete_first()
        else:
            temp = self.head
            while(temp.next.next != None):
                temp = temp.next
            temp1 = temp.next
            temp.next = None
            del temp1
    
    def last_element(self):
        if self.head.next == None:
            return self.head.data
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            return temp.data

    def display(self):
        if self.head != None:
            temp = self.head
            while(temp.next != None):
                print(str(temp.data)+"->",end="")
                temp = temp.next
            print(temp.data)
        else:
            print("Empty Linked List.")
        
    def reverse(self):
        if self.head != None:
            a = None
            b = self.head
            c = b.next

            while(b.next!=None):
                b.next = a
                a = b
                b = c
                c = c.next
            b.next = a
            self.head = b
        else:
            print("Empty Linked List.")