# import numpy as np
# import pandas as pd

# dataset = '/Users/damilare/Documents/ingryd/datasets/telecom_churn.csv'

# # set the decimal no to 2dp
# pd.set_option("display.precision", 2)

# df = pd.read_csv(dataset)
# df.head()
# State	Account length	Area code	International plan	Voice mail plan	Number vmail messages	Total day minutes	Total day calls	Total day charge	Total eve minutes	Total eve calls	Total eve charge	Total night minutes	Total night calls	Total night charge	Total intl minutes	Total intl calls	Total intl charge	Customer service calls	Churn
# 0	KS	128	415	No	Yes	25	265.1	110	45.07	197.4	99	16.78	244.7	91	11.01	10.0	3	2.70	1	False
# 1	OH	107	415	No	Yes	26	161.6	123	27.47	195.5	103	16.62	254.4	103	11.45	13.7	3	3.70	1	False
# 2	NJ	137	415	No	No	0	243.4	114	41.38	121.2	110	10.30	162.6	104	7.32	12.2	5	3.29	0	False
# 3	OH	84	408	Yes	No	0	299.4	71	50.90	61.9	88	5.26	196.9	89	8.86	6.6	7	1.78	2	False
# 4	OK	75	415	Yes	No	0	166.7	113	28.34	148.3	122	12.61	186.9	121	8.41	10.1	3	2.73	3	False
# print(df.shape)
# (3333, 20)
# print(df.columns)
# Index(['State', 'Account length', 'Area code', 'International plan',
#        'Voice mail plan', 'Number vmail messages', 'Total day minutes',
#        'Total day calls', 'Total day charge', 'Total eve minutes',
#        'Total eve calls', 'Total eve charge', 'Total night minutes',
#        'Total night calls', 'Total night charge', 'Total intl minutes',
#        'Total intl calls', 'Total intl charge', 'Customer service calls',
#        'Churn'],
#       dtype='object')
# print(df.describe())
#        Account length  Area code  Number vmail messages  Total day minutes  \
# count         3333.00    3333.00                3333.00            3333.00   
# mean           101.06     437.18                   8.10             179.78   
# std             39.82      42.37                  13.69              54.47   
# min              1.00     408.00                   0.00               0.00   
# 25%             74.00     408.00                   0.00             143.70   
# 50%            101.00     415.00                   0.00             179.40   
# 75%            127.00     510.00                  20.00             216.40   
# max            243.00     510.00                  51.00             350.80   

#        Total day calls  Total day charge  Total eve minutes  Total eve calls  \
# count          3333.00           3333.00            3333.00          3333.00   
# mean            100.44             30.56             200.98           100.11   
# std              20.07              9.26              50.71            19.92   
# min               0.00              0.00               0.00             0.00   
# 25%              87.00             24.43             166.60            87.00   
# 50%             101.00             30.50             201.40           100.00   
# 75%             114.00             36.79             235.30           114.00   
# max             165.00             59.64             363.70           170.00   

#        Total eve charge  Total night minutes  Total night calls  \
# count           3333.00              3333.00            3333.00   
# mean              17.08               200.87             100.11   
# std                4.31                50.57              19.57   
# min                0.00                23.20              33.00   
# 25%               14.16               167.00              87.00   
# 50%               17.12               201.20             100.00   
# 75%               20.00               235.30             113.00   
# max               30.91               395.00             175.00   

#        Total night charge  Total intl minutes  Total intl calls  \
# count             3333.00             3333.00           3333.00   
# mean                 9.04               10.24              4.48   
# std                  2.28                2.79              2.46   
# min                  1.04                0.00              0.00   
# 25%                  7.52                8.50              3.00   
# 50%                  9.05               10.30              4.00   
# 75%                 10.59               12.10              6.00   
# max                 17.77               20.00             20.00   

