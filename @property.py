class Person(object):

    def __init__(self, age=0):
        self._age = age

    @property
    def value(self):
        print("Displaying value:")
        return self._age
    
    @value.setter
    def value(self, age):
        if age > 100:
            raise ValueError("Age can't be greater than 100.")
        print("Setting the values:")
        self._age = age
    
    @value.deleter
    def value(self):
        print("Deleting the instance property:")
        del self._age

if __name__ == '__main__':

    obj = Person(1000)
    print(obj.value)

    obj.value = 1000

    del obj.value
