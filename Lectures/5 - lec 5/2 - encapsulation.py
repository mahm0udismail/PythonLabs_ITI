"""
    Encapsulation:
            in other languages, java, C#, C++ have keywords:
                                                           public, private, protected

            in Python: we don't have the concept of privacy, since we're all grown-ups

            it's not an actual privacy forced by the interpreter
            but it's through convention.
            and it applies on attributes and methods.

            protected:
                    _ one underscore after the dot

            private:
                    __
                    it has nothing to do with privacy
                    name mangling, avoid name collision in inheritance and multiple inheritance
                    and collision of namespaces
                    it changes the name to:
                    _Class__attribute

            programmer will follow convention:
                    getters and setters (mutators and accessors)
                    get_   set_


    tips and tricks:
        using @property decorator:
            use the attribute name as the method name for both setters and getters.

        using property function:
            the getter must be the first argument, the setter must be the second.

"""


class Phone:

    def __init__(self, model, storage):
        self.__model = model
        self.__storage = storage

    def get_model(self):
        return self.__model

    def set_model(self, name):
        self.__model = name

    def get_storage(self):
        return self.__storage

    def set_storage(self, size):
        self.__storage = size


my_phone = Phone("S24", 512)

print(my_phone.get_model())
my_phone.set_model("Iphone 15")

print(my_phone.get_model())


class ComplexNumbers:
    def __init__(self, num1, num2, summation):
        self._num1 = num1
        self._num2 = num2
        self._summation = summation

    def get_num1(self):
        return self._num1

    def set_num1(self, number):
        self._num1 = number

    def get_num2(self):
        return self._num2

    def set_num2(self, number):
        self._num2 = number

    def get_sum(self):
        return self._summation

    def set_sum(self, number):
        self._summation = number


my_number = ComplexNumbers(2, 4, 6)
my_number.set_num1(3)
my_number.set_num2(5)
my_number.set_sum(my_number.get_num1() + my_number.get_num2())


# my_number.summation = my_number.num1 +  my_number.num2

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        print("Hello from the method name")
        return self._name

    @name.setter
    def name(self, other):
        self._name = other

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, other):
        if other < 0:
            raise Exception("Age can't be less than zero")
        self._age = other


my_person = Person("Kareem", 22)
print(my_person.name)

my_person.name = "Abo gabal"

print(my_person.name)

my_person.age = 15
print(my_person.age)


# my_person.age = -1

my_person._age = -1
print(my_person.age)



class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, other):
        self._name = other


    name = property(get_name, set_name)

    def get_age(self):
        return self._age


    def set_age(self, number):
        self._age = number

    age =  property(get_age, set_age)

    def __do_something(self):
        print("I'm doing something")



my_person = Person("Abo gabal", 22)
print(my_person.name)

my_person.name = "Kareem"

print(my_person.name)


my_person._Person__do_something()







