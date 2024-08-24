import math
# q1 - write a program that prints hello world
print("hello world")

# q2 - application to take a number in binary form from the user, and print it as a decimal
t= True
while t:
    try:
        d = int(input('Enter a binary number: '), 2)
        print(f"The decimal equivalent is: {d}")
        t=False
    except ValueError:
        print("Invalid input. Please enter a valid binary number.")


#q3 
def fizz_buzz(x):
    if x % 15 == 0:
        return 'FizzBuzz'
    if x % 3 == 0:
        return 'Fizz'
    if x % 5 == 0:
        return 'Buzz'
    return x
print(fizz_buzz(15))

#q4 - Ask the user to enter the radius of a circle print its calculated area and circumference
radius = float(input("enter radius of a circle : "))
print("Area" , math.pi * radius**2)
print("circumference" , 2 * math.pi * radius)

#q5 - Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data
name=str(input("enter name: "))
import re

pattern = r'^[ .]*$'
 
while re.fullmatch(pattern, name) or name.isnumeric():
    name=str(input("plese enter name: "))
email=str(input("plese enter email: "))
while re.fullmatch(pattern, email) or email.isnumeric():
    email=str(input("plese enter email: "))
print(f'name is {name} and email is {email}')

#q6 - Write a program that prints the number of times the substring 'iti' occurs in a string
string="iti iti iti iti"
text= "iti"
print(string.count(text))