
"""
    lambda functions:
            anonymous inline function,

            used once, can't reference
"""


my_list = [
    {"key": 1},
    {"key": 2},
    {"key": -1},
]


def my_comparison(my_dict):
    return my_dict["key"]

my_list.sort(key=lambda my_dict: my_dict["key"])

print(my_list)