#        Total intl charge  Customer service calls  
# count            3333.00                 3333.00  
# mean                2.76                    1.56  
# std                 0.75                    1.32  
# min                 0.00                    0.00  
# 25%                 2.30                    1.00  
# 50%                 2.78                    1.00  
# 75%                 3.27                    2.00  
# max                 5.40                    9.00  
# print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3333 entries, 0 to 3332
# Data columns (total 20 columns):
#  #   Column                  Non-Null Count  Dtype  
# ---  ------                  --------------  -----  
#  0   State                   3333 non-null   object 
#  1   Account length          3333 non-null   int64  
#  2   Area code               3333 non-null   int64  
#  3   International plan      3333 non-null   object 
#  4   Voice mail plan         3333 non-null   object 
#  5   Number vmail messages   3333 non-null   int64  
#  6   Total day minutes       3333 non-null   float64
#  7   Total day calls         3333 non-null   int64  
#  8   Total day charge        3333 non-null   float64
#  9   Total eve minutes       3333 non-null   float64
#  10  Total eve calls         3333 non-null   int64  
#  11  Total eve charge        3333 non-null   float64
#  12  Total night minutes     3333 non-null   float64
#  13  Total night calls       3333 non-null   int64  
#  14  Total night charge      3333 non-null   float64
#  15  Total intl minutes      3333 non-null   float64
#  16  Total intl calls        3333 non-null   int64  
#  17  Total intl charge       3333 non-null   float64
#  18  Customer service calls  3333 non-null   int64  
#  19  Churn                   3333 non-null   bool   
# dtypes: bool(1), float64(8), int64(8), object(3)
# memory usage: 498.1+ KB
# None
# # We can change the column type with the astype method. Let's apply this method to the Churn feature to convert
# # it into int64

# df["Churn"] = df["Churn"].astype("int64")
# # In order to see statistics on non-numerical features, one has to explicitly indicate data types of interest
# # in the include parameter

# df.describe(include=["object", "bool"])
# State	International plan	Voice mail plan
# count	3333	3333	3333
# unique	51	2	2
# top	WV	No	No
# freq	106	3010	2411
# # For categorical (type object) and boolean (type bool) features we can use the value_counts method. 
# # Let's have a look at the distribution of Churn

# df["Churn"].value_counts()
# 0    2850
# 1     483
# Name: Churn, dtype: int64
# # 2850 users out of 3333 are loyal; their Churn value is 0. To calculate fractions, pass normalize=True 
# # to the value_counts function.

# df["Churn"].value_counts(normalize=True)
# 0    0.86
# 1    0.14
# Name: Churn, dtype: float64
# # sort in desc order
# df.sort_values(by="Total day charge", ascending=False).head()
# State	Account length	Area code	International plan	Voice mail plan	Number vmail messages	Total day minutes	Total day calls	Total day charge	Total eve minutes	Total eve calls	Total eve charge	Total night minutes	Total night calls	Total night charge	Total intl minutes	Total intl calls	Total intl charge	Customer service calls	Churn
# 365	CO	154	415	No	No	0	350.8	75	59.64	216.5	94	18.40	253.9	100	11.43	10.1	9	2.73	1	1
# 985	NY	64	415	Yes	No	0	346.8	55	58.96	249.5	79	21.21	275.4	102	12.39	13.3	9	3.59	1	1
# 2594	OH	115	510	Yes	No	0	345.3	81	58.70	203.4	106	17.29	217.5	107	9.79	11.8	8	3.19	1	1
# 156	OH	83	415	No	No	0	337.4	120	57.36	227.4	116	19.33	153.9	114	6.93	15.8	7	4.27	0	1
# 605	MO	112	415	No	No	0	335.5	77	57.04	212.5	109	18.06	265.0	132	11.93	12.7	8	3.43	2	1
# # sort by multiple columns
# df.sort_values(by=["Churn", "Total day charge"], ascending=[True, False]).head()
# State	Account length	Area code	International plan	Voice mail plan	Number vmail messages	Total day minutes	Total day calls	Total day charge	Total eve minutes	Total eve calls	Total eve charge	Total night minutes	Total night calls	Total night charge	Total intl minutes	Total intl calls	Total intl charge	Customer service calls	Churn
# 688	MN	13	510	No	Yes	21	315.6	105	53.65	208.9	71	17.76	260.1	123	11.70	12.1	3	3.27	3	0
# 2259	NC	210	415	No	Yes	31	313.8	87	53.35	147.7	103	12.55	192.7	97	8.67	10.1	7	2.73	3	0
# 534	LA	67	510	No	No	0	310.4	97	52.77	66.5	123	5.65	246.5	99	11.09	9.2	10	2.48	4	0
# 575	SD	114	415	No	Yes	36	309.9	90	52.68	200.3	89	17.03	183.5	105	8.26	14.2	2	3.83	1	0
# 2858	AL	141	510	No	Yes	28	308.0	123	52.36	247.8	128	21.06	152.9	103	6.88	7.4	3	2.00	1	0
# # Indexing and retrieving data
# # A DataFrame can be indexed in a few different ways; df[column_name', df.loc[location/label], df.iloc[index]

