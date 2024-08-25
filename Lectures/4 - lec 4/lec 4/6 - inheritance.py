"""
    inheritance:
        don't repeat yourself
        a relationship of subclass IS superclass

        method overriding:
            to customize logic to your case

        isinstance(object, class)

        issubclass(subclass, superclass)

    INHERITANCE IS A ONE WAY ROAD.


    # multiple inheritance.

"""

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        return f"Hello, my name is {self.name} and I work as {self.occupation}"


    def say_age(self):
        return self.age


class SuperHero(Person):

    def __init__(self, name, age, occupation, superhero_name, nemesis):
        super().__init__(name, age, occupation)
        self.superhero_name = superhero_name
        self.nemesis = nemesis

    def say_you_are_a_superhero(self):
        return f"I'm a super hero, I'm {self.superhero_name}"

    def say_age(self):
        return f"old or young, I'll beat evil (also side note: I'm {super().say_age()})"

    def old_say_age(self):
        return super().say_age()


# kareem = Person("Kareem", 22, "Software engineer")
# print(kareem.say_hello())


kareem = SuperHero("Kareem", 22, "Software engineer", "Batman", "Abo Gabal")


print(kareem.say_hello())

print(kareem.say_you_are_a_superhero())

print(kareem.old_say_age())
print(kareem.say_age())
#

print(isinstance(kareem, Person))



class A:
    def say_hello_from_a(self):
        print("this is A")

class B(A):
    def say_hello_from_b(self):
        print("this is B")

class C(B):
    def say_hello_from_c(self):
        print("this is C")

class D(C):
    def say_hello_from_d(self):
        print("this is D")


print(issubclass(D, A))


object_of_class_d = D()
object_of_class_d.say_hello_from_a()
object_of_class_d.say_hello_from_b()
object_of_class_d.say_hello_from_c()
object_of_class_d.say_hello_from_d()


object_of_class_a = A()

object_of_class_a.say_hello_from_a()

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(A):
#     pass








