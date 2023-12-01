# import numpy as np

# a = np.full((4,5,5),20)
# a
# array([[[20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20]],

#        [[20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20]],

#        [[20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20]],

#        [[20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20],
#         [20, 20, 20, 20, 20]]])
# a.ndim
# 3
# b = np.ones((3,2))
# b
# array([[1., 1.],
#        [1., 1.],
#        [1., 1.]])
# arr1 = np.zeros(6)
# arr1 # this is a vector
# array([0., 0., 0., 0., 0., 0.])
# arr2 = np.random.randn((3))
# arr2
# array([ 0.93863919,  0.5694029 , -0.75817283])
# arry3 = np.random.random((3, 3))
# arry3 # this is a matrix
# array([[0.53549025, 0.44640519, 0.46577415],
#        [0.54395889, 0.03599633, 0.47180149],
#        [0.25104807, 0.86789006, 0.55288054]])
# arry3.size
# 9
# arr2.size
# 3
# arr2.ndim
# 1
# NB
# Arrays of 1 dim are vectors
# Arrays of 2 dim are matrix
# Arrays of 3 dim are tensor
# Working With Special Values
# x = 0/0
# x
# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# Cell In[25], line 1
# ----> 1 x = 0/0
#       2 x

# ZeroDivisionError: division by zero
# # two special values we'll be dealing with are nan & inf
# # NaN refers to a missing info or an undefined number.
# # inf refers to infinity
# # Nothing is equal to NaN, however something can be equivalent to NaN

# vec1 = np.array([1,-1,0], dtype=np.float16)
# vec1
# array([ 1., -1.,  0.], dtype=float16)
# # access the value of vec1
# vec1[0]
# 1.0
# vec2 = vec1 / 0 # divide vec1 by 0
# vec2
# /var/folders/4r/3_6gh8rj44g43v_wlyprm7h40000gn/T/ipykernel_14216/682713793.py:1: RuntimeWarning: divide by zero encountered in divide
#   vec2 = vec1 / 0 # divide vec1 by 0
# /var/folders/4r/3_6gh8rj44g43v_wlyprm7h40000gn/T/ipykernel_14216/682713793.py:1: RuntimeWarning: invalid value encountered in divide
#   vec2 = vec1 / 0 # divide vec1 by 0
# array([ inf, -inf,  nan], dtype=float16)
# # Detecting the special values

# for i in vec2:
#     print(f"Number to evaluate: {i}")
#     print("########")
#     print(f"Inf: {str(i == np.inf)}")
#     print(f"Neg Inf: {str(i == -np.inf)}")
#     print(f"NaN: {str(i == np.nan)}") # this is wrong!!!
#     print()
# Number to evaluate: inf
# ########
# Inf: True
# Neg Inf: False
# NaN: False

# Number to evaluate: -inf
# ########
# Inf: False
# Neg Inf: True
# NaN: False

# Number to evaluate: nan
# ########
# Inf: False
# Neg Inf: False
# NaN: False

# # Nothing is equal to NaN, however something can be Equivalent to NaN

# x = ''
# x
# ''
# y == ''
# y
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# Cell In[33], line 1
# ----> 1 y == ''
#       2 y

# NameError: name 'y' is not defined
# type(y)
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# Cell In[37], line 1
# ----> 1 type(y)

# NameError: name 'y' is not defined
# a = 3
# b == a
# b == 33

# a
# 3
# b
# array([[1., 1.],
#        [1., 1.],
#        [1., 1.]])
# a == 3
# True
# c = 6 - 3
# a == c
# True
# nan = 1

# nan
# 1
# h = 'nothing'
# i = 'something'

# h = nan
# i == nan
# False
# for i in vec2:
#     print(f"Number to evaluate: {i}")
#     print("########")
#     print(f"Inf: {str(i == np.inf)}")
#     print(f"Neg Inf: {str(i == -np.inf)}")
#     print(f"NaN: {str(np.isnan(i))}") # this is correct syntax
#     print()
# Number to evaluate: inf
# ########
# Inf: True
# Neg Inf: False
# NaN: False

# Number to evaluate: -inf
# ########
# Inf: False
# Neg Inf: True
# NaN: False

# Number to evaluate: nan
# ########
# Inf: False
# Neg Inf: False
# NaN: True

# # detect infinite values 
# for i in vec2:
#     print(f"Number to evaluate: {i}")
#     print("########")
#     print(f"Is Finite Value: {str(np.isfinite(i))}") # checks if i is a finite value
#     print(f"Is Infinite Value: {str(np.isinf(i))}") # checks if i is an infinite value 
#     print()
# Number to evaluate: inf
# ########
# Is Finite Value: False
# Is Infinite Value: True

