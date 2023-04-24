import numpy as np

# np.array() function

a1 = np.array([1, 2, 3, 4])  # this is 1d array or vector
# # -> numpy arrays are fixed size
# # list in python store hetrogenous data (like string float int all at once )
# # list in python is dynamic sized as it can double its size
# # print(a)
# print(type(a))
# for i in a:
#     print(i)


# this is 2d array or matrix
a2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=np.int32)
# print(a)

# # 3D numpy array also called tensor
# # in numpy there can be any no. of dimention made of a array
a3 = np.array(
    [
        [
            [
                1, 2
            ], [
                3, 4
            ]
        ], [
            [
                5, 6
            ], [
                7, 8
            ]
        ], [
            [
                9, 10
            ], [
                11, 12
            ]
        ]
    ]
)
# print(a)
# # float data type of numpy array
# # dtype argument can have data type of array as a parameter like float int string complex
# a = np.array([1., 2., 3.], dtype=float)
# print(a)


# # numpy arange() funtion

# # same as range data type in python it will create an array with in a range provided
# # here 1 is included in range and 11 is excluded in range it will take 11-1 i.e 10
# a = np.arange(1, 11)
# print(a)


# # similary as range datatype here we can use slicing parameter
# # like if want to print odd no. we provide 2 as slicing parameter
# # slicing paramter in range() and arange funtion work as a skiping / jump from the given range n-1 if n is the slicing parameter
# # in the current example as the Slicing parameter is 2 it will jump 1 number every time
# print(np.arange(1, 11, 2))
# # for this it will create an array of odd numbers [1,3,5,7,9] etc.
# print(np.arange(1, 11, 3))
# # print(np.arange(1, 11, 0))  # ERROR SLICNG  PARAMETER CANNOT BE 0
# print(np.arange(1, 11, -1))  # ERROR SLICNG  PARAMETER CANNOT BE 0


# # reshape() this funtion use to transpose the matrix that is created by numpy
# # this funtion will only work if transpose  is possible of an array

# print(np.arange(1, 11).reshape(2, 5))   # Array.reshape(row,column)
# print(np.arange(1, 11).reshape(5, 2))   # Array.reshape(row,column)
# # this is will give Error as the size of array is 10 or the no. of element in the array 10 which cannot be reshape or transpose in  5 row and 5 column which required 25 elements
# # print(np.arange(1, 11).reshape(5, 5))

# numpy funtion np.ones(shape,dtype(optional Argument)) , shape=(row,column) this it will create a matrix with row and column having all element 1
# numpy funtion np.ones(shape,dtype(optional Argument)) , shape=(row,column) this it will create a matrix with row and column having all element 1
# ex
# print(np.ones((2, 2)))  # by default its dtype is float
# print(np.ones((2, 2), dtype=int))
# print(np.ones((2, 2), dtype=str))
# print(np.ones((2, 2), dtype=bool))
# print(np.ones((2, 2), dtype=complex))


# # Similarly we  np.zero(shape,dtype) shape=(row,column)
# print(np.zeros((2, 2), dtype=int))
# print(np.zeros((2, 2), dtype=str))
# print(np.zeros((2, 2)))  # by default its dtype is float
# print(np.zeros((2, 2), dtype=bool))
# print(np.zeros((2, 2), dtype=complex))


# we use these two funtion to create / initialize arrays with some value quickly
# use in neural networks in deep learning to initialize the value of weights

# similary we have np.random.random(())
# print(np.random.random((2, 2)))  # woking with random values


# np.linspace
# it stands for linear space
#  it generate points between two givine provide points
#  help to find distances , ploting graphs
# syntax
# np.linspace(lowerLimit ,upperLimit,no. of points)
# print(np.linspace(-10, 10, 10))
# here in this example we an array with random no. between lowerLimit and upperLimit
# with  N no. of elements or points
# such that the distance between two consecutive points is always same


# to create an identity matrix in python numpy we use np.identity(n) funtion this funtion create a [n x n ] identity matrix
# print(np.identity(1))
# print(np.identity(5))


# Attribute

# ndim

# attribute to print n-dimention
# print(a3.ndim)  # 3 dimention
# print(a2.ndim)  # 2 dimentions
# print(a1.ndim)  # 1 dimentions

