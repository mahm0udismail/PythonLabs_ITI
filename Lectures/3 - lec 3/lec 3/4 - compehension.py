
"""
    list, set, dict
    comprehension




"""




my_array = []

for i in range(1, 1_000_001):
    my_array.append(i)

print(len(my_array))

my_list = [i for i in range(1, 1_000_001)]
print(len(my_list))


##############################################

my_new_array = []
for i in range(1, 1_000_001):
    if not i % 2:
        my_array.append(i)
    else:
        my_array.append(i+1)

my_new_list = [i if not i % 2 else i + 1 for i in range(1, 1_000_001)]
print(len(my_new_list))


####################################################


my_new_set = {i for i in range(100)}
print(len(my_new_set))



####################################################
my_new_dict = {index: value for index, value in enumerate(my_new_list)}

print(my_new_dict)


####################################################













