# import numpy as np
# import pandas as pd
# label = ['a','b','c']

# my_data =[10,20,30]

# arr = np.array(my_data)

# d = {'a':10,'b':20,'c':30}
# pd.Series(d)
# a    10
# b    20
# c    30
# dtype: int64
# ser1 = pd.Series(my_data, label)
# ser1
# a    10
# b    20
# c    30
# dtype: int64
# pd.Series(label,my_data)
# 10    a
# 20    b
# 30    c
# dtype: object
# ser1[2]
# 30
# adata = [12,32,42,30]
# ser2 = pd.Series(adata,['a','c','f', 'd'])
# ser2
# a    12
# c    32
# f    42
# d    30
# dtype: int64
# ser1
# a    10
# b    20
# c    30
# dtype: int64
# ser1 + ser2
# a    22.0
# b     NaN
# c    62.0
# d     NaN
# f     NaN
# dtype: float64
 
# ser1 + ser2
# a    22.0
# b     NaN
# c    62.0
# d     NaN
# f     NaN
# dtype: float64
# from numpy.random import randn
# np.random.seed(101)
# df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
# df
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# C	-2.018168	0.740122	0.528813	-0.589001
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509
# df['Y']
# A    0.907969
# B   -0.848077
# C    0.528813
# D   -0.933237
# E    2.605967
# Name: Y, dtype: float64
# df[['W', 'Z']]
# W	Z
# A	2.706850	0.503826
# B	0.651118	0.605965
# C	-2.018168	-0.589001
# D	0.188695	0.955057
# E	0.190794	0.683509
# # 
# df['NEW'] = df['W'] + df['Y']
# df
# W	X	Y	Z	NEW
# A	2.706850	0.628133	0.907969	0.503826	3.614819
# B	0.651118	-0.319318	-0.848077	0.605965	-0.196959
# C	-2.018168	0.740122	0.528813	-0.589001	-1.489355
# D	0.188695	-0.758872	-0.933237	0.955057	-0.744542
# E	0.190794	1.978757	2.605967	0.683509	2.796762
# # axis = 1 means you're referring to the columns (the default axis is 0)
# df.drop('NEW',axis=1,inplace=True)
# df
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# C	-2.018168	0.740122	0.528813	-0.589001
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509
# # axis = 0 means you're referring to the rows
# df.drop('E',axis=0)
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# C	-2.018168	0.740122	0.528813	-0.589001
# D	0.188695	-0.758872	-0.933237	0.955057
# df
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# C	-2.018168	0.740122	0.528813	-0.589001
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509
# # we're indexing row values
# df.loc['C']
# W   -2.018168
# X    0.740122
# Y    0.528813
# Z   -0.589001
# Name: C, dtype: float64
# # iloc means index location of a row
# df.iloc[2]
# W   -2.018168
# X    0.740122
# Y    0.528813
# Z   -0.589001
# Name: C, dtype: float64
# df['Y']
# A    0.907969
# B   -0.848077
# C    0.528813
# D   -0.933237
# E    2.605967
# Name: Y, dtype: float64
# df[['X','Z']]
# X	Z
# A	0.628133	0.503826
# B	-0.319318	0.605965
# C	0.740122	-0.589001
# D	-0.758872	0.955057
# E	1.978757	0.683509
# df
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# C	-2.018168	0.740122	0.528813	-0.589001
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509
# # indexing a row and a column (a single cell)
# df.loc[['C'],['Y']]
# Y
# C	0.528813
# # indexing two rows
# df.loc[['C','A']]
# W	X	Y	Z
# C	-2.018168	0.740122	0.528813	-0.589001
# A	2.706850	0.628133	0.907969	0.503826
# df.loc[['C','A','E'],['W','X','Z']]
# W	X	Z
# C	-2.018168	0.740122	-0.589001
# A	2.706850	0.628133	0.503826
# E	0.190794	1.978757	0.683509
# df
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# C	-2.018168	0.740122	0.528813	-0.589001
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509
# df > 0
# W	X	Y	Z
# A	True	True	True	True
# B	True	False	False	True
# C	False	True	True	False
# D	True	False	False	True
# E	True	True	True	True
# df[df > 0]
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	NaN	NaN	0.605965
# C	NaN	0.740122	0.528813	NaN
# D	0.188695	NaN	NaN	0.955057
# E	0.190794	1.978757	2.605967	0.683509
# df[df['W'] >0]
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509
# df[df['Y']>0]
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# C	-2.018168	0.740122	0.528813	-0.589001
# E	0.190794	1.978757	2.605967	0.683509
# df
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# C	-2.018168	0.740122	0.528813	-0.589001
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509
# df2 = df[df['W']>0]
# df2
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509
# df2.iloc[[0,3]]
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# E	0.190794	1.978757	2.605967	0.683509
# df[df['W']>0].iloc[[0,3]]
# W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# E	0.190794	1.978757	2.605967	0.683509
# (df['W']>0) & (df['Y']>1)
# A    False
# B    False
# C    False
# D    False
# E     True
# dtype: bool
# df[(df['W']>0) & (df['Y']>1)]
# W	X	Y	Z
# E	0.190794	1.978757	2.605967	0.683509
# To reset index of your data frame to original values(your former index will become a column on the data frame)

