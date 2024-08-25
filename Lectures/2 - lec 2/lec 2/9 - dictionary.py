"""
    Dictionary:
        mutable container of elements

        type cast:
            dict()
            {}

        tips:
            before python 3.7:  the order wasn't guaranteed
            cpython 3.6:        as an implementation detail

            keys MUST be immutable # the same reason the set only accepts immutable types.

        mutable types indexing instead of number indexing


        methods:
            update, pop, clear

            keys, values, items


"""

my_dict = {"key": "value"}
print(my_dict["key"])


my_dict["another_key"] = "another_value"
print(my_dict)


my_dict[1.5] = "this is number 1"

print(my_dict)


my_dict[(1, 2, 3)] = "this is a tuple"

print(my_dict)

my_dict["a list"] = [1, 2, 3]

print(my_dict)


print(my_dict.keys())
print(my_dict.values())

print(my_dict.items())


for key in my_dict.keys():
    print(f"key={key}: value={my_dict[key]}")


for value in my_dict.values():
    print(value)


for key, value in my_dict.items():
    print(f"key={key}: value={value}")


for element in my_dict:
    print(element)


print(my_dict)

my_second_dict = {"my second key": 5, "my_third key": 6}

my_dict.update(my_second_dict)

print(my_dict)









