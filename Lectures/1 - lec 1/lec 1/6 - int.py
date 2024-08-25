



"""
int:
    type casts:
            int()
            remove spaces, accepts _
            int("400")
            int("  400_000  ")
            int("101", 2)
            int("F", 16)

    tips:
        never use IS for equality checks with numbers

arithmetic operations:

    +
    -
    /
    *
    %: modulo
    //: integer division / floor division
    **: power  2 ** 3 : 8  
"""
x = 5

y = 1000_000_000

print(y)



z = 5
y = 5
# never use is for equality checks with ints
# always use ==
print(z is y)


# CPython optimization
x = -1
y = -1

x += 1
y += 1

while x is y:
    x += 1
    y += 1

print(x , y)

j = 300
k = 300

print(j == k)
print(j is k)

j += 1
k += 1

print(j == k)
print(j is k)


# Lesson learned
# never use is for equality checks

# use ==



t = 999999999999999999999999999994444444499999999999999999999999995555555
u = 999999999999999999999999999994444444499999999999999999999999995555555

print(t is u)
print(t == u)



# type casts:

print(int("400"))
# remove spaces, accepts _

print(int("  400_000  "))


print(int("101", 2))

print(int("F", 16))