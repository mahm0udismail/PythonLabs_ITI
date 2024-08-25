
from typing import Iterator

# list, tuple, dict, generator, map, filter, zip, string

"""
    - function that returns an iterator
    - function that can halt/pause its execution, and resume at a later time. 
    - special with the word, yield instead of return
"""

def return_first_three_number():
    for i in range(100):
        yield i

import sys

my_list = [element for element in range(100)]
print(sys.getsizeof(my_list))

my_generator = return_first_three_number()
print(sys.getsizeof(my_generator))
print(type(my_generator))

for element in my_generator:
    print(element)

for i in range(101):
    next(my_generator)





my_other_generator = return_first_three_number()