# # what is the proportion of churned users in our dataframe
# df["Churn"].mean()
# 0.14491449144914492
# 14.5% is actually quite bad for a company; such a churn rate can make the company go bankrupt.

# # What are average values of numerical features for churned users?
# df[df["Churn"] == 1].mean()
# /var/folders/4r/3_6gh8rj44g43v_wlyprm7h40000gn/T/ipykernel_26981/1679617622.py:2: FutureWarning: The default value of numeric_only in DataFrame.mean is deprecated. In a future version, it will default to False. In addition, specifying 'numeric_only=None' is deprecated. Select only valid columns or specify the value of numeric_only to silence this warning.
#   df[df["Churn"] == 1].mean()
# Account length            102.66
# Area code                 437.82
# Number vmail messages       5.12
# Total day minutes         206.91
# Total day calls           101.34
# Total day charge           35.18
# Total eve minutes         212.41
# Total eve calls           100.56
# Total eve charge           18.05
# Total night minutes       205.23
# Total night calls         100.40
# Total night charge          9.24
# Total intl minutes         10.70
# Total intl calls            4.16
# Total intl charge           2.89
# Customer service calls      2.23
# Churn                       1.00
# dtype: float64
# # What are the total no of users who didn't cancel
# df[df["Churn"] == 0]
# State	Account length	Area code	International plan	Voice mail plan	Number vmail messages	Total day minutes	Total day calls	Total day charge	Total eve minutes	Total eve calls	Total eve charge	Total night minutes	Total night calls	Total night charge	Total intl minutes	Total intl calls	Total intl charge	Customer service calls	Churn
# 0	KS	128	415	False	True	25	265.1	110	45.07	197.4	99	16.78	244.7	91	11.01	10.0	3	2.70	1	0
# 1	OH	107	415	False	True	26	161.6	123	27.47	195.5	103	16.62	254.4	103	11.45	13.7	3	3.70	1	0
# 2	NJ	137	415	False	False	0	243.4	114	41.38	121.2	110	10.30	162.6	104	7.32	12.2	5	3.29	0	0
# 3	OH	84	408	True	False	0	299.4	71	50.90	61.9	88	5.26	196.9	89	8.86	6.6	7	1.78	2	0
# 4	OK	75	415	True	False	0	166.7	113	28.34	148.3	122	12.61	186.9	121	8.41	10.1	3	2.73	3	0
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 3328	AZ	192	415	False	True	36	156.2	77	26.55	215.5	126	18.32	279.1	83	12.56	9.9	6	2.67	2	0
# 3329	WV	68	415	False	False	0	231.1	57	39.29	153.4	55	13.04	191.3	123	8.61	9.6	4	2.59	3	0
# 3330	RI	28	510	False	False	0	180.8	109	30.74	288.8	58	24.55	191.9	91	8.64	14.1	6	3.81	2	0
# 3331	CT	184	510	True	False	0	213.8	105	36.35	159.6	84	13.57	139.2	137	6.26	5.0	10	1.35	2	0
# 3332	TN	74	415	False	True	25	234.4	113	39.85	265.9	82	22.60	241.4	77	10.86	13.7	4	3.70	0	0
# 2850 rows × 20 columns

