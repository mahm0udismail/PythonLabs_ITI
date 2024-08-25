"""
    Object Oriented Programming:
    what is it:
            paradigm: a way of thinking.
            instead of logic and functions.
            think about data and objects.

    every object has:
                    1 - actions.
                    2 - attributes.

    struct vs class:
            DRY : don't repeat yourself
            inheritance

    why use oop:
        1 - re-usability: inheritance
        2 - modularity: you can insert an object inside an object, living in another object
                        living in a wholly different third party library.
        3 - easy to think about, easy to reason with, easy to wrap your head around.
        4 - mimics real life objects: just like a normal human being does.


   Building blocks of oop:
                    Class, Object

        class:
            blueprint to create the object, its data, and its methods.

            class attributes:
                    public knowledge, general knowledge through all object

            class methods:
                    public usage for the entire class, usually returns objects of the class

            static methods:
                    public usage for everything, doesn't need reference to anything
                    logically related to the class

        object:
            an instance of the class

            object methods and attributes:
                    special to that specific object

            # dunder methods (double underscore methods)

"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat_food(self):
        print(f"hello I'm {self.name} and I'm {self.get_age()} and I'm eating.")


    def get_age(self):
        return self.age

human = Person("Kareem", 22)
print(human)
print(human.name)
print(human.age)

human.eat_food()


class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"this is a circle and my radius is {self.radius}"

    def __repr__(self):
        return f"this is the object inside of a container and my radius is {self.radius}"

    def get_circumference(self):
        return round(2 * self.radius * self.__class__.pi, 2)

    def save(self):
        with open("circles.txt", "a") as file:
            file.write(f"{self.radius}\n")

    @classmethod
    def load(cls):
        my_list = []
        with open("circles.txt", "r") as file:
            for radius in file.readlines():
                my_list.append(cls(int(radius.strip())))
        return my_list





my_circle = Circle(5)

my_first_object, my_second_object, my_third_object = Circle.load()


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y




    @staticmethod
    def draw_axes():
        for i in range(10, 0, -1):
            print(i)
        for i in range(10):
            print(i, end=" ")



my_point = Point(1, 3)

Point.draw_axes()


print(my_first_object)

print(Circle.load())



print(Circle.__str__(my_first_object))













