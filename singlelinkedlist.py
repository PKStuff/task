class Node:
	
	def __init__(self, data):
		
		self.data = data
		self.next = None

class LinkedList:
	
	head = None
	
	def insert_first(self, data):
		
		new_node = Node(data)
		
		if self.head == None:
			
			self.head = new_node
			return
		
		else:
			new_node.next = self.head
			self.head = new_node
	
	def insert_last(self, data):
		
		new_node = Node(data)
		if self.head == None:
			
			self.insert_first(data)
		
		else:
			
			temp = self.head
			while(temp.next != None):
				temp = temp.next
			temp.next = new_node
	
	def delete_last(self):
		
		temp = self.head
		while(temp.next.next != None):
			temp = temp.next
		
		temp1 = temp.next
		temp.next = None
		del(temp1)
	
	def delete_first(self):
		
		if self.head == None:
			print("List is Empty")
			return
		elif self.head.next == None:
			
			self.head = None
		else:
		
			temp = self.head;
			self.head = temp.next
			del(temp)
	def length(self):
		temp = self.head
		leng = 0
		while(temp.next != None):
			leng+=1
			temp=temp.next
		return leng+1
			
	def reverse(self):
		if self.head == None or self.head.next == None:
			print("List is empty or list has only one element")
			return
		elif self.length() == 2:
			a = self.head
			b = a.next
			
			b.next = a
			a.next = None
			
			self.head = b
			
		else:
			
			a = self.head
			b = a.next
			c = b.next
			a.next = None
			
			while(b.next != None):
				
				b.next=a
				a=b
				b=c
				c=c.next
			b.next=a
			
			self.head = b
	def display(self):
		
		temp = self.head
		
		while(temp.next != None):
			print(temp.data)
			temp = temp.next
		print(temp.data)

if __name__ == '__main__':
	
	ls = LinkedList()
	
	ls.insert_first(1)
	ls.insert_first(3)
	ls.insert_first(4)
	ls.insert_last(5)
	ls.insert_last(6)
	ls.insert_first(7)
	ls.insert_first(8)
	ls.delete_last()
	ls.delete_first()
	#ls.reverse()
	
	ls.display()
	ls.reverse()
	print("after")
	ls.display()
	