# # What are average values of numerical features for loyal users?
# df[df["Churn"] == 0].mean()
# /var/folders/4r/3_6gh8rj44g43v_wlyprm7h40000gn/T/ipykernel_26981/2979658814.py:2: FutureWarning: The default value of numeric_only in DataFrame.mean is deprecated. In a future version, it will default to False. In addition, specifying 'numeric_only=None' is deprecated. Select only valid columns or specify the value of numeric_only to silence this warning.
#   df[df["Churn"] == 0].mean()
# Account length            100.79
# Area code                 437.07
# International plan          0.07
# Voice mail plan             0.30
# Number vmail messages       8.60
# Total day minutes         175.18
# Total day calls           100.28
# Total day charge           29.78
# Total eve minutes         199.04
# Total eve calls           100.04
# Total eve charge           16.92
# Total night minutes       200.13
# Total night calls         100.06
# Total night charge          9.01
# Total intl minutes         10.16
# Total intl calls            4.53
# Total intl charge           2.74
# Customer service calls      1.45
# Churn                       0.00
# dtype: float64
# # How much time (on average) do churned users spend on the phone during daytime?
# df[df["Churn"] == 1]["Total day minutes"].mean()
# 206.91407867494823
# # What is the maximum length of international calls among loyal users (Churn == 0) who do not have an
# # international plan?

# df[(df["Churn"] == 0) & (df["International plan"] == "No")]["Total intl minutes"].max()
# 18.9
# # give us the values of the rows with index from 0 to 5 (inclusive) and columns labeled from State to
# # Area code (inclusive)
# df.loc[0:5, "State":"Area code"]
# State	Account length	Area code
# 0	KS	128	415
# 1	OH	107	415
# 2	NJ	137	415
# 3	OH	84	408
# 4	OK	75	415
# 5	AL	118	510
# df.loc[0:5, 0:3]
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[41], line 1
# ----> 1 df.loc[0:5, 0:3]

# File ~/anaconda3/lib/python3.10/site-packages/pandas/core/indexing.py:1067, in _LocationIndexer.__getitem__(self, key)
#    1065     if self._is_scalar_access(key):
#    1066         return self.obj._get_value(*key, takeable=self._takeable)
# -> 1067     return self._getitem_tuple(key)
#    1068 else:
#    1069     # we by definition only have the 0th axis
#    1070     axis = self.axis or 0

# File ~/anaconda3/lib/python3.10/site-packages/pandas/core/indexing.py:1256, in _LocIndexer._getitem_tuple(self, tup)
#    1253 if self._multi_take_opportunity(tup):
#    1254     return self._multi_take(tup)
# -> 1256 return self._getitem_tuple_same_dim(tup)

# File ~/anaconda3/lib/python3.10/site-packages/pandas/core/indexing.py:924, in _LocationIndexer._getitem_tuple_same_dim(self, tup)
#     921 if com.is_null_slice(key):
#     922     continue
# --> 924 retval = getattr(retval, self.name)._getitem_axis(key, axis=i)
#     925 # We should never have retval.ndim < self.ndim, as that should
#     926 #  be handled by the _getitem_lowerdim call above.
#     927 assert retval.ndim == self.ndim

# File ~/anaconda3/lib/python3.10/site-packages/pandas/core/indexing.py:1290, in _LocIndexer._getitem_axis(self, key, axis)
#    1288 if isinstance(key, slice):
#    1289     self._validate_key(key, axis)
# -> 1290     return self._get_slice_axis(key, axis=axis)
#    1291 elif com.is_bool_indexer(key):
#    1292     return self._getbool_axis(key, axis=axis)

# File ~/anaconda3/lib/python3.10/site-packages/pandas/core/indexing.py:1324, in _LocIndexer._get_slice_axis(self, slice_obj, axis)
#    1321     return obj.copy(deep=False)
#    1323 labels = obj._get_axis(axis)
# -> 1324 indexer = labels.slice_indexer(slice_obj.start, slice_obj.stop, slice_obj.step)
#    1326 if isinstance(indexer, slice):
#    1327     return self.obj._slice(indexer, axis=axis)

# File ~/anaconda3/lib/python3.10/site-packages/pandas/core/indexes/base.py:6559, in Index.slice_indexer(self, start, end, step, kind)
#    6516 """
#    6517 Compute the slice indexer for input labels and step.
#    6518 
#    (...)
#    6555 slice(1, 3, None)
#    6556 """
#    6557 self._deprecated_arg(kind, "kind", "slice_indexer")
# -> 6559 start_slice, end_slice = self.slice_locs(start, end, step=step)
#    6561 # return a slice
#    6562 if not is_scalar(start_slice):

