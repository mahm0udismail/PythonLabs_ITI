"""
    functions are a first-class citizens
        1 - can be used as parameters
        2 - can be saved inside variables
        3 - can be returned from functions


    decorators:
        functions, that takes functions, and return functions

        used to enhance and modify the behavior of functions
        the bases for class functions, static methods

"""

# def exponent_of_2(number):
#     return number ** 2
#
# print(exponent_of_2(5))
# print(exponent_of_2(3))
#
# def exponent_of_3(number):
#     return number ** 3
#
# print(exponent_of_3(5))
# print(exponent_of_3(3))


def exponent_creator(power):
    def exponent(number):
        return number ** power
    return exponent

exponent_of_2 = exponent_creator(2)

print(exponent_of_2(5))

# def my_function():
#     print("this is inside of the function")
#
# def beautify(function):
#     print("*" * 40)
#     function()
#     print("*" * 40)
#
#
# beautify(my_function)

def my_function():
    print("this is inside of the function")


def beautify(function):
    def wrapper():
        print("*" * 40)
        function()
        print("*" * 40)

    return wrapper

final = beautify(my_function)
final()

print("this is after creating the final version of the function")




# def my_new_function():
#     print("another function")
#
# new_final = beautify(my_function)
#
#
# new_final()

@beautify
def my_new_function():
    print("another function")

my_new_function()

import time

def timer(ibrahim):
    def wrapper():
        start = time.time()
        print(ibrahim())
        print(time.time() - start)

    return wrapper


@timer
def create_list_and_check():
    my_list = [i for i in range(1_000_000)]
    return 500 in my_list

create_list_and_check()









