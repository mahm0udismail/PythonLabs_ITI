"""
    functions:
            used to simplify logic, repeat unrelated logic

            can take parameters:
                    - positionals (rely on position)
                    - key worded arguments: (rely on names)
                            - can't have positionals after key worded args

            can take default parameters:
                    never give it a function call, or a mutable type.


            Scope:
                global: can only access global, doesn't need key word to modify
                local: can access global, can't modify without special key word
                lexical: can access both global and local, can't modify without special key word

                keywords:
                        # DON'T USE BOTH
                        global
                        nonlocal

            Available global functions:
                sum, min, max, any, all
                print
                len, type, id
                str, int, tuple, set, bool, range

            args and kwargs:
                args: arguments
                kwargs: key worded arguments


"""


def my_function():
    pass


print(my_function())


def my_function():
    return "inside my function"


print(my_function())


def old_summation(x, y, z=0):
    return x + y + z


print(old_summation(5, 6))
print(old_summation(5, 6))


def new_function(first_multiply_parameter, second_parameter, third_parameter, fourth_multiply_parameter):
    return first_multiply_parameter * second_parameter + third_parameter * fourth_multiply_parameter


print(new_function(1, 5, 6, 1))

print(new_function(1, 2, 3, fourth_multiply_parameter=5))


def extra_new_function(first_multiply_parameter, second_parameter, third_parameter, fourth_multiply_parameter=1):
    return first_multiply_parameter * second_parameter + third_parameter * fourth_multiply_parameter


print(extra_new_function(1, 2, 3))

#
# def add_number_to_list(number, my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append(number)
#     return my_list
#
#
# a = add_number_to_list(2)
# b = add_number_to_list(1, [10])
# c = add_number_to_list(5)
#
#
#
# print(a)
# print(b)
# print(c)


import random


def add_random_number(x, the_random=random.choice([1, 2, 3, 4, 5, 6])):
    print(the_random)
    return x + the_random


add_random_number(1)
add_random_number(5)
add_random_number(6)

print("scope")

# Global, Local, Lexical/internal
x = 5


def my_function():
    y = 6
    print(x)

    def internal_function():
        print(x)
        print(y)

    internal_function()


my_function()

# global
# nonlocal

print("global key word")
new_int = 5


def new_function():
    global new_int
    new_int += 1


print(new_int)

new_function()

print(new_int)

print("non local")


def completely_new_function():
    y = 6

    def new_internal_function():
        nonlocal y
        y = 5

    print(y)
    new_internal_function()
    print(y)


completely_new_function()

my_list = [1, 2, 3, 4]

print(sum(my_list))
print(min(my_list))
print(max(my_list))

my_list = ["", [], 0, False]

print(any(my_list))

my_list = [" ", [1], 1, True]

print(all(my_list))

my_objects = [1, 2, 3, 4, 6]

print(all(True if element < 5 else False for element in my_objects))


#
# _summation = 0
# for element in my_list:
#     _summation += element
#
# print(_summation)

def summation(*args, **kwargs):
    print(type(kwargs))
    print(kwargs)
    print(type(args))
    summing = 0
    if args:
        for element in args:
            summing += element
    return summing


print(summation(4, 5, 7))
print(summation(4, 5, 9, 12, 20))

print(summation())

print(summation(1, 4, third=5, fouth=17, kareem=555))

print(summation())










