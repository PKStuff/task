class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary(object):

    def create_tree(self):
        root = Node(1)

        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        return root

    def insert(self, root, data):
        temp_node = Node(data)
        if root == None:
            root = temp_node
            return
        else:
            Queue = []
            Queue.append(root)
            flag = True
            while Queue:
                t = Queue[0]
                Queue.pop(0)
                if not t.left:
                    t.left = temp_node
                    break
                else:
                    Queue.append(t.left)

                if not t.right:
                    t.right = temp_node
                    break
                else:
                    Queue.append(t.right)
        return root

    def level_order(self, root):
        print("\nLevel Order Traversal..")
        Queue = []
        if root == None:
            print("Tree is Empty....")
        else:
            Queue.append(root)
            while(Queue):
                temp_node = Queue[0]
                if temp_node.left != None:
                    Queue.append(temp_node.left)
                if temp_node.right != None:
                    Queue.append(temp_node.right)
                print(temp_node.data, end="->")
                Queue.pop(0)

    def pre_order(self, t):
        if t:
            print(t.data, end="->")
            self.pre_order(t.left)
            self.pre_order(t.right)

    def inorder(self, t):
        if t:
            self.inorder(t.left)
            print(t.data, end="->")
            self.inorder(t.right)

    def postorder(self, t):
        if t:
            self.postorder(t.left)
            self.postorder(t.right)
            print(t.data, end="->")

if __name__ == '__main__':
    """
    Binary Tree Example
    """
    b1 = Binary()
    root = b1.create_tree()
    b1.level_order(root)
    print("\nPreOrder Traversal..")
    b1.pre_order(root)
    print("\nInOrder Traversal..")
    b1.inorder(root)
    print("\nPostOrder Traversal..")
    b1.postorder(root)
    root = b1.insert(root, 8)
    b1.level_order(root)
    print()