# df.reset_index()
# index	W	X	Y	Z
# 0	A	2.706850	0.628133	0.907969	0.503826
# 1	B	0.651118	-0.319318	-0.848077	0.605965
# 2	C	-2.018168	0.740122	0.528813	-0.589001
# 3	D	0.188695	-0.758872	-0.933237	0.955057
# 4	E	0.190794	1.978757	2.605967	0.683509
# You can also assign new indexes by first making it a new column

# newind = 'CA CB CC CD CE'.split()
# newind
# ['CA', 'CB', 'CC', 'CD', 'CE']
# df['ind'] = newind
# df
# W	X	Y	Z	ind
# A	2.706850	0.628133	0.907969	0.503826	CA
# B	0.651118	-0.319318	-0.848077	0.605965	CB
# C	-2.018168	0.740122	0.528813	-0.589001	CC
# D	0.188695	-0.758872	-0.933237	0.955057	CD
# E	0.190794	1.978757	2.605967	0.683509	CE
# # making the column 'ind' our new index
# df.set_index('ind', inplace = True)
# df
# W	X	Y	Z
# ind				
# CA	2.706850	0.628133	0.907969	0.503826
# CB	0.651118	-0.319318	-0.848077	0.605965
# CC	-2.018168	0.740122	0.528813	-0.589001
# CD	0.188695	-0.758872	-0.933237	0.955057
# CE	0.190794	1.978757	2.605967	0.683509
# # Index Levels

# outside = ['G1','G1','G1','G2','G2','G2']
# inside = [1,2,3,1,2,3]
# hier_index = list(zip(outside,inside))

# hier_index = pd.MultiIndex.from_tuples(hier_index)
# hier_index
# MultiIndex([('G1', 1),
#             ('G1', 2),
#             ('G1', 3),
#             ('G2', 1),
#             ('G2', 2),
#             ('G2', 3)],
#            )
# df1 = pd.DataFrame(randn(6,2),hier_index,['A','B'])
# df1
# A	B
# G1	1	0.302665	1.693723
# 2	-1.706086	-1.159119
# 3	-0.134841	0.390528
# G2	1	0.166905	0.184502
# 2	0.807706	0.072960
# 3	0.638787	0.329646
# df1.loc['G1'].loc[1]
# A    0.302665
# B    1.693723
# Name: 1, dtype: float64
# df1['AB'] = df1['A'] + df1['B']
# df1
# A	B	AB
# G1	1	0.302665	1.693723	1.996388
# 2	-1.706086	-1.159119	-2.865205
# 3	-0.134841	0.390528	0.255687
# G2	1	0.166905	0.184502	0.351406
# 2	0.807706	0.072960	0.880666
# 3	0.638787	0.329646	0.968433
# df1['AB']
# G1  1    1.996388
#     2   -2.865205
#     3    0.255687
# G2  1    0.351406
#     2    0.880666
#     3    0.968433
# Name: AB, dtype: float64
# df1.loc['G2'][['A','AB']]
# A	AB
# 1	0.166905	0.351406
# 2	0.807706	0.880666
# 3	0.638787	0.968433
# To name the indexes, use dataframename.index.names = [ the name(s) in strings, seperated with commas]

