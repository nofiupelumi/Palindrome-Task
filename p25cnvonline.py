# # What is NumPy?
# # It's a library for numerical and scientific computations in Python.
# # Characteristics of NumPy
# # It consists of ndarrays i.e. n-dimensional arrays
# # It can be used for some advanced mathematical operations such as statistical operation, algebra, matrices, etc
# # The elements in a np array should be a homogeneous data type
# # The sizes of an np array is static unlike lists data structure


# import numpy as np

# # create an array obj
# array = np.array([1,2,3,4,5,6,7,8,9,10])
# array


# What is NumPy?
# It's a library for numerical and scientific computations in Python.
# Characteristics of NumPy
# It consists of ndarrays i.e. n-dimensional arrays
# It can be used for some advanced mathematical operations such as statistical operation, algebra, matrices, etc
# The elements in a np array should be a homogeneous data type
# The sizes of an np array is static unlike lists data structure
# import numpy as np

# # create an array obj
# array = np.array([1,2,3,4,5,6,7,8,9,10])
# array
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
# # get the type of the array obj
# type(array)
# numpy.ndarray
# # get the dimension of the array obj
# array.ndim
# 1
# # get the shape of the array obj
# array.shape
# (10,)
# # get the size of the array obj
# array.size
# 10
# # get the type of elements in the array obj
# array.dtype
# dtype('int64')
# # create a 2d array 
# array_2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# array_2
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10]])
# # get the type of the array obj
# type(array_2)
# numpy.ndarray
# # get the dimension of the array obj
# array_2.ndim
# 2
# # get the shape of the array obj
# array_2.shape
# (2, 5)
# # get the size of the array obj
# array_2.size
# 10
# array_3 = np.array([[1,3,5,7], [9,11,13,15], [17,19,21,23]], dtype='float')
# array_3
# array([[ 1.,  3.,  5.,  7.],
#        [ 9., 11., 13., 15.],
#        [17., 19., 21., 23.]])
# # get the type of elements in the array obj
# array_3.dtype
# dtype('float64')
# # get the shape of the array obj
# array_3.shape
# (3, 4)
# # get the dimension of the array obj
# array_3.ndim
# 2
# # Create a 3D array obj
# array_4 = np.array([
#     [
#         [1,2,3,1],
#         [4,5,6,2]
#     ],
#     [
#         [7,8,9,3],
#         [10,11,12,4]
#     ],
#     [
#         [17,18,19,5],
#         [110,111,112,6]
#     ],
#     [
#         [170,180,190,50],
#         [1100,1110,1120,60]
#     ]
# ])
# # get the shape of the array obj
# array_4.shape
# (4, 2, 4)
# # get the dimension of the array obj
# array_4.ndim
# 3
# array_4.size
# 32
# # You can create your np arrays without explicitly putting the numbers there
# array_z = np.zeros(5)
# array_z
# array([0., 0., 0., 0., 0.])
# array_z.dtype
# dtype('float64')
# array_z.ndim
# 1
# array_zx = np.zeros((5,6), dtype="int")
# array_zx.shape
# (5, 6)
# array_zx
# array([[0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]])
# array_zx.dtype
# dtype('int64')
# array_o = np.ones(5)
# array_o
# array([1., 1., 1., 1., 1.])
# array_ox = np.ones((3,3,4), dtype='int') # note that the kwargs comes after the positional arg
# array_ox
# array([[[1, 1, 1, 1],
#         [1, 1, 1, 1],
#         [1, 1, 1, 1]],

#        [[1, 1, 1, 1],
#         [1, 1, 1, 1],
#         [1, 1, 1, 1]],

#        [[1, 1, 1, 1],
#         [1, 1, 1, 1],
#         [1, 1, 1, 1]]])
# array_ox.size
# 36
# array_ox.shape
# (3, 3, 4)
# array_ox.ndim

# array_ox.dtype
# dtype('int64')
# array_ox.ndim
# 3
# array_f = np.full((3,7), 15)
# array_f
# array([[15, 15, 15, 15, 15, 15, 15],
#        [15, 15, 15, 15, 15, 15, 15],
#        [15, 15, 15, 15, 15, 15, 15]])
# array_f.shape
# (3, 7)
# array_r = np.random.random((3,2))
# array_r
# array([[0.42181997, 0.75819656],
#        [0.03235316, 0.1324526 ],
#        [0.36805606, 0.33592894]])
 