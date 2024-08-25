"""
    bool:

    type casts:
        bool()

        Only one Object that lives in memory
        True.
        False.
        None.


    truthy values:
                True, any number other than 0, "1", [1], (1), {"key": "Value"}, {1}

    Falsy values:
                False, 0, "", [], (), {}, {}, None


    if

    elif

    elif

    elif

    else

    and
    or

    no &&
    no ||

    short-circuiting:
        or: acts as if the first Truthy value is enough
        and: acts as if the first Falsy value is enough

    tips:
        1 - If you can use the actual value, use it instead of casting to bool and then comparing with True and False
        2 - use Is instead of == for comparison with True or False

        talk about why in the oop part
"""

if True:
    print("this is true")
print("anything else")


if 1:
    print(1, end=" ")
    print("is a truthy value")


if " ":
    print(" ", end=" ")
    print("is a truthy value")


if [1]:
    print([1], end=" ")
    print("is a truthy value")


if 0:
    print("zero is a truthy value")
else:
    print("zero is a falsy value")

if "":
    print("zero is a truthy value")
else:
    print("empty string is a falsy value")


if 1 and True:
    print("both are true")

if 1 or False:
    print("one of them is True")

y = True

x = y or 5

print(x)




y = False

x = y and 5

print(x)


print(bool([1]))

#
if 5:
    print("5 is truthy value")




x = True

if x:
    print("x is true")









