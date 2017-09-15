'''
Created on Aug 11, 2017

@author: idolchevic
'''
import pandas as pd
import matplotlib.pyplot as plt

print("---------------------------------------------------")
print("     Inspecting your data")
print("---------------------------------------------------")

df = pd.read_csv('world_ind_pop_data.csv')

print(df.shape)
print(df.head(1).loc[:,['Year','Total Population']])
print(df.tail(1).loc[:,['Year','Total Population']])


print("---------------------------------------------------")
print("    DataFrame data types ")
print("---------------------------------------------------")

print(df.info())


print("---------------------------------------------------")
print("    NumPy and pandas working together ")
print("---------------------------------------------------")


df = df.head(6).loc[:,['Year','Total Population']]

# Import numpy
import numpy as np

# Create array of DataFrame values: np_vals
np_vals = df.values

# Create new array of base 10 logarithm values: np_vals_log10
np_vals_log10 = np.log10(np_vals)

# Create array of new DataFrame by passing df to np.log10(): df_log10
df_log10 = np.log10(df)

# Print original and new data containers
print(type(np_vals), type(np_vals_log10))
print(type(df), type(df_log10))



print("---------------------------------------------------")
print("    Zip lists to build a DataFrame ")
print("---------------------------------------------------")

list_keys = ['Country', 'Total']
list_values = [['United States', 'Soviet Union', 'United Kingdom'], [1118, 473, 273]]

# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)


print("---------------------------------------------------")
print("   Labeling your data  ")
print("---------------------------------------------------")

list_keys = ['a', 'b', 'c' ,'d']
list_values = [[1980,1981,1982],['Blondie', 'Chistorpher Cross', 'Joan Jett'],['Call Me','Arthurs Theme  3', 'I Love Rock and Roll'],[6,3,7]]
df = pd.DataFrame(dict(list(zip(list_keys, list_values))))

# Build a list of labels: list_labels
list_labels = ['year', 'artist', 'song', 'chart weeks']

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels

print(df)

print("---------------------------------------------------")
print("    Building DataFrames with broadcasting ")
print("---------------------------------------------------")

cities = ['Manheim',
 'Preston park',
 'Biglerville',
 'Indiana',
 'Curwensville',
 'Crown',
 'Harveys lake',
 'Mineral springs',
 'Cassville',
 'Hannastown',
 'Saltsburg',
 'Tunkhannock',
 'Pittsburgh',
 'Lemasters',
 'Great bend']

# Make a string with the value 'PA': state
state = 'PA'

# Construct a dictionary: data
data = {'state':state, 'city':cities}

# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)

# Print the DataFrame
print(df)



print("---------------------------------------------------")
print("   Reading a flat file  ")
print("---------------------------------------------------")

# Read in the file: df1
df1 = pd.read_csv('world_population.csv')

# Create a list of the new column labels: new_labels
new_labels = ['year', 'population']

# Read in the file, specifying the header and names parameters: df2
df2 = pd.read_csv('world_population.csv', header=0, names=new_labels)

# Print both the DataFrames
print(df1)
print(df2)

file_messy = 'messy_stock_data.tsv'
file_clean = 'tmp_clean_stock_data.csv'

print("---------------------------------------------------")
print("    Delimiters, headers, and extensions ")
print("---------------------------------------------------")

# Read the raw file as-is: df1
df1 = pd.read_csv(file_messy)

# Print the output of df1.head()
print(df1.head(5))

# Read in the file with the correct parameters: df2
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')

# Print the output of df2.head()
print(df2.head())

# Save the cleaned up DataFrame to a CSV file without the index
df2.to_csv(file_clean, index=False)

# Save the cleaned up DataFrame to an excel file without the index
df2.to_excel('file_clean.xlsx', index=False)



print("---------------------------------------------------")
print("    Plotting series using pandas ")
print("---------------------------------------------------")

