

"""
    list:
        array-like object
        container of elements.
        can carry different data types

    creation:
        []
        list()

    features:
            supports indexing, reverse indexing, slicing, unpacking, membership (in)

    important methods:
            append, sort, reverse, remove, insert, extend, count

    important functions:
            del







"""

my_list = []

new_list = list()
print(new_list)

third_list = list("my str")
print(third_list)


print(third_list[0])

print(third_list[-1])

print(third_list[3:])

my_string = "- this is the separator- ".join(third_list)
print(my_string)


# fourth_list = "Hello world".split(" ")
# print(fourth_list)
my_new_list = [5, 0, 1, 2, 3]

my_new_list.append(4)

print(my_new_list)

element = my_new_list.pop()
print(element)
print(my_new_list)

element = my_new_list.pop(0)
print(element)
print(my_new_list)


my_new_list.append(-1)
my_new_list.append(-15)

my_new_list.append(2.5)

print(my_new_list)

my_new_list.sort(reverse=True)

print(my_new_list)

str_list = ["Ahmed", "Mohamed", "Abdallah", "Abdallah", "Mostafa"]

str_list.sort(key=len)

print(str_list)

str_list.reverse()
print(str_list)


str_list.insert(0, "Salssabel")

print(str_list)

str_list.remove("Abdallah")

print(str_list)

str_list.extend([1, 2, 3, 4])

print(str_list)

str_list.append([1, 2, 3, 4])

print(str_list)

print(str_list[-1][0])

my_list = [1, 2, 3]
my_list = my_list + [4, 5, 6]

print(my_list)



my_list = [1, 2]

a, b = my_list
print(a)
print(b)


a = 5
b = 6

b, a = [a, b]
print(b)
print(a)


"""
a, b= [1, 2, 3]
print(a)
print(b)
"""


a, b, _ = [1, 2, 3]
print(a)
print(b)



a, *_, b = [1, 2, 3, 4, 5, 6, 7]
print(f"{a=}")
print(f"{b=}")


a, *c, b = [1, 2, 3, 4, 5, 6, 7]
print(c)


if 2 in c:
    print("True")

print(2 in c)



del c[1]

print(c)