# File ~/anaconda3/lib/python3.10/site-packages/pandas/core/indexes/base.py:6767, in Index.slice_locs(self, start, end, step, kind)
#    6765 start_slice = None
#    6766 if start is not None:
# -> 6767     start_slice = self.get_slice_bound(start, "left")
#    6768 if start_slice is None:
#    6769     start_slice = 0

# File ~/anaconda3/lib/python3.10/site-packages/pandas/core/indexes/base.py:6676, in Index.get_slice_bound(self, label, side, kind)
#    6672 original_label = label
#    6674 # For datetime indices label may be a string that has to be converted
#    6675 # to datetime boundary according to its resolution.
# -> 6676 label = self._maybe_cast_slice_bound(label, side)
#    6678 # we need to look up the label
#    6679 try:

# File ~/anaconda3/lib/python3.10/site-packages/pandas/core/indexes/base.py:6623, in Index._maybe_cast_slice_bound(self, label, side, kind)
#    6618 # We are a plain index here (sub-class override this method if they
#    6619 # wish to have special treatment for floats/ints, e.g. Float64Index and
#    6620 # datetimelike Indexes
#    6621 # reject them, if index does not contain label
#    6622 if (is_float(label) or is_integer(label)) and label not in self:
# -> 6623     raise self._invalid_indexer("slice", label)
#    6625 return label

# TypeError: cannot do slice indexing on Index with these indexers [0] of type int
# # give us the values of the first five rows in the first three columns" (as in a typical Python slice: the maximal value 
# # is not included)
# df.iloc[0:5, 0:3]
# State	Account length	Area code
# 0	KS	128	415
# 1	OH	107	415
# 2	NJ	137	415
# 3	OH	84	408
# 4	OK	75	415
# # to get the first or the last line of the data frame, we can use the df[:1] or df[-1:]
# df[-1:]
# State	Account length	Area code	International plan	Voice mail plan	Number vmail messages	Total day minutes	Total day calls	Total day charge	Total eve minutes	Total eve calls	Total eve charge	Total night minutes	Total night calls	Total night charge	Total intl minutes	Total intl calls	Total intl charge	Customer service calls	Churn
# 3332	TN	74	415	No	Yes	25	234.4	113	39.85	265.9	82	22.6	241.4	77	10.86	13.7	4	3.7	0	0
# df[:1]
# State	Account length	Area code	International plan	Voice mail plan	Number vmail messages	Total day minutes	Total day calls	Total day charge	Total eve minutes	Total eve calls	Total eve charge	Total night minutes	Total night calls	Total night charge	Total intl minutes	Total intl calls	Total intl charge	Customer service calls	Churn
# 0	KS	128	415	False	True	25	265.1	110	45.07	197.4	99	16.78	244.7	91	11.01	10.0	3	2.7	1	0
# Applying functions to columns, rows and cells
# # The apply method can also be used to apply a function to each row. To do this, specify axis=1
# df.apply(np.max)
# State                        WY
# Account length              243
# Area code                   510
# International plan          Yes
# Voice mail plan             Yes
# Number vmail messages        51
# Total day minutes         350.8
# Total day calls             165
# Total day charge          59.64
# Total eve minutes         363.7
# Total eve calls             170
# Total eve charge          30.91
# Total night minutes       395.0
# Total night calls           175
# Total night charge        17.77
# Total intl minutes         20.0
# Total intl calls             20
# Total intl charge           5.4
# Customer service calls        9
# Churn                         1
# dtype: object
# # Select all states starting with W
# df[df["State"].apply(lambda state: state[0] == "W")].head()
# State	Account length	Area code	International plan	Voice mail plan	Number vmail messages	Total day minutes	Total day calls	Total day charge	Total eve minutes	Total eve calls	Total eve charge	Total night minutes	Total night calls	Total night charge	Total intl minutes	Total intl calls	Total intl charge	Customer service calls	Churn
# 9	WV	141	415	Yes	Yes	37	258.6	84	43.96	222.0	111	18.87	326.4	97	14.69	11.2	5	3.02	0	0
# 26	WY	57	408	No	Yes	39	213.0	115	36.21	191.1	112	16.24	182.7	115	8.22	9.5	3	2.57	0	0
# 44	WI	64	510	No	No	0	154.0	67	26.18	225.8	118	19.19	265.3	86	11.94	3.5	3	0.95	1	0
# 49	WY	97	415	No	Yes	24	133.2	135	22.64	217.2	58	18.46	70.6	79	3.18	11.0	3	2.97	1	0
# 54	WY	87	415	No	No	0	151.0	83	25.67	219.7	116	18.67	203.9	127	9.18	9.7	3	2.62	5	1
# # The map method can be used to replace values in a column by passing a dictionary of the form 
# # {old_value: new_value} as its argument:

