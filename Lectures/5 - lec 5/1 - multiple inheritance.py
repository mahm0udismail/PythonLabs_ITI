"""
    multiple inheritance
        syntax:
            class C (A, B):


    Method Resolution order:
            the order in which we can resolve the existence of attributes or methods
            it works: Depth first , from left to right.
"""


# Object

class Dinosaur:
    def __init__(self, weight):
        self.weight = weight


class Carnivore:
    def __init__(self, diet):
        self.diet = diet


class Tyrannosaurus(Dinosaur, Carnivore):
    def __init__(self, weight, diet):
        Dinosaur.__init__(self, weight)
        Carnivore.__init__(self, diet)


my_dino = Tyrannosaurus(400, "What it wants")

print(my_dino.weight)
print(my_dino.diet)

print(my_dino)

print(Tyrannosaurus.__mro__)


class A:
    def say_hello(self):
        print("Hello from class A")

class B:
    def say_hello(self):
        print("Hello from class B")

class C(A, B):
    def say_hello(self):
        print("Hello from class C")


    def say_hello_from_class_b(self):
        super(A, self).say_hello()


#
# def say_hello(self):
#     print("hello from object")


my_object = C()
my_object.say_hello()

print(C.__mro__)

my_object.say_hello_from_class_b()

# my_object.say_hello = say_hello
#
# my_object.say_hello(my_object)


class A:
    pass

class B:
    pass

class C(A, B):
    pass


class D(C, B):
    pass

my_object = D()
print(D.__mro__)


# class A:
#     pass
#
# class B:
#     pass
#
# class C(A, B):
#     pass
#
#
# class D(B, C):
#     pass
#
# my_object = D()
#
# print(D.__mro__)

# http://python-history.blogspot.com/2010/06/method-resolution-order.html


















