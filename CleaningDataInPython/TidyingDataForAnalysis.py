'''
Created on Aug 10, 2017

@author: idolchevic
'''
import numpy as np
import pandas as pd

print("---------------------------------------------------")
print("    Recognizing tidy data")
print("---------------------------------------------------")

airquality = pd.read_csv('airquality.csv',sep=';',skiprows=1,names = ['Ozone','Solar.R','Wind','Temp','Month','Day']) 
print(airquality.head())

print("---------------------------------------------------")
print("   Reshaping your data using melt ")
print("---------------------------------------------------")

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'])

# Print the head of airquality_melt
print(airquality_melt.head())


print("---------------------------------------------------")
print("   Customizing melted data ")
print("---------------------------------------------------")

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())


print("---------------------------------------------------")
print("   Pivot data ")
print("---------------------------------------------------")

# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())


print("---------------------------------------------------")
print("   Resetting the index of a DataFrame ")
print("---------------------------------------------------")
# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the new index of airquality_pivot
print(airquality_pivot.index)

# Print the head of airquality_pivot
print(airquality_pivot.head())



print("---------------------------------------------------")
print("   Pivoting duplicate values ")
print("---------------------------------------------------")

airquality_dup = airquality_melt
 
# Pivot airquality_dup: airquality_pivot
airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the head of airquality
print(airquality.head())


print("---------------------------------------------------")
print("   Splitting a column with .str ")
print("---------------------------------------------------")

# tb = pd.read_csv('tb.csv',sep=';')

# Melt tb: tb_melt
# tb_melt = pd.melt(frame=tb, id_vars=['country', 'year'])

# Create the 'gender' column
# tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column
# tb_melt['age_group'] = tb_melt.variable.str[1:]

# Print the head of tb_melt
# print(tb_melt.head())


print("---------------------------------------------------")
print("  Splitting a column with .split() and .get()  ")
print("---------------------------------------------------")

# Melt ebola: ebola_melt
# ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

# Create the 'str_split' column
# ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

# Create the 'type' column
# ebola_melt['type'] = ebola_melt['str_split'].str.get(0)

# Create the 'country' column
# ebola_melt['country'] = ebola_melt['str_split'].str.get(1)

# Print the head of ebola_melt
# print(ebola_melt.head())