# d = {"No": False, "Yes": True}
# df["International plan"] = df["International plan"].map(d)
# df.head()
# State	Account length	Area code	International plan	Voice mail plan	Number vmail messages	Total day minutes	Total day calls	Total day charge	Total eve minutes	Total eve calls	Total eve charge	Total night minutes	Total night calls	Total night charge	Total intl minutes	Total intl calls	Total intl charge	Customer service calls	Churn
# 0	KS	128	415	False	Yes	25	265.1	110	45.07	197.4	99	16.78	244.7	91	11.01	10.0	3	2.70	1	0
# 1	OH	107	415	False	Yes	26	161.6	123	27.47	195.5	103	16.62	254.4	103	11.45	13.7	3	3.70	1	0
# 2	NJ	137	415	False	No	0	243.4	114	41.38	121.2	110	10.30	162.6	104	7.32	12.2	5	3.29	0	0
# 3	OH	84	408	True	No	0	299.4	71	50.90	61.9	88	5.26	196.9	89	8.86	6.6	7	1.78	2	0
# 4	OK	75	415	True	No	0	166.7	113	28.34	148.3	122	12.61	186.9	121	8.41	10.1	3	2.73	3	0
# d = {"No": False, "Yes": True}
# df.loc[:,'International plan'] = df["International plan"].map(d)
# # df.iloc[:, 3] = df["International plan"].map(d) you have to know the column index to use this.
# df.head()
# State	Account length	Area code	International plan	Voice mail plan	Number vmail messages	Total day minutes	Total day calls	Total day charge	Total eve minutes	Total eve calls	Total eve charge	Total night minutes	Total night calls	Total night charge	Total intl minutes	Total intl calls	Total intl charge	Customer service calls	Churn
# 0	KS	128	415	NaN	True	25	265.1	110	45.07	197.4	99	16.78	244.7	91	11.01	10.0	3	2.70	1	0
# 1	OH	107	415	NaN	True	26	161.6	123	27.47	195.5	103	16.62	254.4	103	11.45	13.7	3	3.70	1	0
# 2	NJ	137	415	NaN	False	0	243.4	114	41.38	121.2	110	10.30	162.6	104	7.32	12.2	5	3.29	0	0
# 3	OH	84	408	NaN	False	0	299.4	71	50.90	61.9	88	5.26	196.9	89	8.86	6.6	7	1.78	2	0
# 4	OK	75	415	NaN	False	0	166.7	113	28.34	148.3	122	12.61	186.9	121	8.41	10.1	3	2.73	3	0
# # doing the above with the replace mtd
# df = df.replace({"Voice mail plan": d})
# df.head()
# State	Account length	Area code	International plan	Voice mail plan	Number vmail messages	Total day minutes	Total day calls	Total day charge	Total eve minutes	Total eve calls	Total eve charge	Total night minutes	Total night calls	Total night charge	Total intl minutes	Total intl calls	Total intl charge	Customer service calls	Churn
# 0	KS	128	415	False	True	25	265.1	110	45.07	197.4	99	16.78	244.7	91	11.01	10.0	3	2.70	1	0
# 1	OH	107	415	False	True	26	161.6	123	27.47	195.5	103	16.62	254.4	103	11.45	13.7	3	3.70	1	0
# 2	NJ	137	415	False	False	0	243.4	114	41.38	121.2	110	10.30	162.6	104	7.32	12.2	5	3.29	0	0
# 3	OH	84	408	True	False	0	299.4	71	50.90	61.9	88	5.26	196.9	89	8.86	6.6	7	1.78	2	0
# 4	OK	75	415	True	False	0	166.7	113	28.34	148.3	122	12.61	186.9	121	8.41	10.1	3	2.73	3	0
# Grouping
# The syntax for grouping is:
# df.groupby(by=grouping_columns)[columns_to_show].function()
# i. First, the groupby method divides the grouping_columns by their values. They become a new index in the resulting dataframe.

