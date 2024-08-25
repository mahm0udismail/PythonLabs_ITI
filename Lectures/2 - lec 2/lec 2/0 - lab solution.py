# 2 -
# my_input = input("Enter a binary number: ")
# if my_input and my_input.count("0") + my_input.count("1") == len(my_input):
#     print(int(my_input, 2))


my_input = 15

if not my_input % 15:
    print("FizzBuzz")
elif not my_input % 5:
    print("Buzz")
elif not my_input % 3:
    print("Fizz")
else:
    print(my_input)