list_keys = ['Temperature (deg F)']
list_values = [[79. ,77.4,76.4,75.7,75.1,74.6,74.5,76. ,79.8,83.3,86.6,89.3,91.6,93.2,94.4,95. ,94.8,93.9,92.4,89.9,86.1,83.6,81.8,80. ,79.1,77.4,76.5,75.8,75.2,74.6,74.6,76.1,79.8,83.3,86.5,89.4,91.6,93.2,94.4,95. ,94.8,93.9,92.4,89.8,86.1,83.6,81.8,80.1,79.1,77.5,76.5,75.8,75.2,74.6,74.5,76. ,79.8,83.4,86.6,89.4,91.7,93.3,94.5,95.1,94.9,94.1,92.5,89.8,86. ,83.5,81.9,80.1,79.2,77.6,76.6,75.9,75.3,74.7,74.6,76. ,79.9,83.5,86.7,89.5,91.9,93.4,94.6,95.1,95. ,94.1,92.5,89.7,86. ,83.5,81.9,80.2,79.2,77.6,76.6,75.9,75.3,74.7,74.6,76.1,79.8,83.4,86.6,89.5,91.9,93.4,94.5,95.1,94.9,94.1,92.4,89.6,85.9,83.4,81.8,80.1,79.2,77.6,76.6,75.9,75.3,74.6,74.6,76. ,79.7,83.4,86.6,89.5,91.8,93.4,94.5,95.2,95. ,94.1,92.5,89.6,85.9,83.4,81.8,80. ,79.2,77.5,76.5,75.8,75.2,74.6,74.6,76. ,79.7,83.3,86.5,89.4,91.8,93.4,94.5,95.3,95. ,94.1,92.4,89.5,85.8,83.3,81.7,80. ,79.2,77.5,76.5,75.8,75.2,74.6,74.6,75.9,79.7,83.3,86.5,89.4,91.7,93.3,94.5,95.2,94.9,94.1,92.4,89.5,85.7,83.3,81.7,80. ,79.2,77.5,76.5,75.8,75.2,74.6,74.6,75.9,79.7,83.3,86.4,89.4,91.7,93.3,94.5,95.2,94.9,94.1,92.2,89.3,85.6,83.2,81.6,79.9,79.1,77.4,76.4,75.8,75.2,74.6,74.6,75.9,79.6,83.3,86.4,89.4,91.7,93.2,94.4,95.1,94.8,94.1,92.3,89.2,85.6,83.2,81.6,79.9,79.1,77.4,76.5,75.8,75.3,74.7,74.6,75.9,79.6,83.3,86.4,89.3,91.7,93.2,94.4,95. ,94.7,94. ,92.1,89. ,85.5,83.1,81.6,80. ,79.2,77.5,76.5,75.8,75.3,74.8,74.7,75.9,79.6,83.2,86.4,89.2,91.6,93.1,94.4,94.9,94.7,94. ,92.1,89. ,85.5,83.2,81.7,80.1,79.2,77.5,76.6,75.9,75.4,74.8,74.7,75.9,79.6,83.2,86.4,89.3,91.6,93.2,94.4,95. ,94.8,94.1,92.3,89.2,85.7,83.4,81.7,80.2,79.2,77.5,76.5,75.9,75.4,74.9,74.7,75.9,79.5,83.1,86.3,89.2,91.5,93.1,94.3,94.9,94.7,94. ,92.1,89. ,85.6,83.3,81.6,80.1,79.1,77.4,76.4,75.8,75.3,74.8,74.7,75.8,79.5,83.1,86.2,89.1,91.4,93. ,94.2,94.7,94.6,93.9,91.9,88.8,85.5,83.3,81.6,80. ,79.1,77.4,76.5,75.9,75.3,74.8,74.7,75.8,79.4,83.1,86.2,89. ,91.4,93. ,94.2,94.7,94.6,94. ,92. ,88.9,85.5,83.4,81.7,80.1,79.2,77.5,76.6,75.9,75.3,74.8,74.8,75.9,79.5,83.2,86.3,89.1,91.5,93.1,94.3,94.8,94.6,94. ,92. ,88.8,85.5,83.3,81.6,80.1,79.2,77.5,76.6,75.9,75.4,74.9,74.8,75.9,79.5,83.1,86.3,89.1,91.5,93.1,94.3,94.8,94.6,93.9,91.9,88.8,85.6,83.4,81.7,80.1,79.2,77.5,76.6,75.9,75.3,74.9,74.8,75.8,79.5,83.1,86.3,89.1,91.5,93.1,94.3,94.8,94.7,94. ,92.1,88.9,85.7,83.5,81.7,80.2,79.2,77.6,76.6,75.9,75.3,74.8,74.7,75.8,79.5,83.2,86.4,89.2,91.5,93.2,94.4,94.8,94.7,94.1,92.1,88.9,85.7,83.5,81.8,80.2,79.3,77.6,76.6,75.9,75.3,74.8,74.7,75.7,79.4,83.1,86.3,89.1,91.4,93.1,94.3,94.7,94.6,94. ,92. ,88.7,85.5,83.4,81.7,80.1,79.2,77.5,76.5,75.8,75.2,74.8,74.7,75.6,79.4,83. ,86.3,89. ,91.4,93. ,94.2,94.6,94.6,93.8,91.7,88.5,85.4,83.3,81.6,80. ,79.1,77.4,76.5,75.7,75.1,74.6,74.5,75.5,79.2,82.9,86.2,88.9,91.3,92.8,94. ,94.5,94.5,93.7,91.6,88.3,85.2,83.1,81.4,79.9,78.9,77.3,76.4,75.7,75. ,74.5,74.4,75.4,79.2,82.9,86.2,88.8,91.1,92.7,93.9,94.3,94.3,93.5,91.5,88.2,85.1,83. ,81.3,79.7,78.9,77.3,76.4,75.6,74.9,74.5,74.3,75.3,79.1,82.7,86. ,88.7,91. ,92.6,93.8,94.1,94. ,93.2,91.2,87.9,84.9,82.7,81. ,79.6,78.8,77.2,76.2,75.5,74.8,74.4,74.2,75.2,79. ,82.6,85.9,88.6,90.9,92.4,93.6,94. ,93.9,93. ,91. ,87.8,84.7,82.6,81. ,79.4,78.6,77. ,76.2,75.4,74.7,74.2,74.1,75. ,78.9,82.6,85.8,88.6,90.8,92.3,93.3,93.7,93.6,92.7,90.7,87.5,84.4,82.2,80.7,79.2,78.4,76.9,76. ,75.3,74.6,74.1,74. ,74.9,78.7,82.4,85.7,88.4,90.6,92.1,93.1,93.5,93.3,92.3,90.3,87.1,84.1,81.9,80.4,78.9,78.2,76.7,75.9,75.1,74.5,74. ,73.8,74.7,78.5,82.2,85.5,88.2,90.4,91.9,92.9,93.3,93.2,92.2,90.1,86.9,83.9,81.7,80.1,78.7,78. ,76.5,75.7,74.9,74.3,73.7,73.7,74.5,78.3,82.1,85.4,88.1,90.4,91.8,92.8,93.3,93.1,92.1,90. ,86.8,83.7,81.5,79.9,78.4,77.8,76.3,75.5,74.7,74.1,73.5,73.4,74.3,78.1,81.9,85.2,87.9,90.1,91.6,92.6,93.1,93. ,91.9,89.8,86.6,83.4,81.2,79.7,78.2]]
df = pd.DataFrame(dict(list(zip(list_keys, list_values))))
print(df)
# Create a plot with color='red'
df.plot(color='red')

# Add a title
plt.title('Temperature in Austin')

# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')

# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')

# Display the plot
plt.show()

print("---------------------------------------------------")
print("    Plotting DataFrames ")
print("---------------------------------------------------")

df = pd.read_csv('weather_data_austin_2010_cpy.csv')

# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots=True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['Dew Point (deg F)']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature (deg F)','Dew Point (deg F)']
df[column_list2].plot()
plt.show()


