class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.link = None

class LinkedList(object):
    
    def __init__(self, user_id):
        self.head = None
        self.user_id = user_id
    
    def insert(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_last(self, data):
        if self.head == None:
            self.insert(data)
            return

        temp_node = self.head
        new_node = Node(data)
        while temp_node.next != None:
            temp_node = temp_node.next
        temp_node.next = new_node
    
    def delete_node(self, id):
        if self.head.data['id'] == id and self.head.next == None:
            self.head = None
            return 1
        else:
            if self.head.data['id']== id and self.head.next != None:
                temp_node = self.head.next
                self.head = temp_node
                return 1
            prev_node = self.head
            temp_node = self.head.next
            while temp_node!=None:
                if temp_node.data['id'] == id and temp_node.next == None:
                    prev_node.next = None
                    return 1
                elif temp_node.data['id'] == id and temp_node.next:
                    prev_node.next = temp_node.next
                    return 1
                temp_node = temp_node.next
                prev_node = prev_node.next
        return -1
    
    def display(self):
        temp_node = self.head
        total_amount = 0
        total_discount = 0
        print("User {} bill is following:".format(self.user_id))
        while temp_node != None:
            print(temp_node.data)
            if temp_node.data:
                total_amount+=temp_node.data['Total']
                total_discount+=(temp_node.data['Total'] - (temp_node.data['Quantity']*temp_node.data['price']))
            temp_node = temp_node.next
        print()
        print("Total Amount is:{}".format(total_amount))
        print("Total Discount is: %1.2f"%total_discount)
