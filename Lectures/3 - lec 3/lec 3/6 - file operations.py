"""
    file operations.
    modes:
        w, a, r, rw, rb, wb, ab

    tips:
        remember to only open files using context manager and "with" syntax
        with open(file_name, mode) as file:
            # do some operations

    functions:
        open: returns a handler.
              which is a cursor

    methods:
        close, write, read, readlines, seek
"""

file = open("new_file.txt", "w")
file.write("something\n")
file.close()

file = open("new_file.txt", "a")
file.write("something else")
file.close()


file = open("file.txt", "r")
text = file.readlines()
file.close()

print(text)


def copy_function(old_file_name, new_file_name):
    _file = open(old_file_name, "rb")
    _bytes = _file.read()
    _file.close()

    _file = open(new_file_name, "wb")
    _file.write(_bytes)
    _file.close()


copy_function("images.jpeg", "an image of a cat.jpg")



file_handler = open("file.txt", "r")
file_handler.seek(0)
for line in file_handler:
    print(line, end="")

file_handler.seek(0)

for line in file_handler:
    print(line, end="")

file_handler.close()

# context manager
with open("new_file.txt", "r") as file:
    text = file.read()

print(text)











