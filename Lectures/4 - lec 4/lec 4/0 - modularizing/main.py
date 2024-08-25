import os
from datetime import datetime

# block third party libraries

# block internal imports
from gabal import my_function
from kareem.morsy import second_function
from ahmed.tarek import my_third_function


"""
    modules attributes:
        __name__ = "the name of the module"
        __name__ == "__main__"
        if I imported that file
        __name__ == __esm_el_file__


"""


def main():
    my_function()
    my_third_function()






if __name__ == '__main__':
    main()
