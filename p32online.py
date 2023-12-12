# Introduction
# In this class, we'll go beyond the EDA features of Pandas. We'll do more than load and transform your data. We will learn the basic pandas plotting facilities, starting with the simplest type of visualization: single-variable or "univariate" visualizations.

# This includes basic tools like bar plots and line charts. Through these we'll get an understanding of pandas plotting library structure, and spend some time examining data types.

# import numpy as np
# import pandas as pd

# dataset = '/Users/damilare/Documents/ingryd/datasets/winemag-data_first150k.csv'

# reviews = pd.read_csv(dataset)
# reviews.head()
# Unnamed: 0	country	description	designation	points	price	province	region_1	region_2	variety	winery
# 0	0	US	This tremendous 100% varietal wine hails from ...	Martha's Vineyard	96	235.0	California	Napa Valley	Napa	Cabernet Sauvignon	Heitz
# 1	1	Spain	Ripe aromas of fig, blackberry and cassis are ...	Carodorum Selección Especial Reserva	96	110.0	Northern Spain	Toro	NaN	Tinta de Toro	Bodega Carmen Rodríguez
# 2	2	US	Mac Watson honors the memory of a wine once ma...	Special Selected Late Harvest	96	90.0	California	Knights Valley	Sonoma	Sauvignon Blanc	Macauley
# 3	3	US	This spent 20 months in 30% new French oak, an...	Reserve	96	65.0	Oregon	Willamette Valley	Willamette Valley	Pinot Noir	Ponzi
# 4	4	France	This is the top wine from La Bégude, named aft...	La Brûlade	95	66.0	Provence	Bandol	NaN	Provence red blend	Domaine de la Bégude
# reviews.shape
# (150930, 11)
# get_province = reviews['province']
# get_province.value_counts().head(10)
# California          44508
# Washington           9750
# Tuscany              7281
# Bordeaux             6111
# Northern Spain       4892
# Mendoza Province     4742
# Oregon               4589
# Burgundy             4308
# Piedmont             4093
# Veneto               3962
# Name: province, dtype: int64
# # Bar charts are arguably the simplest data visualization. They map categories to numbers.
# reviews['province'].value_counts().head(10).plot.bar()
# <Axes: >

# reviews.columns
# Index(['Unnamed: 0', 'country', 'description', 'designation', 'points',
#        'price', 'province', 'region_1', 'region_2', 'variety', 'winery'],
#       dtype='object')
# # Getting the percentage of the california vintage wine
# (reviews['province'].value_counts().head(10) / len(reviews)).plot.bar()
# <Axes: >

# We can see that California produces almost a third of the total wines produced
# reviews['points']
# 0         96
# 1         96
# 2         96
# 3         96
# 4         95
#           ..
# 150925    91
# 150926    91
# 150927    91
# 150928    90
# 150929    90
# Name: points, Length: 150930, dtype: int64
# Line charts are not the best when it comes to nominal categorical data.
# reviews['points'].value_counts().sort_index().plot.line()
# <Axes: >

# The area chart is simply a shaded line chart
# reviews['points'].value_counts().sort_index().plot.area()
# <Axes: >

# # Get the price variable
# price = reviews['price']
# price
# 0         235.0
# 1         110.0
# 2          90.0
# 3          65.0
# 4          66.0
#           ...  
# 150925     20.0
# 150926     27.0
# 150927     20.0
# 150928     52.0
# 150929     15.0
# Name: price, Length: 150930, dtype: float64
# # get prices less than 200
# reviews[price < 200]
# Unnamed: 0	country	description	designation	points	price	province	region_1	region_2	variety	winery
# 1	1	Spain	Ripe aromas of fig, blackberry and cassis are ...	Carodorum Selección Especial Reserva	96	110.0	Northern Spain	Toro	NaN	Tinta de Toro	Bodega Carmen Rodríguez
# 2	2	US	Mac Watson honors the memory of a wine once ma...	Special Selected Late Harvest	96	90.0	California	Knights Valley	Sonoma	Sauvignon Blanc	Macauley
# 3	3	US	This spent 20 months in 30% new French oak, an...	Reserve	96	65.0	Oregon	Willamette Valley	Willamette Valley	Pinot Noir	Ponzi
# 4	4	France	This is the top wine from La Bégude, named aft...	La Brûlade	95	66.0	Provence	Bandol	NaN	Provence red blend	Domaine de la Bégude
# 5	5	Spain	Deep, dense and pure from the opening bell, th...	Numanthia	95	73.0	Northern Spain	Toro	NaN	Tinta de Toro	Numanthia
# ...	...	...	...	...	...	...	...	...	...	...	...
# 150925	150925	Italy	Many people feel Fiano represents southern Ita...	NaN	91	20.0	Southern Italy	Fiano di Avellino	NaN	White Blend	Feudi di San Gregorio
# 150926	150926	France	Offers an intriguing nose with ginger, lime an...	Cuvée Prestige	91	27.0	Champagne	Champagne	NaN	Champagne Blend	H.Germain
# 150927	150927	Italy	This classic example comes from a cru vineyard...	Terre di Dora	91	20.0	Southern Italy	Fiano di Avellino	NaN	White Blend	Terredora
# 150928	150928	France	A perfect salmon shade, with scents of peaches...	Grand Brut Rosé	90	52.0	Champagne	Champagne	NaN	Champagne Blend	Gosset
# 150929	150929	Italy	More Pinot Grigios should taste like this. A r...	NaN	90	15.0	Northeastern Italy	Alto Adige	NaN	Pinot Grigio	Alois Lageder
# 136368 rows × 11 columns

# # plot a histogram for the prices < 200
# reviews[price < 200]['price'].plot.hist()
# <Axes: ylabel='Frequency'>

# # plot a bar chart for the prices < 200
# reviews[price < 200]['price'].plot.bar()
 