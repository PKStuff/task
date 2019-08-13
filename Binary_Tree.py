class node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def inorder(t):
    if (t==None):
        return
    inorder(t.left)
    print(str(t.data)+"->",end="")
    inorder(t.right)

def preorder(t):
    if (t==None):
        return
    print(str(t.data)+"->",end="")
    preorder(t.left)
    preorder(t.right)

def postorder(t):
    if t==None:
        return
    postorder(t.left)
    postorder(t.right)
    print(str(t.data)+"->",end="")

def level_order(t):

    q = []
    q.append(t)

    while(len(q)!=0):
        temp = q.pop(0)
        print(str(temp.data)+"->",end="")
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

def search(t,data):
    q = []
    q.append(t)
    flag = False
    while(len(q)!=0):
        temp = q.pop(0)
        if temp.data == data:
            flag=True
            break
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if flag:
        return temp

def insert(t,data):
    if t!=None:
        q = []
        q.append(t)
        new_node = node(data)

        while(len(q)!=0):
            temp = q.pop(0)
            if temp.left == None:
                temp.left = new_node
                break
            elif temp.right == None:
                temp.right = new_node
                break
            elif temp.left:
                q.append(temp.left)
            elif temp.right:
                q.append(temp.right)

def parent_of_last_node(t):

    q = []
    stack = []
    q.append(t)

    while(len(q)!=0):
        temp = q.pop(0)
        if temp.left or temp.right:
            stack.append(temp)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    return stack[-1]

def delete(t,data):

    end_node = parent_of_last_node(t)
    delete_node = search(t,data)
    if end_node.right:
        temp = end_node.right
        delete_node.data = temp.data
        end_node.right = None
        del temp
    else:
        temp = end_node.left
        end_node.left = None
        del temp

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
insert(root,8)
insert(root,9)
print("\nIn-Order Traversal.")
inorder(root)
print("\nPre-Order Traversal.")
preorder(root)
print("\nPost-Order Traversal.")
postorder(root)
print("\nLevel-Order Traversal.")
level_order(root)

print("In-Order Without Recursion:")
delete(root,2)
print("After Deletion:")
level_order(root)


'''
OUTPUT:
In-Order Traversal.
8->4->9->2->5->1->6->3->7->
Pre-Order Traversal.
1->2->4->8->9->5->3->6->7->
Post-Order Traversal.
8->9->4->5->2->6->7->3->1->
Level-Order Traversal.
1->2->3->4->5->6->7->8->9->
After Deletion:
1->9->3->4->5->6->7->8->
'''
