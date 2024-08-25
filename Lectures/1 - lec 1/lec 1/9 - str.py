
"""
    str:
        type cast:
                str()

    useful methods:
        indexing: [1]
        len(): length
        in: to check on the presence of the letter in the iterator
        # slicing: [from:to:step]

    please use formatted strings / f strings

    remember to talk about: mutable vs immutable
                            why use value then is then == in boolean checking

"""
from more_itertools.more import first

x = ""
y = ''

x = 5
y = str(x)

print(type(y))

# this is a single line comment

"""
this is 
a 
multi-line
comment
"""


x = "Eslamreda.info"

if "e" in x:
    print("there's an E in Islam")

y = " Abdallah"

print(y[1])

print(y[1:4])

print(y[1::2])

print(y[len(y)- 1])

print(y[-1])
print(y[-2])

print(y[::-1])

# print(y[20])
#
# print(y[-50])

y = "Mahmoud Ahmed El-sayed"

print(y.count("m"))

z = y.lower()
print(z.count("m"))

print(y.upper())

print(y.isupper())
print(y.islower())

print(y.index("m"))

# print(y.index("z"))

print(y.find("m", y.find("m")+1))

print(y.rfind("m"))


print(y.startswith("M"))

print(y.endswith("d"))

print(y.startswith("Mahmoud"))



x = "  Ahmed \n \t   "
print(len(x.strip()))
print(x.strip() == "Ahmed")

if "folan " == "folan ":
    print(True)


# print(x.rstrip())
# print(x.lstrip())

x = " Ahmed  "

print(x.replace(" ", "A"))

# print(help(x.replace))

print("5a".isnumeric())

print("5".isalpha())

print("5".isalnum())

print("5".isdigit())

print("*".isalnum())



print("ⅠⅢⅧ".isnumeric())
print("ⅠⅢⅧ".isdigit())


print("بشس".isascii())
# UTF-8


first_name = "Mahmoud"

last_name = "Wafi"


print(first_name + " " + last_name)

age = 22

# print(first_name + " " + last_name + " and my age is: " + age)

print(first_name + " " + last_name + " and my age is: " + str(age))

print("%s %s" % (first_name, last_name))
print("%s %s and my age is %d" % (first_name, last_name, age))

print("{} {} and my age is {}".format(first_name, last_name, age))

# print("{} {} and my age is {} {}".format(first_name, last_name, age))

print("{name_1} {name_2} and my age is {my_age} {my_age}".format(name_1=first_name, name_2=last_name, my_age=age))

print("{1} {0} {0}".format(first_name, last_name))


print(f"My first name is {first_name} and my last name is {last_name} and my age is: {age + 5}")


x = input("Give me a number: ") # always a string
































def main():
    pass


if __name__ == '__main__':
    main()














