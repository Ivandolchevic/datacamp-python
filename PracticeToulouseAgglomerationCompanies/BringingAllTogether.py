'''
Created on Sep 5, 2017

@author: idolchevic
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import seaborn as sns


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y


sns.set()

tail_n = 20
 
df_pop = pd.read_csv('pop_count_smoothed.csv',index_col=[0,1])

df_cies = pd.read_csv('cies_count_smoothed.csv',index_col=[0,1])

df_toulouse_pop = df_pop.loc['TOULOUSE']['count']
df_toulouse_cies = df_cies.loc['TOULOUSE']['count']

df_agglomeration_pop = df_pop.loc['AGGLOMERATION']['count']
df_agglomeration_cies = df_cies.loc['AGGLOMERATION']['count']



print('--------------------------------------------------------')
print('    Plot ECDF')
print('--------------------------------------------------------')

max_toulouse_pop = df_toulouse_pop.max()
max_agglo_pop = df_agglomeration_pop.max()

df_toulouse_pop_percent = df_toulouse_pop / max_toulouse_pop * 100
df_agglomeration_pop_percent = df_agglomeration_pop / max_agglo_pop * 100

x_toulouse_pop,y_toulouse_pop = ecdf(df_toulouse_pop_percent)
x_agglo_pop,y_agglo_pop = ecdf(df_agglomeration_pop_percent)
 
# Plot the ECDFs
_ = plt.plot(x_toulouse_pop, y_toulouse_pop, marker='.', linestyle='none')
_ = plt.plot(x_agglo_pop, y_agglo_pop, marker='.', linestyle='none')

# Set margins
_ = plt.margins(0.02)

# Add axis labels and legend
_ = plt.xlabel('Population')
_ = plt.ylabel('ECDF')
_ = plt.legend(('Toulouse', 'Agglomération'), loc='upper left')

# Show the plot
plt.show()

print('--------------------------------------------------------')
print('    Plot comparaison between cies and population')
print('--------------------------------------------------------')

_ = plt.plot(df_toulouse_pop, marker='.', linestyle='none')
_ = plt.plot(df_agglomeration_pop, marker='.', linestyle='none')

_ = plt.xlabel('years')
_ = plt.ylabel('population')
_ = plt.title('Toulouse vs Agglomeration Toulousaine - population growth since 1968')
_ = plt.legend(('Toulouse','Agglomération toulousaine'),loc='lower right')
plt.show()