# ii. Then, columns of interest are selected (columns_to_show). If columns_to_show is not included, all non groupby clauses will be included.

# iii. Finally, one or several functions are applied to the obtained groups per selected columns.

# # Group the data according to the Churn and get the statistics of the 3 given columns
# columns_to_show = ["Total day minutes", "Total eve minutes", "Total night minutes"]
# df.groupby(["Churn"])[columns_to_show].describe(percentiles=[]) # this truncate the the 25th & 75th percentile
# Total day minutes	Total eve minutes	Total night minutes
# count	mean	std	min	50%	max	count	mean	std	min	50%	max	count	mean	std	min	50%	max
# Churn																		
# 0	2850.0	175.18	50.18	0.0	177.2	315.6	2850.0	199.04	50.29	0.0	199.6	361.8	2850.0	200.13	51.11	23.2	200.25	395.0
# 1	483.0	206.91	69.00	0.0	217.6	350.8	483.0	212.41	51.73	70.9	211.3	363.7	483.0	205.23	47.13	47.4	204.80	354.9
# columns_to_show = ["Total day minutes", "Total eve minutes", "Total night minutes"]
# df.groupby(["Churn"])[columns_to_show].describe()
# Total day minutes	Total eve minutes	Total night minutes
# count	mean	std	min	25%	50%	75%	max	count	mean	...	75%	max	count	mean	std	min	25%	50%	75%	max
# Churn																					
# 0	2850.0	175.18	50.18	0.0	142.83	177.2	210.30	315.6	2850.0	199.04	...	233.20	361.8	2850.0	200.13	51.11	23.2	165.90	200.25	234.90	395.0
# 1	483.0	206.91	69.00	0.0	153.25	217.6	265.95	350.8	483.0	212.41	...	249.45	363.7	483.0	205.23	47.13	47.4	171.25	204.80	239.85	354.9
# 2 rows × 24 columns

# # Let’s do the same thing, but slightly differently by passing a list of functions to agg()
# columns_to_show = ["Total day minutes", "Total eve minutes", "Total night minutes"]
# df.groupby(["Churn"])[columns_to_show].agg([np.mean, np.std, np.min, np.max])
# Total day minutes	Total eve minutes	Total night minutes
# mean	std	amin	amax	mean	std	amin	amax	mean	std	amin	amax
# Churn												
# 0	175.18	50.18	0.0	315.6	199.04	50.29	0.0	361.8	200.13	51.11	23.2	395.0
# 1	206.91	69.00	0.0	350.8	212.41	51.73	70.9	363.7	205.23	47.13	47.4	354.9
# # Suppose we want to see how the observations in our sample are distributed in the context of two variables
# # Churn and International plan. To do so, we can build a contingency table using the crosstab method:

# pd.crosstab(df["Churn"], df["International plan"])
# International plan	False	True
# Churn		
# 0	2664	186
# 1	346	137
# # Churn and Voice mail plan
# pd.crosstab(df["Churn"], df["Voice mail plan"], normalize=True)
# Voice mail plan	False	True
# Churn		
# 0	0.60	0.25
# 1	0.12	0.02
# We can see that most of the users are loyal and do not use additional services (International Plan/Voice mail).

# They are similar to Pivot in Excel.

# Pivot tables are implemented in Pandas: the pivot_table method takes the following parameters:

# i. values – a list of variables to calculate statistics for,

# ii. index – a list of variables to group data by,

# iii. aggfunc – what statistics we need to calculate for groups, ex. sum, mean, maximum, minimum or something else.

# Let's take a look at the average number of day, evening, and night calls by area code:
# df.pivot_table(
#     ["Total day calls", "Total eve calls", "Total night calls"],
#     ["Area code"],
#     aggfunc="mean",
# )
# Total day calls	Total eve calls	Total night calls
# Area code			
# 408	100.50	99.79	99.04
# 415	100.58	100.50	100.40
# 510	100.10	99.67	100.60
 