"""
    Polymorphism:
        is change, many faces
        often means group of functions with the same name, but with different output
        concept in which a single interface is applicable with different types.

    polymorphism:
        1 - method overloading # We do not support method overloading:
            we do it using default arguments, *args and **kwargs

        2 - method overriding (Inheritance)

        3 - Operator overloading:
            +, -, *, /, //
            using dunder methods:
                __add__, __iadd__, __mul__, __lt__, __le__
                __gt__, __ge__, __truediv__, __floordiv__
                __sub__

            c++, Java
        4 - duck typing (compile time binding vs runtime binding):
            if it walks like a duck, and talks like a duck, it's probably a duck

            I don't care about the type of the object, I care about what it can do.

            easier to ask for forgiveness than for permission
"""
from numbers import Complex

my_number = 8 + 5

print(my_number)

my_string = "Abo" + "Gabal"
print(my_string)

my_list = [1, 2] + [3, 4]
print(my_list)


class Mathematics:

    def do_summation(self, x, y, z):
        return x + y + z

    def do_summation(self, x, y):
        return x + y



my_math_object = Mathematics()
print(my_math_object.do_summation(2, 3))


class FinancialAccount:
    def __init__(self, amount):
        self.amount = amount

class BankAccount(FinancialAccount):

    def __add__(self, other):
        return self.amount + other.amount



class InvestmentAccount(FinancialAccount):
    pass


ba = BankAccount(500)
ia = InvestmentAccount(900)

print(ba + ia)

# print(ia + ba)
# iterator: iterate on it
# __iter__
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __str__(self):
        return f"Point({self.x}, {self.y})"


point_1 = Point(1, 1)
point_2 = Point(3, 3)

my_new_point = point_1 + point_2
print(my_new_point)

point_1 = Point(1, 1)
print(point_1)
point_1 += Point(3, 3)
print(point_1)



class Pitcher:

    def hit(self):
        print("hitting the ball")

class Singer:

    def hit(self):
        print("My song was a hit, I'm so rich")



def use_my_hit(some_object):
    try:
        some_object.hit()
    except AttributeError:
        print("this object has no method hit")


tiger_woods = Pitcher()

abo_gabal = Singer()

class A:
    pass

object_of_a = A()


use_my_hit(tiger_woods)
use_my_hit(abo_gabal)
use_my_hit(object_of_a)







