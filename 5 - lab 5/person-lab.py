"""
    class Person:
    Private Attributes:
        __name:
        __brith year:

    methods:
        say_hello: prints name whenever called

    properties:
        name
        age
"""
import datetime

class Person:
    def __init__(self, name, birthyear):
        self.__name = name
        self.__birthyear = birthyear

    def say_hello(self):
        print(self.__name)



class Subclass(Person):
    def __init__(self, name, birthyear):
        super().__init__(name, birthyear)

    @property
    def age(self):
        current_year = datetime.datetime.now().year
        return current_year - self._Person__birthyear
    
p1 = Person("Mahmoud", 2000)
p1.say_hello()

s1 = Subclass('Mahmoud', 2000)
s1.say_hello()
print(s1.age)
