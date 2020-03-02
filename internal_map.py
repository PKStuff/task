def square(num):
    return num*num


def map1(function, my_list):
    result = []
    for i in my_list:
        result.append(function(i))
    return result

list1 = [1,2,3,4,5,6]
a = map1(square, list1)

print(a)