# Number to evaluate: -inf
# ########
# Is Finite Value: False
# Is Infinite Value: True

# Number to evaluate: nan
# ########
# Is Finite Value: False
# Is Infinite Value: False

# vec2[0]
# inf
# vec2[1]
# -inf
# vec2[2]
# nan
# 5 ** vec2[0]
# inf
# 5 ** vec2[1]
# 0.0
# 5 ** vec2[2]
# nan
# vec3 = np.array([9999], dtype='float')
# vec3
# array([9999.])
# vec3[0]
# 9999.0
# vec3[0] ** vec3[0] # we have an infinite value cos the program is very very large 
# /var/folders/4r/3_6gh8rj44g43v_wlyprm7h40000gn/T/ipykernel_14216/3555918632.py:1: RuntimeWarning: overflow encountered in double_scalars
#   vec3[0] ** vec3[0]
# inf
# a = 9999
# a ** a
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# File ~/anaconda3/lib/python3.10/site-packages/IPython/core/formatters.py:706, in PlainTextFormatter.__call__(self, obj)
#     699 stream = StringIO()
#     700 printer = pretty.RepresentationPrinter(stream, self.verbose,
#     701     self.max_width, self.newline,
#     702     max_seq_length=self.max_seq_length,
#     703     singleton_pprinters=self.singleton_printers,
#     704     type_pprinters=self.type_printers,
#     705     deferred_pprinters=self.deferred_printers)
# --> 706 printer.pretty(obj)
#     707 printer.flush()
#     708 return stream.getvalue()

# File ~/anaconda3/lib/python3.10/site-packages/IPython/lib/pretty.py:393, in RepresentationPrinter.pretty(self, obj)
#     390 for cls in _get_mro(obj_class):
#     391     if cls in self.type_pprinters:
#     392         # printer registered in self.type_pprinters
# --> 393         return self.type_pprinters[cls](obj, self, cycle)
#     394     else:
#     395         # deferred printer
#     396         printer = self._in_deferred_types(cls)

# File ~/anaconda3/lib/python3.10/site-packages/IPython/lib/pretty.py:778, in _repr_pprint(obj, p, cycle)
#     776 """A pprint that just redirects to the normal repr function."""
#     777 # Find newlines and replace them with p.break_()
# --> 778 output = repr(obj)
#     779 lines = output.splitlines()
#     780 with p.group():

# ValueError: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
# vec4 = np.ones(7)
# vec4
# array([1., 1., 1., 1., 1., 1., 1.])
# vec4.dtype
# dtype('float64')
# vec4.dtype = 'int64' # or vec4.dtype = int ; this is a wrong way of casting/converting 
# # your np data types. you'll have garbage values i.e. random values from memory.
# vec4.dtype
# dtype('int64')
# vec4
# array([4607182418800017408, 4607182418800017408, 4607182418800017408,
#        4607182418800017408, 4607182418800017408, 4607182418800017408,
#        4607182418800017408])
# vec4
# array([4607182418800017408, 4607182418800017408, 4607182418800017408,
#        4607182418800017408, 4607182418800017408, 4607182418800017408,
#        4607182418800017408])
# vec4 = np.ones(7)
# vec4
# array([1., 1., 1., 1., 1., 1., 1.])
# # this is the right/appropriate way to do it
# vec4 = np.array(vec4, dtype='int64')
# vec4.dtype
# dtype('int64')
# vec4
# array([1, 1, 1, 1, 1, 1, 1])
# # assign a nan to the array
# vec4 = np.ones(7)
# vec4[1] = np.nan
# vec4
# array([ 1., nan,  1.,  1.,  1.,  1.,  1.])
# np.sum(vec4) # sum everything together
# nan
# np.nansum(vec4) # this removes the nan then sums the elements 
# 6.0
# str_vec = np.array([['Judge', 'Goat', 'Saudi'], ['Spurs', 'Bottlers', 'Reds']])
# str_vec.dtype
# dtype('<U8')
# str_vec.size
# 6
# str_vec.shape
# (2, 3)
# str_vec.ndim
# 2
# str_vec
# array([['Judge', 'Goat', 'Saudi'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U8')
# str_vec[1][2]
# 'Reds'
# str_vec[0][1][2]
# 'a'
# str_vec[0]
# array(['Judge', 'Goat', 'Saudi'], dtype='<U8')
# str_vec[0][1][2][3]
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# Cell In[83], line 1
# ----> 1 str_vec[0][1][2][3]

