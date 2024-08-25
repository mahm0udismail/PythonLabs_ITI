"""
    set:
        type cats:
            set()
            {1}


        mutable container of elements
        can only carry immutable types

    why use:
        can't have duplicate elements.


    important notes:
                before python 3.7: it couldn't guarantee order of elements

    supports:


    important methods:
        add, pop, remove, discard
        intersection / &
        union / |

    # why can it only accepts immutable types
"""


my_list = [1, 2, 2, 3, 4, 4, 5, 6]

print(set(my_list))


# check for duplicates

my_list = [1, 2, 3, 4, 5]

print(len(my_list) == len(set(my_list)))




my_set = {1, 2, 3, 4}

my_set.add(5)

print(my_set)


# my_set.add([1, 2, 3])
# unhashable type: 'list'
# print(my_set[0])
# why can it handle the entry of elements without raising errors
# why errors are KeyErrors


my_set.remove(5)


print(my_set.intersection({1, 2}))

print(my_set.union({1, 2, 3}))


print(my_set | {7, 8, 9})

print(my_set & {1, 2})



new_set = {1, 2, 3, 4}
new_set.discard(5)
print(new_set)






