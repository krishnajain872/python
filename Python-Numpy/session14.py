import numpy as np
import time
import sys
# python List Vs Numpy array

# python list are dynamic linear datastructure its size get double
# it store the elements address(store the refrence)

# numpy array
# numpy arrays are static in nature
# it store the actual element rather storing the refrence


# speed
a = []
start = time.time()
for i in range(1, 10000000+1):
    a.append(i)

print(time.time() - start)

np.arange(10000000)


# space
sys.getsizeof(a
              )

a = np.arange(24).reshape(6, 4)
# fancy Indexing
# # pass a list of indices
# print(a)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]


# print(1,3,5 row)
# print(a[[1,3,5]])
# print(a[:,[0,3]])


# Boolean Indexing (important)
# make a array with random values

a = np.random.randint(1, 100, 24).reshape(6, 4)
# print(a)
# [[99 80 30 82]
#  [39 87 61 19]
#  [13 99 91 77]
#  [ 2 92 15 86]
#  [ 2 65 48 29]
#  [33 64 94  1]]

# now quetion is to find all the no. greater than 5

c = a > 50
# print(c)
# this returns a boolean
# array
# c = [[False False False  True]
#  [False False  True False]
#  [False  True False False]
#  [ True False False  True]
#  [ True  True False  True]
#  [ True False  True False]]

print(a[a > 50])
# ans
# [79 95 63 76 91 59 94 63 77 97 65]

# find even no. from the array
# print(a[a % 2 == 0])
# [96 12 44 34 84 90 80 20 34 42 50]
# boolean masking
# print(a[c])

