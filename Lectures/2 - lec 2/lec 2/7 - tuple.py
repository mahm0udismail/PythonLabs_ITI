"""
    tuple:
        immutable container

        typecase:
                tuple()
                ()
                element,

    why use it:
            1 - because it's immutable
            2 - less size than list (less flexible)

    supports:
            indexing, reverse indexing, slicing

    common methods:
            index
            count

    the best kind of swapping elements

"""



x = (1, 2, 3)
print(type(x))
x = x + (4, 5, 6)
print(x)



# swapping elements

a = 5
b = 6

a, b = b, a

print(f"{a=}")
print(f"{b=}")


new_tuple = 1,
print(type(new_tuple))


my_tuple = (1, 2, 3, 4, 5, 6)

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple[1:4])


#

for index, element in enumerate(my_tuple):
    print(f"{index=}")
    print(f"{element=}")