# new_df = pd.DataFrame(randn(4,4),['A','B','C','D'],['W','X','Y','Z'])
# new_df
# W	X	Y	Z
# A	-0.497104	-0.754070	-0.943406	0.484752
# B	-0.116773	1.901755	0.238127	1.996652
# C	-0.993263	0.196800	-1.136645	0.000366
# D	1.025984	-0.156598	-0.031579	0.649826
# new_df.index.names = ['index']
# new_df
# W	X	Y	Z
# index				
# A	-0.497104	-0.754070	-0.943406	0.484752
# B	-0.116773	1.901755	0.238127	1.996652
# C	-0.993263	0.196800	-1.136645	0.000366
# D	1.025984	-0.156598	-0.031579	0.649826
# df1.index.names = ['Groups','num']
# df1
# A	B	AB
# Groups	num			
# G1	1	0.302665	1.693723	1.996388
# 2	-1.706086	-1.159119	-2.865205
# 3	-0.134841	0.390528	0.255687
# G2	1	0.166905	0.184502	0.351406
# 2	0.807706	0.072960	0.880666
# 3	0.638787	0.329646	0.968433
# df1.loc['G2'].loc[2]['B']
# 0.07295967531703869
# df1.loc['G1'].loc[[1,2]]['AB']
# num
# 1    1.996388
# 2   -2.865205
# Name: AB, dtype: float64
# # xs means cross section
# df1.xs(1,level='num')[['AB','B']]
# AB	B
# Groups		
# G1	1.996388	1.693723
# G2	0.351406	0.184502
# df1.xs('G2')
# A	B	AB
# num			
# 1	0.166905	0.184502	0.351406
# 2	0.807706	0.072960	0.880666
# 3	0.638787	0.329646	0.968433
# d1 = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3],'D':[3,4,5]}
# df3 = pd.DataFrame(d1)
# df3
# A	B	C	D
# 0	1.0	5.0	1	3
# 1	2.0	NaN	2	4
# 2	NaN	NaN	3	5
# # without the argument of inplace = True the changes are not permanent on our dataframe
# df3.dropna()
# A	B	C	D
# 0	1.0	5.0	1	3
# df3
# A	B	C	D
# 0	1.0	5.0	1	3
# 1	2.0	NaN	2	4
# 2	NaN	NaN	3	5
# df3.dropna(axis=1)
# C	D
# 0	1	3
# 1	2	4
# 2	3	5
# df3.dropna(thresh=2)
# A	B	C	D
# 0	1.0	5.0	1	3
# 1	2.0	NaN	2	4
# 2	NaN	NaN	3	5
# df3.dropna(axis=1,thresh=2)
# A	C	D
# 0	1.0	1	3
# 1	2.0	2	4
# 2	NaN	3	5
# df3
# A	B	C	D
# 0	1.0	5.0	1	3
# 1	2.0	NaN	2	4
# 2	NaN	NaN	3	5
# We stopped here...
# df3.fillna(value='FILL')
# A	B	C	D
# 0	1.0	5.0	1	3
# 1	2.0	FILL	2	4
# 2	FILL	FILL	3	5
# df3['A'].fillna(value = df3['A'].mean(),inplace=True)
# df3
# A	B	C	D
# 0	1.0	5.0	1	3
# 1	2.0	NaN	2	4
# 2	1.5	NaN	3	5
# data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
#        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
#        'Sales':[200,120,340,124,243,350]}
# df3 = pd.DataFrame(data)
# df3
# Company	Person	Sales
# 0	GOOG	Sam	200
# 1	GOOG	Charlie	120
# 2	MSFT	Amy	340
# 3	MSFT	Vanessa	124
# 4	FB	Carl	243
# 5	FB	Sarah	350
# df3.groupby('Company')['Sales'].sum()
# Company
# FB      593
# GOOG    320
# MSFT    464
# Name: Sales, dtype: int64
# df3.groupby('Company')['Sales'].std()
# Company
# FB       75.660426
# GOOG     56.568542
# MSFT    152.735065
# Name: Sales, dtype: float64
# df3.groupby('Company').max()
# Person	Sales
# Company		
# FB	Sarah	350
# GOOG	Sam	200
# MSFT	Vanessa	340
# df3.groupby('Company').min()
# Person	Sales
# Company		
# FB	Carl	243
# GOOG	Charlie	120
# MSFT	Amy	124
# df3.groupby('Company').count()
# Person	Sales
# Company		
# FB	2	2
# GOOG	2	2
# MSFT	2	2
# df3.groupby('Company').describe()
# Sales
# count	mean	std	min	25%	50%	75%	max
# Company								
# FB	2.0	296.5	75.660426	243.0	269.75	296.5	323.25	350.0
# GOOG	2.0	160.0	56.568542	120.0	140.00	160.0	180.00	200.0
# MSFT	2.0	232.0	152.735065	124.0	178.00	232.0	286.00	340.0
# df3.groupby('Company').describe().loc['GOOG']
# Sales  count      2.000000
#        mean     160.000000
#        std       56.568542
#        min      120.000000
#        25%      140.000000
#        50%      160.000000
#        75%      180.000000
#        max      200.000000
# Name: GOOG, dtype: float64
# df3.groupby('Company').describe().loc[['FB','MSFT']]
# Sales
# count	mean	std	min	25%	50%	75%	max
# Company								
# FB	2.0	296.5	75.660426	243.0	269.75	296.5	323.25	350.0
# MSFT	2.0	232.0	152.735065	124.0	178.00	232.0	286.00	340.0
# Check out concatnation(which I like and get), merging and joining of dataframes

