

for i in range(5):
    print(i, end=" ")


print()



# for (let i = 0; i < 3; i++){
#
# }
#
#     for element of my_list



print()
print(range(5))

# enumerate
my_list = ["320", "Ahmed", "Mohamed"]

# elements version
for i in my_list:
    print(i)

# basic version
for i in range(len(my_list)):
    print(i)


# advanced/better version
for index, value in enumerate(my_list):
    print(index)
    print(value)



for i in range(5):
    print(i)
else:
    print("done")


# get me the prime numbers from 2 to 100

the_prime_numbers = []

for i in range(2, 102): # 2 -> 101
    for j in range(2, i):  # 2 -> i
        if i % j == 0:
            break
    else:
        the_prime_numbers.append(i)

print(the_prime_numbers)


for i in range(5):
    pass
    # modify_database_objects()
else:
    print("all done")












