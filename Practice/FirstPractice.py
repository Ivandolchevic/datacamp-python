'''
Created on Aug 9, 2017

@author: idolchevic
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('points-dinteret.csv',sep=';')

#print(list(df[['nom']].groupby(['nom'])))


#agg = df[['categorie']].groupby(['categorie'])['categorie'].count()
#agg = df.filter(regex='^Citoy', axis=0)

criterion = df['categorie'].map(lambda x: not x.startswith('Citoy'))

# pandas.core.frame.DataFrame 
print(type(df))
print(type(df[criterion]))
print(type(df[criterion][['categorie']]))

# pandas.core.groupby.DataFrameGroupBy
print(type(df[criterion][['categorie']].groupby(['categorie'])))

# pandas.core.groupby.SeriesGroupBy
print(type(df[criterion][['categorie']].groupby(['categorie'])['categorie']))

# pandas.core.series.Series
print(type(df[criterion][['categorie']].groupby(['categorie'])['categorie'].count()))


agg = df[criterion][['categorie']].groupby(['categorie'])['categorie'].count()

# agg of type pandas.core.series.Series
print(type(agg));

# agg.values as type numpy.ndarray
print(type(agg.values));

# agg.keys() as type pandas.core.indexes.base.Index
print(type(agg.keys()))

plt.bar(range(len(agg)), agg.values, align='center')
plt.xticks(range(len(agg)), agg.keys(),rotation='vertical')
plt.show()