# shape attributes
# print(a1.shape)  # will provide shape as (row,col)
# print(a2.shape)  # will provide shape as (row,col)
# print(a3.shape)  # will provide shape as (no. of 2D arrays , row-2D array , col-2D array)

# size attribute and itemsize attribute
# np.dtype = int32 to types of size of int
# np.dtype = int64  (Default)
# print(a2.size)  # size of the total array (No. of elements)
# print(a2.itemsize)  # size of the  array element in memory


# # dtype attribute will display array type
# print(a2.dtype)


# # Total Attribute
# # 1 ndim
# # 2 shape
# # 3 size
# # 4 itemsize
# # 5 dtype
# # change data type of already created array

# # astype attribute
# # print(a2.dtype)
# print(a2.astype('int64'))
# print(a2.dtype)


# # mathematical operations on numpy arrays


# # Saler operations
# # a1 = matrix , 2= scaler
# # =>Arthimatic operators
# print(a1*2)  # will multiply the each element with 2
# print(a1/2)  # will divide the each element with 2
# print(a1//2)  # will floor the each element with 2
# print(a1 % 2)  # will modulous the each element with 2
# print(a1+2)  # will additions the each element with 2
# print(a1-2)  # will subtraction the each element with 2
# print(a1**2)  # will power the each element with 2
# # => Logical Operators
# print(a1 ^ 2)  # will XOR the each element with 2
# print(a1.all() and 2)  # will AND the each element with 2
# print(a1.all() or 2)  # will OR the each element with 2
# # => Relational Operators
# print(a1 == 2)  # will check each element if it is equal to 2 return an array
# print(a1 != 2)  # will check each element if it is equal to 2 return an array
# print(a1 >= 2)  # will check each element if it is equal to 2 return an array
# print(a1 <= 2)  # will check each element if it is equal to 2 return an array
# print(a1 < 2)  # will check each element if it is equal to 2 return an array
# print(a1 > 2)  # will check each element if it is equal to 2 return an array

# Vector  Operations
# operation apply between two or more arrays
# note the shape should be same to both the operand arrays in vector operations
# just like matrix
# print(a1)
# print(a2)
# # print(a1*a1)
# print(a1*a1)
# print(a1**a2)
# print(a1+a1)
# print(a1/a2)
# print(a1-a1)


# a1 = a1.reshape(4, 1)
# print(a1*a2)  this will produce Error as the shape is not same
# operands could not be broadcast together with shapes (4,1) (2,4)


# array funtions in numpy
# there are so many array funtions these are the basic array function
# print(a1.sum())
# print(a1.max())
# print(a1.min())
# print(a1.prod())
# print(np.min(a2,axis=0))
# print(np.min(a2,axis=1))


a1 = np.random.random((3, 3))
a1 = np.round(a1*100)
# print(a1)
# print(a1.max())
# print(a1.min())
# print(a1.sum())
# print(a1.prod())
# # min and max from each row
# #  0 = col , 1=row
# print(np.min(a1, axis=1))
# print(np.max(a1, axis=1))

# Statical method
# print(np.mean(a1))  # mean from Whole array elements
# print(np.median(a1))  # median from Whole array elements
# print(np.std(a1))  # standad Deviations
# print(np.var(a1))  # variance
# # print(np.mode(a1))

# # Trignomatric funtions
# print(np.sin(a1))
# print(np.cos(a1))
# print(np.tan(a1))


# dot product funtion


# a1 = np.random.random((3, 4))
# a2 = np.random.random((4, 3))
# a1 = np.round(a1*100)
# a2 = np.round(a2*100)

# # Conditions for dot product
# # no. of col of 1st matrix == no.of row of 2nd matrix
# #  (2,3).(3,2) resultent matrix = (2,2)

# print(np.dot(a1,a2))


# # log
# print(np.log(a1))
# print(np.exp(a1))  # exponential
# # will make round off the no. to the neareset integer like 6.9 = 7 and 6.4 = 6
# print(np.round(np.exp(a1)))
# # floor will round of to the previous nearest integer like floor(6.9) == 6
# print(np.floor(np.exp(a1)))
# # ceil will round of to the next nearest integer like ceil(6.9) == 7
# print(np.ceil(np.exp(a1)))