# IndexError: string index out of range
# # what does the dtype mean and how to work with it?
# str_vec
# array([['Judge', 'Goat', 'Saudi'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U8')
# str_vec[0]
# array(['Judge', 'Goat', 'Saudi'], dtype='<U8')
# str_vec[1]
# array(['Spurs', 'Bottlers', 'Reds'], dtype='<U8')
# str_vec[0][0]
# 'Judge'
# str_vec[0][0][2]
# 'd'
# str_vec.dtype
# dtype('<U8')
# str_vec[0][2] =  'Burkinafaso'
# str_vec
# array([['Judge', 'Goat', 'Burkinaf'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U8')
# str_vec = np.array(str_vec, dtype='<U16')
# str_vec
# array([['Judge', 'Goat', 'Burkinaf'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U16')
# str_vec[0][2] =  'Burkinafaso'
# str_vec
# array([['Judge', 'Goat', 'Burkinafaso'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U16')
# str_vec
# array([['Judge', 'Goat', 'Burkinafaso'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U16')
# Copy the array obj
# # copy the array
# new_str_vec = str_vec
# new_str_vec
# array([['Judge', 'Goat', 'Burkinafaso'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U16')
# str_vec[0][1] = np.nan
# str_vec
# array([['Judge', 'nan', 'Burkinafaso'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U16')
# new_str_vec
# array([['Judge', 'nan', 'Burkinafaso'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U16')
# new_arry = str_vec.copy() # the copy mtd creates a new instance independent of the parent array
# new_arry
# array([['Judge', 'nan', 'Burkinafaso'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U16')
# str_vec[1][2] = np.nan
# str_vec
# array([['Judge', 'nan', 'Burkinafaso'],
#        ['Spurs', 'Bottlers', 'nan']], dtype='<U16')
# new_arry
# array([['Judge', 'nan', 'Burkinafaso'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U16')
# Save the array obj
# # To save the array obj  
# '''
# The ffg syntax are used to save an array in np
# save(file, arr), saves in a npy format.
# savez(file, arr), saves in npz format i.e. a compressed file
# savetxt(file, arr, delimeter), saves in a text file or csv file (when using the delimeter arg)
# arr.tofile(file, sep), saves in a file with the arr elements separated by comma
# '''

# file = '/Users/damilare/Documents/ingryd/datasets/numpy_data/new_array.npy'


# new_arry
# array([['Judge', 'nan', 'Burkinafaso'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U16')
# np.save(file, new_arry)
# # load the array from the npy file in np
# get_arry = np.load(file)
# get_arry
# array([['Judge', 'nan', 'Burkinafaso'],
#        ['Spurs', 'Bottlers', 'Reds']], dtype='<U16')
# # using the savetxt mtd

# # declare file path
# file2 = '/Users/damilare/Documents/ingryd/datasets/numpy_data/another_array.csv'
# np.savetxt(file2, new_arry, delimiter=",") # separate the values by comma
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# File ~/anaconda3/lib/python3.10/site-packages/numpy/lib/npyio.py:1590, in savetxt(fname, X, fmt, delimiter, newline, header, footer, comments, encoding)
#    1589 try:
# -> 1590     v = format % tuple(row) + newline
#    1591 except TypeError as e:

# TypeError: must be real number, not numpy.str_

# The above exception was the direct cause of the following exception:

# TypeError                                 Traceback (most recent call last)
# Cell In[117], line 1
# ----> 1 np.savetxt(file2, new_arry, delimiter=",")

# File <__array_function__ internals>:180, in savetxt(*args, **kwargs)

# File ~/anaconda3/lib/python3.10/site-packages/numpy/lib/npyio.py:1592, in savetxt(fname, X, fmt, delimiter, newline, header, footer, comments, encoding)
#    1590             v = format % tuple(row) + newline
#    1591         except TypeError as e:
# -> 1592             raise TypeError("Mismatch between array dtype ('%s') and "
#    1593                             "format specifier ('%s')"
#    1594                             % (str(X.dtype), format)) from e
#    1595         fh.write(v)
#    1597 if len(footer) > 0:

