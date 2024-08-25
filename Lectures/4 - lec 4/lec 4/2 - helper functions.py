
"""
    helper global functions:
        map: apply function to an iterator
        filter: filter an iterator according to a function that returns a boolean value
        zip: pack iterators together.
"""

my_list = [1, 2, 3, 4]

my_second_list = list(map(lambda x: x * 2, my_list))

print(my_second_list)
print(my_list)

my_third_list = list(filter(lambda x: not bool(x % 2), my_list))
print(my_third_list)

print(map(lambda x: x * 2, my_list))

print(filter(lambda x: not bool(x % 2), my_list))

my_third_list = ["a", "b", "c"]
my_zip_object = zip(my_list, my_second_list, my_third_list)
print(my_zip_object)

my_dict = dict(zip(my_list, my_second_list))

print(my_dict)



my_tuple = tuple(my_zip_object)

print(my_tuple)













