from calc import LinkedList

l1 = LinkedList(1)
l2 = LinkedList(2)

data = {
    'id': 1,
    'Name': 'Item1',
    'Quantity': 2,
    'price': 30,
    'discount' : 2.5,
    'Total' : 0
}

data['Total'] = (data['price'] * data['Quantity']) + (((data['price'] * data['Quantity'])*data['discount'])/100)

data1 = {
    'id': 2,
    'Name': 'Item2',
    'Quantity': 2,
    'price': 40,
    'discount' : 10.5,
    'Total' : 0
}

data1['Total'] = (data1['price'] * data1['Quantity']) + (((data1['price'] * data1['Quantity'])*data1['discount'])/100)



l1.insert_at_last(data)

l1.insert_at_last(data1)

l1.display()

print()


l2.insert_at_last(data)

l2.insert_at_last(data1)

l2.delete_node(2)

l2.display()



/* Output:

User 1 bill is following:
{'id': 1, 'Name': 'Item1', 'Quantity': 2, 'price': 30, 'discount': 2.5, 'Total': 61.5}
{'id': 2, 'Name': 'Item2', 'Quantity': 2, 'price': 40, 'discount': 10.5, 'Total': 88.4}

Total Amount is:149.9
Total Discount is: 9.90

User 2 bill is following:
{'id': 1, 'Name': 'Item1', 'Quantity': 2, 'price': 30, 'discount': 2.5, 'Total': 61.5}

Total Amount is:61.5
Total Discount is: 1.50



*/