# Indexing in numpy arrays
# array indexing starts with 0 is positive indexing right to left
# array indexing starts with -1 is negative indexing  left to right
# arr[row,col] for access an element in array

a = np.arange(11)
b = np.arange(1, 26).reshape(5, 5)
# print(a)
# print(b)
# here in numpy the array index or numbering of column and rows start with 0
# print(b[2, 2])
# # here in numpy the array index or numbering of column and rows start with 0
# print(b[0, 4])

# 0 =  row1
# 4 = col5


# Now array indexing for 3D Array
# so  as we know a 3D array or a tensor is a made up of 2d matrix
#  so to access any element in a 3D matrix we should index the Each 2D array in a 3D array that start with 0
# arr3D[indexOf2DArray , indexOfRowOf2DArray,indexOfColOf2DArray]
# after finding the index of 2D array find the index of row of in 2D array in which your element present this index is also start with the 0
# after finding the index of row of  2D array  find the index of Col of in 2D array in which your element present this index is also start with the 0

# lets create a tensor
a = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]],
    [[9, 10],
     [11, 12]]
])
# print(a[0,0,0])
# print(a[1, 1, 1])
# print(a[1,0,1])

# Array slicing
# to fetch more than one item at once use slicing

# array slicing in 1D is like list
# b[start:stop:Jump]
# start = 0 default
# end = end of the array lenth default
# jump = 1 default
# so [::] will return whole array or string or list
# as jump = 1 default so to jump 1 element in list or array we set jump =  2
# array slicing in 2D is
#  b[row slicing, column slicing ]

# points
# in 2D array slicing
# we do something like
# arr[::,::] this will print entire 2D array
# print(b)
# print(b[::])  # similary this print all row means entire 2D array
# print(b[::, ::])  # similary this print all row means entire 2D array
# similary this print all odd rows starting form 0 to end array lenght or last row

# print(b[::2])

# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]
# print (1,5,21,25)
# 12 13 14 15

# print(b[::3, ::4])
# print(b[::3, ::4])
# print(b[2::, 1::])


# Now slicing the  3D arrays
# for slice a 3d array we know that a 3D array is consist a no. of 2D arrays
# arr3D[slic 2D array, slice row ,slice col]
# 3D array

# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]

# print(a)
# print(a[1::3, 1::, 1::]) #[[[8]]]
# print(a[1::3, ::2, 1::2]) #[[[6]]]
# print(a[::, ::2, 1::2]) #[[[6]]]

# negative slicing will reverse the array
# ex
# print(a[::-2])
a = np.arange(11)
# print(a[::-1]) #this code will reverse the linear 1D array or list
# this code will reverse and print skip element the linear 1D array or list
# print(a[::-2])
# print(a[1::-1])  # this code will start from 1 and will reverse
# print(a[5::-1])  # this code will start from 1 and will reverse
# print(a[5::-1])  # this code will start from 1 and will reverse


# def factorial(num):
#     a = np.arange(1, num+1)
#     fac = 1
#     for i in a:
#         fac = fac*i
#     return fac


# c = factorial(10)
# print(c)

# factorial function using numpy arrays

# funtion to reverse a string
# def reverse(string):
# 	return string[::-1]

# a=reverse('krishna')
# print(a)

# iteration


a1 = np.arange(1, 11)
a2 = np.arange(1, 10).reshape(3, 3)
a3 = np.arange(1, 28).reshape(3, 3, 3)
# print(a3)
# print(a2)
# print(a1)

# for i in a1:
#   print(i)


# for i in a2:
#     print(i)


# for i in a3:
#   print(i)

# for i in np.nditer(a3):
# 	print(i)


# transpose
# print(a1.T)
# print(a1.T)
# print(a3.T)


# print((a3.ravel()))


# Stacking  mixing two or more array
# hstack ,vstack
# hstack horizontaly stack array this will change the no.of cols
# vstack vertically stack array this will change the no.of rows

a=np.arange(12).reshape(3,4 )
b=np.arange(12,18).reshape(3,2 )
b2=np.arange(12,24).reshape(3,4 )

# print(np.hstack((a,b)))
# print(np.vstack((a,b2)))



# spliting
# hsplit(array,number of parts) opposite of vstack 
# vsplit(array,number of parts) opposite of  hstack