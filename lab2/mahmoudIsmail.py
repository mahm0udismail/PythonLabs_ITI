# 1 - Fill an array of 5 elements from the user, 
#       Sort it in descending and ascending orders then display the output.

# lst1 = []
# lst1 = [int(item) for item in input("Enter the list items : ").split()]
# print(lst1)

# def toSordedList(list):
#     list.sort(reverse=True)
#     print("sort with reverse",list)
#     list.sort()
#     print("normal sort",list)
# toSordedList(lst1)

# 2 - Write a function that accepts two arguments (length, start) 
#       to generate an array of a specific length filled with integer numbers 
#       increased by one from start.

# lst2 = []
# def generateArray(length, start):
#     for i in range(length):
#         lst2.append(start) 
#         start+=1
#     print(lst2) 

# generateArray(5, 2)

# 3 - Write a program which repeatedly reads numbers until the user
# 	    enters “done”. Once “done” is entered, print out the total, count, and average of the numbers.
# 	    If the user enters anything other than a number, detect their
#             mistake, print an error message and skip to the next number.

def done():
    total = 0
    count = 0

    while True:
        user_input = input("Enter a number or 'done' to finish: ")

        if user_input.lower() == 'done':
            break

        number = float(user_input)
        total += number
        count += 1

    if count > 0:
        average = total / count
        print(f"Total: {total}, Count: {count}, Average: {average}")
    else:
        print("No numbers were entered.")
done()

# Bonus:
# 4 - discuss why dictionary key can only be an immutable type, 
# 
# why the set only accepts immutable types, 
# 
# how the set makes sure it has non-duplicates