# TypeError: Mismatch between array dtype ('<U16') and format specifier ('%.18e,%.18e,%.18e')
# new_arry.ndim
# 2
# new_arry2 = np.random.random((3,4)) # the savetxt mtd works with real numbers and not strings
# new_arry2
# array([[0.01842995, 0.16727138, 0.52458089, 0.95673066],
#        [0.82820891, 0.05670513, 0.59104059, 0.90642109],
#        [0.806815  , 0.30562813, 0.15095961, 0.91586111]])
# np.savetxt(file2, new_arry2, delimiter=",")
# # read the another_array.csv file

# get_csv_file = np.load(file2)
# get_csv_file
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Cell In[122], line 3
#       1 # read the another_array.csv file
# ----> 3 get_csv_file = np.load(file2)
#       4 get_csv_file

# File ~/anaconda3/lib/python3.10/site-packages/numpy/lib/npyio.py:438, in load(file, mmap_mode, allow_pickle, fix_imports, encoding, max_header_size)
#     435 else:
#     436     # Try a pickle
#     437     if not allow_pickle:
# --> 438         raise ValueError("Cannot load file containing pickled data "
#     439                          "when allow_pickle=False")
#     440     try:
#     441         return pickle.load(fid, **pickle_kwargs)

# ValueError: Cannot load file containing pickled data when allow_pickle=False
# get_csv_file = np.load(file2, allow_pickle=True)
# get_csv_file # we can't use the load mtd to open a csv/txt file
# ---------------------------------------------------------------------------
# UnpicklingError                           Traceback (most recent call last)
# File ~/anaconda3/lib/python3.10/site-packages/numpy/lib/npyio.py:441, in load(file, mmap_mode, allow_pickle, fix_imports, encoding, max_header_size)
#     440 try:
# --> 441     return pickle.load(fid, **pickle_kwargs)
#     442 except Exception as e:

# UnpicklingError: could not find MARK

# The above exception was the direct cause of the following exception:

# UnpicklingError                           Traceback (most recent call last)
# Cell In[123], line 1
# ----> 1 get_csv_file = np.load(file2, allow_pickle=True)
#       2 get_csv_file

# File ~/anaconda3/lib/python3.10/site-packages/numpy/lib/npyio.py:443, in load(file, mmap_mode, allow_pickle, fix_imports, encoding, max_header_size)
#     441     return pickle.load(fid, **pickle_kwargs)
#     442 except Exception as e:
# --> 443     raise pickle.UnpicklingError(
#     444         f"Failed to interpret file {file!r} as a pickle") from e

# UnpicklingError: Failed to interpret file '/Users/damilare/Documents/ingryd/datasets/numpy_data/another_array.csv' as a pickle
# # let's use the open func to read the csv file
# get_csv_file = open(file2, 'r')
# get_csv_file
# <_io.TextIOWrapper name='/Users/damilare/Documents/ingryd/datasets/numpy_data/another_array.csv' mode='r' encoding='UTF-8'>
# get_csv_file.read()
# '1.842995381228673679e-02,1.672713832088749131e-01,5.245808899561253957e-01,9.567306592828144218e-01\n8.282089075405481005e-01,5.670513082269779126e-02,5.910405949723169794e-01,9.064210937126564449e-01\n8.068149984836069377e-01,3.056281348720055746e-01,1.509596063551595924e-01,9.158611103135182452e-01\n'
# get_csv_file.readlines()
# []
# get_csv_file.close()
# get_csv_file2 = np.loadtxt(file2)
# get_csv_file2
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Cell In[129], line 1
# ----> 1 get_csv_file2 = np.loadtxt(file2)
#       2 get_csv_file2

# File ~/anaconda3/lib/python3.10/site-packages/numpy/lib/npyio.py:1338, in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin, encoding, max_rows, quotechar, like)
#    1335 if isinstance(delimiter, bytes):
#    1336     delimiter = delimiter.decode('latin1')
# -> 1338 arr = _read(fname, dtype=dtype, comment=comment, delimiter=delimiter,
#    1339             converters=converters, skiplines=skiprows, usecols=usecols,
#    1340             unpack=unpack, ndmin=ndmin, encoding=encoding,
#    1341             max_rows=max_rows, quote=quotechar)
#    1343 return arr

