import numpy as np

# np.array() function

# a = np.array([1, 2, 3, 4])  # this is 1d array or vector
# # -> numpy arrays are fixed size
# # list in python store hetrogenous data (like string float int all at once )
# # list in python is dynamic sized as it can double its size
# # print(a)
# print(type(a))
# for i in a:
#     print(i)


# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])  # this is 2d array or matrix
# print(a)

# # 3D numpy array also called tensor
# # in numpy there can be any no. of dimention made of a array
# a = np.array(
#     [
#         [
#             [
#                 1, 2
#             ], [
#                 3, 4
#             ]
#         ], [
#             [
#                 5, 6
#             ], [
#                 7, 8
#             ]
#         ], [
#             [
#                 9, 10
#             ], [
#                 11, 12
#             ]
#         ]
#     ]
# )
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




