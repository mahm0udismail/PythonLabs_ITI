"""
    for loop -> while loops -> functions ->
    global available functions (sum, min, max, any, all)
    # after tuple and dictionary args and kwargs

    -> tuple -> set -> dictionary

    mutability:
            the ability to change in place.

            data types:
                list, dictionary, set

    immutability:
            once created never changed.

            data types:
                int, float, string, tuple, bool, None
"""

my_int = 5
print(id(my_int))
my_int += 1
print(id(my_int))

my_str = "Hello world"
new_str = my_str.replace("world", "universe")

print(my_str)
print(new_str)

my_str.lower()

print(my_str)


new_str = my_str.replace("world", "universe").lower().upper().title()  # method chaining


import sys
my_str = "AAA"

my_new_str = my_str

print(sys.getrefcount(my_new_str))

my_str = my_str.lower()
#
# print(my_str)
# print(my_new_str)






my_new_list = [1, 2, 3]

my_other_list = my_new_list

my_new_list.append(4)

# print(my_other_list)


import sys

print(sys.getrefcount(my_new_list))































