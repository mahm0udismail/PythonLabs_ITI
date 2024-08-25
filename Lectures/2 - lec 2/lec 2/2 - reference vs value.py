
x = 5

print(id(x))
# everything is passed by reference


# immutable
def modify_int(x: int):
    print(x)
    x += 1
    print(x)

y = 5
modify_int(y)

print(y)



##############################

# mutable

def modify_list(x: list):
    print(x)
    x.append(4)

y = [1, 2, 3]
modify_list(y)

print(y)




