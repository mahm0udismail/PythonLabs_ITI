
"""
    Recursion:
        the process of repeating items in a self-similar way or self-repeating way.
        a process that repeats itself until a solution is found

        part:
            "divide and conquer"
            "decrease and conquer"
            merge sort, depth first search, dynamic programming.

        to understand recursion, you must understand recursion

    # if you can solve the simplest step of the big problem, you can solve the problem

"""

"""
    how many twists does it take to screw in a light bulb
    
    base case:
            law mtrkba already?  0
            
            law mesh mtrkba?
                screw once, then ask me again
"""


"""
    how to go home:
        where am i? 
                home: stop moving
                
                else: move 1 step towards home
            ask again




"""






my_int = 3 * 5

def multiply(base_number, multiplier):
    sum = 0
    while multiplier > 0:
        sum += base_number
        multiplier -= 1
    print(sum)

multiply(2, 10)
def recursive_multiply(base_number, multiplier):
    if multiplier == 1:
        return base_number
    return base_number + recursive_multiply(base_number, multiplier - 1)

print(recursive_multiply(4, 5))


# golden ratio, fibonnaci
# """
# 1 ,1 , 2, 3, 5, 8, 13, 21, 34, 55
# """







# 1, 1, 2, 3, 5, 8, 13, 21






def nth_fib_number(number):
    if number == 1:
        return 1
    if number == 2:
        return 1

    return nth_fib_number(number - 1) + nth_fib_number(number - 2)


print(nth_fib_number(5))