# File ~/anaconda3/lib/python3.10/site-packages/numpy/lib/npyio.py:999, in _read(fname, delimiter, comment, quote, imaginary_unit, usecols, skiplines, max_rows, converters, ndmin, unpack, dtype, encoding)
#     996     data = _preprocess_comments(data, comments, encoding)
#     998 if read_dtype_via_object_chunks is None:
# --> 999     arr = _load_from_filelike(
#    1000         data, delimiter=delimiter, comment=comment, quote=quote,
#    1001         imaginary_unit=imaginary_unit,
#    1002         usecols=usecols, skiplines=skiplines, max_rows=max_rows,
#    1003         converters=converters, dtype=dtype,
#    1004         encoding=encoding, filelike=filelike,
#    1005         byte_converters=byte_converters)
#    1007 else:
#    1008     # This branch reads the file into chunks of object arrays and then
#    1009     # casts them to the desired actual dtype.  This ensures correct
#    1010     # string-length and datetime-unit discovery (like `arr.astype()`).
#    1011     # Due to chunking, certain error reports are less clear, currently.
#    1012     if filelike:

# ValueError: could not convert string '1.842995381228673679e-02,1.672713832088749131e-01,5.245808899561253957e-01,9.567306592828144218e-01 to float64 at row 0, column 1.
# get_csv_file = open(file2, 'r')
# get_csv_file
# <_io.TextIOWrapper name='/Users/damilare/Documents/ingryd/datasets/numpy_data/another_array.csv' mode='r' encoding='UTF-8'>
# [data for data in get_csv_file]
# ['1.842995381228673679e-02,1.672713832088749131e-01,5.245808899561253957e-01,9.567306592828144218e-01\n',
#  '8.282089075405481005e-01,5.670513082269779126e-02,5.910405949723169794e-01,9.064210937126564449e-01\n',
#  '8.068149984836069377e-01,3.056281348720055746e-01,1.509596063551595924e-01,9.158611103135182452e-01\n']
# get_csv_file = open(file2, 'r')
# get_csv_file

# for data in get_csv_file:
#     print(data, '=>', type(data))
# 1.842995381228673679e-02,1.672713832088749131e-01,5.245808899561253957e-01,9.567306592828144218e-01
#  => <class 'str'>
# 8.282089075405481005e-01,5.670513082269779126e-02,5.910405949723169794e-01,9.064210937126564449e-01
#  => <class 'str'>
# 8.068149984836069377e-01,3.056281348720055746e-01,1.509596063551595924e-01,9.158611103135182452e-01
#  => <class 'str'>
# get_csv_file2 = np.loadtxt(file2, delimiter=',')
# get_csv_file2
# array([[0.01842995, 0.16727138, 0.52458089, 0.95673066],
#        [0.82820891, 0.05670513, 0.59104059, 0.90642109],
#        [0.806815  , 0.30562813, 0.15095961, 0.91586111]])
# Array Slicing
# The following notes should be remembered when working with NP array slicing

# The colon works with arrays just like with Lists, however, we're dealing with at least 1d array.
# Select all rows from a to b and all columns from c to d for a 2d array 'arry' with arry[a:b, c:d].
# Select every row in a dimension with : e.g. arry[a:b, :].
# Select all rows up to b with arry[:b, :].
# Select all rows after and including row a with arry[a:]
# A second colon can be used to go by increment/step e.g. arry[a:b:i, :] or arry[a:b:(-1), :] for a -ve slicing or to go in the reverse direction.
# # ex

# arry1 = np.array([
#     [
#         ['John', 'Doe', 'Tobe'],
#         ['Franca', 'Funsho', 'Gideon'],
#         ['Ire', 'Yemi', 'Wakil']
#     ],
#     [
#         ['Dara', 'Joe', 'Dona'],
#         ['Feranmi', 'Abubakar', 'Sulaimon'],
#         ['Franklin', 'Bola', 'Peter']
#     ],
#     [
#         ['Rasheed', 'Semande', 'Caleb'],
#         ['Tunde', 'Timson', 'Kunle'],
#         ['Joan', 'Jamiu', 'Patrick']
#     ]
    
# ])

# arry1
# array([[['John', 'Doe', 'Tobe'],
#         ['Franca', 'Funsho', 'Gideon'],
#         ['Ire', 'Yemi', 'Wakil']],

#        [['Dara', 'Joe', 'Dona'],
#         ['Feranmi', 'Abubakar', 'Sulaimon'],
#         ['Franklin', 'Bola', 'Peter']],

