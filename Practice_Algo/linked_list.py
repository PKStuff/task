class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:

    def __init__(self):
        self.head = None
    
    def create(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            return

    def insert_at_last(self, data):
        new_node = Node(data)
        temp_node = self.head
        while temp_node.next != None:
            temp_node = temp_node.next
        temp_node.next = new_node
        return
    
    def delete_at_first(self):
        if self.head:
            temp_node = self.head
            if self.head.next == None:
                self.head = None
            else:
                self.head = self.head.next
                temp_node.next = None
            return temp_node.data
        else:
            return -1
    
    def delete_at_last(self):
        if self.head:
            temp_node = self.head
            del_node_data = None
            if self.head.next == None:
                del_node_data = self.head.data
                self.head = None
            else:
                while temp_node.next.next != None:
                    temp_node = temp_node.next
                del_node_data = temp_node.next.data
                temp_node.next = None
            return del_node_data
        else:
            return -1
    
    def display(self):
        if self.head:
            temp_node = self.head
            while temp_node.next != None:
                print(temp_node.data, end=",")
                temp_node = temp_node.next
            print(temp_node.data)
        else:
            print("List is empty...")
    
    def first(self):
        if self.head:
            return self.head.data
        else:
            return -1


if __name__ == '__main__':
    l1 = LinkedList()
    l1.create(1)
    l1.create(2)
    l1.create(3)
    print("Before Deletion:")
    l1.display()
    l1.delete_at_last()
    print("After deletion:")
    l1.display()
    print("Top is:{}".format(l1.first()))
    print("The head is:{}".format(l1.head.data))
