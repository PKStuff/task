class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	
	head = None
	
	def push(self, data):
		
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			return
		else:
			
			temp = self.head
			while(temp.next != None):
				temp = temp.next
			
			temp.next = new_node
			
	def pop(self):
		
		if self.head == None:
			print("UnderFlow.")
			return
		else:
			temp = self.head
			self.head = temp.next
			item = temp.data
			del(temp)
			return item
	
	def top(self):
		
		if self.head == None:
			print("UnderFlow:")
			return
		else:
			
			return(self.head.data)
			
	def display(self):
		temp = self.head
		while(temp.next != None):
			print(temp.data,end="->")
			temp = temp.next
		print(temp.data)

if __name__ == '__main__':
	
	st = Stack()
	st.push(1)
	st.push(2)
	st.push(3)
	st.push(4)
	
	print("After Insert:")
	st.display()
	print("Deleted item is:"+str(st.pop()))
	
	print("After Delete:")
	st.display()
	print("Top item is:"+str(st.top()))
			
			
'''
o/p:

After Insert:                                                                                                                  
1->2->3->4                                                                                                                     
Deleted item is:1                                                                                                              
After Delete:                                                                                                                  
2->3->4                                                                                                                        
Top item is:2  

'''
