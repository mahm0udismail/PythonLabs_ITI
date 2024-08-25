"""
    errors:
        1 - syntax errors
        2 - runtime errors:
                unfortunate errors, due to lack of defensive programming

                try:
                    code that might raise an error, that I want to catch
                except:
                    the behavior I wanna do if an exception was raised
                else:
                    code that happens if the try succeeded, and if errors happened, I want to raise
                finally:
                    code that happens regardless of anything else.
                    Database connection closure


        3 - logical errors:
                import math
                print(math.floor(10.5))

                print(math.floor(-10.5))

"""

try:
    my_input = int(input("Enter a number: "))
    number = 10 / my_input
except ZeroDivisionError:
    print("you entered a zero")
except ValueError:
    print("you entered something that can't be turned into an int")
except Exception as e:   # general exception clause
    print(e)
else:
    # to raise exception that I want to halt execution
    print("try passed successfully")
finally:
    print("finally done")
    # db.close()


print("done")

# exit gracefully.
# exit not gracefully.

import sys


def my_function():
    try:
        other_input = int(input("Enter a number: "))
        other_number = 10 / other_input
    except ZeroDivisionError:
        print("you entered a zero")
        return -1
    except ValueError:
        print("you entered something that can't be turned into an int")
        return -1
    except Exception as another_e:  # general exception clause
        print(another_e)
        return -1
    else:
        # to raise exception that I want to halt execution
        print("try passed successfully")
        # sys.exit()
        # raise Exception("Ibrahim asked a very good question, thus he's failing the class")
        # return other_number
    finally:
        print("finally done")


print(my_function())








# raise Exception("Ibrahim asked a very good question, thus he's failing the class")




