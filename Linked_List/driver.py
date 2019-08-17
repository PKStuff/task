from header import Linkedlist

if __name__ == '__main__':

    l1 = Linkedlist()
    l1.insert(1)
    l1.insert(2)
    l1.insert(3)
    l1.insert(4)

    l1.display()
    l1.reverse()
    l1.display()
    print(l1.last_element())

    l2 = Linkedlist()
    l2.insert(6)
    l2.insert(7)
    l2.display()
    l2.delete_last()
    l2.display()
    print(l2.last_element())
    