# df_c = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
# df_c.head()
# col1	col2	col3
# 0	1	444	abc
# 1	2	555	def
# 2	3	666	ghi
# 3	4	444	xyz
# df_c
# col1	col2	col3
# 0	1	444	abc
# 1	2	555	def
# 2	3	666	ghi
# 3	4	444	xyz
# df_c['col2'].unique()
# array([444, 555, 666], dtype=int64)
# df_c['col2'].nunique()
# 3
# df_c['col2'].value_counts()
# 444    2
# 555    1
# 666    1
# Name: col2, dtype: int64
# df_c[df_c['col1']>1]
# col1	col2	col3
# 1	2	555	def
# 2	3	666	ghi
# 3	4	444	xyz
# df_c['col1']>1
# 0    False
# 1     True
# 2     True
# 3     True
# Name: col1, dtype: bool
# df_c[(df_c['col1']>1) & (df_c['col2']==444)]
# col1	col2	col3
# 3	4	444	xyz
# df_c.index.names = ['indx']
# df_c
# col1	col2	col3
# indx			
# 0	1	444	abc
# 1	2	555	def
# 2	3	666	ghi
# 3	4	444	xyz
# YOU CAN APPLY LAMBDA EXPRESSIONS OR ANY OTHER METHOD,BUT MOSTLY USEFUL WITH LAMBDA EXPRESSIONS BY USING .apply(the expression)

# df_c['col2'].apply(lambda x:x**2)
# indx
# 0    197136
# 1    308025
# 2    443556
# 3    197136
# Name: col2, dtype: int64
# df_c.columns
# Index(['col1', 'col2', 'col3'], dtype='object')
# df_c.index
# RangeIndex(start=0, stop=4, step=1, name='indx')
# df_c.sort_values(by='col2')
# col1	col2	col3
# indx			
# 0	1	444	abc
# 3	4	444	xyz
# 1	2	555	def
# 2	3	666	ghi
# df_c.isnull()
# col1	col2	col3
# indx			
# 0	False	False	False
# 1	False	False	False
# 2	False	False	False
# 3	False	False	False
# data = {'A':['foo','foo','foo','bar','bar','bar'],
#      'B':['one','one','two','two','one','one'],
#        'C':['x','y','x','y','x','y'],
#        'D':[1,3,2,5,4,1]}

# df4 = pd.DataFrame(data) 
# df4
# A	B	C	D
# 0	foo	one	x	1
# 1	foo	one	y	3
# 2	foo	two	x	2
# 3	bar	two	y	5
# 4	bar	one	x	4
# 5	bar	one	y	1
# df4.pivot_table(index=['A','B'],values='D',columns='C')
# C	x	y
# A	B		
# bar	one	4.0	1.0
# two	NaN	5.0
# foo	one	1.0	3.0
# two	2.0	NaN
 