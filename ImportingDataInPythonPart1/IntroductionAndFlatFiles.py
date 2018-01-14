'''
Created on Aug 8, 2017

@author: idolchevic
'''

print("---------------------------------------------------")
print("      Importing different datatypes")
print("---------------------------------------------------")

import numpy as np
import matplotlib.pyplot as plt

# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
#plt.show()

print("---------------------------------------------------")
print("     Working with mixed datatypes (1) ")
print("---------------------------------------------------")

data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)
print(data)

print("---------------------------------------------------")
print("      Working with mixed datatypes (2)")
print("---------------------------------------------------")

# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file,delimiter=',',names=True)

# Print out first three entries of d
print(d[:3])

print("---------------------------------------------------")
print("      Using pandas to import flat files as DataFrames (1)")
print("---------------------------------------------------")
# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())

print("---------------------------------------------------")
print("      Using pandas to import flat files as DataFrames (2)")
print("---------------------------------------------------")
# Assign the filename: file
file = 'digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5,header=None)

# Build a numpy array from the DataFrame: data_array
data_array = np.array(data.values,dtype=None)

# Print the datatype of data_array to the shell
print(type(data_array))




print("---------------------------------------------------")
print("     Customizing your pandas import ")
print("---------------------------------------------------")

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()


print("---------------------------------------------------")
print("      ")
print("---------------------------------------------------")



print("---------------------------------------------------")
print("      ")
print("---------------------------------------------------")



