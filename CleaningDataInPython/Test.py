'''
Created on Aug 10, 2017

@author: idolchevic
'''
# Import pandas
import pandas as pd

df_subset = pd.read_csv('dob_job_application_filings_subset.csv')


df_subset['initial_cost'] = list(map((lambda cost:float(cost[1:])),df_subset['Initial Cost']))
df_subset['total_est_fee'] = list(map((lambda cost:float(cost[1:])),df_subset['Total Est. Fee']))

print(df_subset.columns)
print(df_subset.head()[['Initial Cost','initial_cost']])
print(df_subset.head()[['Total Est. Fee','total_est_fee']])

print("---------------------------------------------------")
print("    Gapeminder ")
print("---------------------------------------------------")
g1800s = pd.read_csv('gapminder.csv')
print(g1800s.shape)
print(" before ...")                                      
print(g1800s.iloc[4])
print(" and now ...")
print(g1800s.iloc[4].dropna())


print("---------------------------------------------------")
print("    Trash ")
print("---------------------------------------------------")

import numpy as np
z = np.array([[1, 2, 3], 
              [17, 18, 19]])
print(np.transpose(z))
