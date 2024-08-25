"""
    generators:
            special functions that returns an iterator
            special functions that can halt its execution

        special with the word:
            yield

    base for async and await in python, co-routines in general
"""

# def function():
#     return 1
#     return 2
#     return 3


def my_one_to_three():
    yield 1
    yield 2
    yield 3


for element in my_one_to_three():
    print(element)


print("range")

def my_own_implementation_of_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0
    while start < end:
        yield start
        start += step


# for element in my_own_implementation_of_range(1, 15, 2):
#     print(element)


print("next")

my_list = [i for i in range(1_000_000)]

for element in my_list:
    pass

my_iterator = my_own_implementation_of_range(1_000_000)

import sys

print(sys.getsizeof(my_list))

print(sys.getsizeof(my_iterator))

new_iterator = my_own_implementation_of_range(1_000_000)


print(type(new_iterator))