#        [['Rasheed', 'Semande', 'Caleb'],
#         ['Tunde', 'Timson', 'Kunle'],
#         ['Joan', 'Jamiu', 'Patrick']]], dtype='<U8')
# arry1.shape
# (3, 3, 3)
# arry1.size
# 27
# arry1.ndim
# 3
# # copy the array
# arry2 = arry1[:, :,0].copy()
# arry2
# array([['John', 'Franca', 'Ire'],
#        ['Dara', 'Feranmi', 'Franklin'],
#        ['Rasheed', 'Tunde', 'Joan']], dtype='<U8')
# # what did we copy?
# '''
# loop thru the rows, go thru the columns  
# '''
# arry1[0]
# array([['John', 'Doe', 'Tobe'],
#        ['Franca', 'Funsho', 'Gideon'],
#        ['Ire', 'Yemi', 'Wakil']], dtype='<U8')
# arry1[1]
# array([['Dara', 'Joe', 'Dona'],
#        ['Feranmi', 'Abubakar', 'Sulaimon'],
#        ['Franklin', 'Bola', 'Peter']], dtype='<U8')
# arry1[2]
# array([['Rasheed', 'Semande', 'Caleb'],
#        ['Tunde', 'Timson', 'Kunle'],
#        ['Joan', 'Jamiu', 'Patrick']], dtype='<U8')
# Wk7_1.3 - Slicing & Indexing Cont
# arry1[:2]
# array([[['John', 'Doe', 'Tobe'],
#         ['Franca', 'Funsho', 'Gideon'],
#         ['Ire', 'Yemi', 'Wakil']],

#        [['Dara', 'Joe', 'Dona'],
#         ['Feranmi', 'Abubakar', 'Sulaimon'],
#         ['Franklin', 'Bola', 'Peter']]], dtype='<U8')
# arry1[:2, :2]
# array([[['John', 'Doe', 'Tobe'],
#         ['Franca', 'Funsho', 'Gideon']],

#        [['Dara', 'Joe', 'Dona'],
#         ['Feranmi', 'Abubakar', 'Sulaimon']]], dtype='<U8')
# arry1[:2, :2, :2]
# array([[['John', 'Doe'],
#         ['Franca', 'Funsho']],

#        [['Dara', 'Joe'],
#         ['Feranmi', 'Abubakar']]], dtype='<U8')
# arry1[:0, :1, :2]
# array([], shape=(0, 1, 2), dtype='<U8')
# arry1[0:, :1, :2]
# array([[['John', 'Doe']],

#        [['Dara', 'Joe']],

#        [['Rasheed', 'Semande']]], dtype='<U8')
# arry1[::-1, :]
# array([[['Rasheed', 'Semande', 'Caleb'],
#         ['Tunde', 'Timson', 'Kunle'],
#         ['Joan', 'Jamiu', 'Patrick']],

#        [['Dara', 'Joe', 'Dona'],
#         ['Feranmi', 'Abubakar', 'Sulaimon'],
#         ['Franklin', 'Bola', 'Peter']],

#        [['John', 'Doe', 'Tobe'],
#         ['Franca', 'Funsho', 'Gideon'],
#         ['Ire', 'Yemi', 'Wakil']]], dtype='<U8')
# arry1[::-1, :2]
# array([[['Rasheed', 'Semande', 'Caleb'],
#         ['Tunde', 'Timson', 'Kunle']],

#        [['Dara', 'Joe', 'Dona'],
#         ['Feranmi', 'Abubakar', 'Sulaimon']],

#        [['John', 'Doe', 'Tobe'],
#         ['Franca', 'Funsho', 'Gideon']]], dtype='<U8')
# Advanced Indexing
# arry1 # this returns the whole array
# array([[['John', 'Doe', 'Tobe'],
#         ['Franca', 'Funsho', 'Gideon'],
#         ['Ire', 'Yemi', 'Wakil']],

#        [['Dara', 'Joe', 'Dona'],
#         ['Feranmi', 'Abubakar', 'Sulaimon'],
#         ['Franklin', 'Bola', 'Peter']],

#        [['Rasheed', 'Semande', 'Caleb'],
#         ['Tunde', 'Timson', 'Kunle'],
#         ['Joan', 'Jamiu', 'Patrick']]], dtype='<U8')
# # get all the data that are not Caleb
# print(arry1[arry1 != 'Caleb'])
# ['John' 'Doe' 'Tobe' 'Franca' 'Funsho' 'Gideon' 'Ire' 'Yemi' 'Wakil'
#  'Dara' 'Joe' 'Dona' 'Feranmi' 'Abubakar' 'Sulaimon' 'Franklin' 'Bola'
#  'Peter' 'Rasheed' 'Semande' 'Tunde' 'Timson' 'Kunle' 'Joan' 'Jamiu'
#  'Patrick']
# print(arry1 != 'Caleb') # this returned a list of lists
# [[[ True  True  True]
#   [ True  True  True]
#   [ True  True  True]]

