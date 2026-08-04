#property decorators are used to control the element
#_variable name in variable defines that this variable/property should not be accessed directly and no direct reading or writing vale-special meaning

class TeaLeaf:
    def __init__(self,age):
        self._age=age

    @property   #it gets the value and we are controlling how we are reading the value
    def age(self):
        return self._age+2

    @age.setter #it sets the value and we are setting how we want our value and even error
    def age(self,age):
        if 1<=age<=5:
            self._age=age
        else:
            raise ValueError("tea leaf should be between 1 and 5 yrs")

leaf=TeaLeaf(2)  #creating an object
print(leaf.age) # behind the scene we are calling age method but we dont need to put parantheses thats the magic of @property

leaf.age=4
print(leaf.age)