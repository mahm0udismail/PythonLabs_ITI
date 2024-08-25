my_str = "Kareem Morsy"

print(hash(my_str))

# 1, n, log n, n log n, n2, 2**n (exponential), n!, n**n

my_list = [element for element in range(10_000_001)]

my_set = set(my_list)


import time

start = time.time()

print(10_000_000 in my_list)

print(time.time() - start)




start = time.time()

print(10_000_000 in my_set)

print(time.time() - start)


# set membership checking is O(1)


# list, tuple membership checking is O(n)