#  [[ True  True  True]
#   [ True  True  True]
#   [ True  True  True]]

#  [[ True  True False]
#   [ True  True  True]
#   [ True  True  True]]]
# arry1 != 'Caleb' # this returned an array of list of lists
# array([[[ True,  True,  True],
#         [ True,  True,  True],
#         [ True,  True,  True]],

#        [[ True,  True,  True],
#         [ True,  True,  True],
#         [ True,  True,  True]],

#        [[ True,  True, False],
#         [ True,  True,  True],
#         [ True,  True,  True]]])
# # get the data via an array of index

# # Row indices
# idx0 = np.array([
#             [
#                 [0,0],[0,0]
#             ], 
#             [
#                 [2,2], [2,2]
#             ]
#         ])
# idx0
# array([[[0, 0],
#         [0, 0]],

#        [[2, 2],
#         [2, 2]]])
# # Column indices
# idx1 = np.array([
#             [
#                 [0,2],[0,2]
#             ],
#             [
#                 [0,2],[0,2]
#             ]
#         ])
# idx1
# array([[[0, 2],
#         [0, 2]],

#        [[0, 2],
#         [0, 2]]])
# # Depth indices
# idx2 = np.array([
#             [
#                 [0,0],[2,2]
#             ],
#             [
#                 [0,0],[2,2]
#             ]
#         ])
# idx2
# array([[[0, 0],
#         [2, 2]],

#        [[0, 0],
#         [2, 2]]])
# arry1[idx0, idx1, idx2]
# array([[['John', 'Ire'],
#         ['Tobe', 'Wakil']],

#        [['Rasheed', 'Joan'],
#         ['Caleb', 'Patrick']]], dtype='<U8')
# arry1
# array([[['John', 'Doe', 'Tobe'],
#         ['Franca', 'Funsho', 'Gideon'],
#         ['Ire', 'Yemi', 'Wakil']],

#        [['Dara', 'Joe', 'Dona'],
#         ['Feranmi', 'Abubakar', 'Sulaimon'],
#         ['Franklin', 'Bola', 'Peter']],

#        [['Rasheed', 'Semande', 'Caleb'],
#         ['Tunde', 'Timson', 'Kunle'],
#         ['Joan', 'Jamiu', 'Patrick']]], dtype='<U8')
# arry1.ndim
# 3
# Array Expansion
# # you can use the concatenate mtd to join two arrays together
# arry1
# array([[['John', 'Doe', 'Tobe'],
#         ['Franca', 'Funsho', 'Gideon'],
#         ['Ire', 'Yemi', 'Wakil']],

#        [['Dara', 'Joe', 'Dona'],
#         ['Feranmi', 'Abubakar', 'Sulaimon'],
#         ['Franklin', 'Bola', 'Peter']],

#        [['Rasheed', 'Semande', 'Caleb'],
#         ['Tunde', 'Timson', 'Kunle'],
#         ['Joan', 'Jamiu', 'Patrick']]], dtype='<U8')
# new_arry1 = arry1[0]
# new_arry1
# array([['John', 'Doe', 'Tobe'],
#        ['Franca', 'Funsho', 'Gideon'],
#        ['Ire', 'Yemi', 'Wakil']], dtype='<U8')
# new_arry1.ndim
# 2
# new_arry2 = arry1[1]
# new_arry2
# array([['Dara', 'Joe', 'Dona'],
#        ['Feranmi', 'Abubakar', 'Sulaimon'],
#        ['Franklin', 'Bola', 'Peter']], dtype='<U8')
# new_arry2.shape
# (3, 3)
# new_arry1.shape
# (3, 3)
# joined_arrys = np.concatenate((new_arry1, new_arry2))
# joined_arrys
# array([['John', 'Doe', 'Tobe'],
#        ['Franca', 'Funsho', 'Gideon'],
#        ['Ire', 'Yemi', 'Wakil'],
#        ['Dara', 'Joe', 'Dona'],
#        ['Feranmi', 'Abubakar', 'Sulaimon'],
#        ['Franklin', 'Bola', 'Peter']], dtype='<U8')
# joined_arrys.shape
# (6, 3)
# joined_arrys.ndim
# 2
# # the syntax for the concatenate is np.concatenate((arr1, arr2), axis=n) where n = the dimensions
# first_arry = np.array([[1,3], [5,7]])
# sec_arry = np.array([[2,4]]) # the extra sq brac makes it a 2d

# first_arry.shape
# (2, 2)
# sec_arry.shape
# (1, 2)
# print(f'first array dim => {first_arry.ndim}')
# print(f'second array dim => {sec_arry.ndim}')
# first array dim => 2
# second array dim => 2
# combined_arrys = np.concatenate((first_arry, sec_arry))
# combined_arrys
# array([[1, 3],
#        [5, 7],
#        [2, 4]])
# combined_arrys_axis_0 = np.concatenate((first_arry, sec_arry), axis=0)
# combined_arrys_axis_0 # the axis are zero by default
# array([[1, 3],
#        [5, 7],
#        [2, 4]])
# combined_arrys_axis_1 = np.concatenate((first_arry, sec_arry), axis=1)
# combined_arrys_axis_1
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Cell In[221], line 1
# ----> 1 combined_arrys_axis_1 = np.concatenate((first_arry, sec_arry), axis=1)
#       2 combined_arrys_axis_1

# File <__array_function__ internals>:180, in concatenate(*args, **kwargs)

# ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 1
# # Ex2 on Concatenation
# xarry = np.array([
#     [
#         [0,1],
#         [2,3]
#     ],
#     [
#         [4,5],
#         [6,7]
#     ]
# ])


# yarry = np.array([
#     [
#         [10,11],
#         [12,13]
#     ],
#     [
#         [14,15],
#         [16,17]
#     ]
# ])

# print('Getting the arrays...\n')
# print('X ARRAYS')
# print(xarry)
# print('\nY ARRAYS')
# print(yarry)
# Getting the arrays...

# X ARRAYS
# [[[0 1]
#   [2 3]]

#  [[4 5]
#   [6 7]]]

# Y ARRAYS
# [[[10 11]
#   [12 13]]

#  [[14 15]
#   [16 17]]]
# print(f'x array dim => {xarry.ndim}')
# print(f'y array dim => {yarry.ndim}')
# x array dim => 3
# y array dim => 3
# print(f'x array shapes => {xarry.shape}')
# print(f'y array shapes => {yarry.shape}')
# x array shapes => (2, 2, 2)
# y array shapes => (2, 2, 2)
# # Start with axis 0
# axes0arrys = np.concatenate((xarry, yarry), 0) # putting the arg 0 == saying axis = 0
# axes0arrys
# array([[[ 0,  1],
#         [ 2,  3]],

#        [[ 4,  5],
#         [ 6,  7]],

#        [[10, 11],
#         [12, 13]],

#        [[14, 15],
#         [16, 17]]])
# # Try for axis = 1
# axes1arrys = np.concatenate((xarry, yarry), 1) # putting the arg 1 == saying axis = 1
# axes1arrys
# array([[[ 0,  1],
#         [ 2,  3],
#         [10, 11],
#         [12, 13]],

#        [[ 4,  5],
#         [ 6,  7],
#         [14, 15],
#         [16, 17]]])
# # ([x0,x1],[y0,y1]) => axis = 0
# # ([x0,y0], [x1,y1]) => axis = 1
# print(f'axis 0 array shapes => {axes0arrys.shape}')
# print(f'axis 1 array shapes => {axes1arrys.shape}')
# axis 0 array shapes => (4, 2, 2)
# axis 1 array shapes => (2, 4, 2)
# print(f'axis 0 array dim => {axes0arrys.ndim}')
# print(f'axis 1 array dim => {axes1arrys.ndim}')
# axis 0 array dim => 3
# axis 1 array dim => 3
# # Try fo axis = 2
# axes2arrys = np.concatenate((xarry, yarry), axis=2) # putting the arg 2 == saying axis = 2
# axes2arrys
# array([[[ 0,  1, 10, 11],
#         [ 2,  3, 12, 13]],

#        [[ 4,  5, 14, 15],
#         [ 6,  7, 16, 17]]])
# axes0arrys # to compare with the default concatenation
# array([[[ 0,  1],
#         [ 2,  3]],

#        [[ 4,  5],
#         [ 6,  7]],

#        [[10, 11],
#         [12, 13]],

#        [[14, 15],
#         [16, 17]]])
# axes2arrys.shape
# (2, 2, 4)
# # Try fo axis = None
# axes2arrys = np.concatenate((xarry, yarry), axis= None) # putting the arg None == saying axis = None
# axes2arrys # this flattens the array.
# array([ 0,  1,  2,  3,  4,  5,  6,  7, 10, 11, 12, 13, 14, 15, 16, 17])
 