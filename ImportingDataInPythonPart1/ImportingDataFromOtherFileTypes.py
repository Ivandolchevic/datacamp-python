'''
Created on Aug 8, 2017

@author: idolchevic
'''

import matplotlib.pyplot as plt

print("---------------------------------------------------")
print("      Not so flat any more")
print("---------------------------------------------------")

#import os
#wd = os.getcwd()
#os.listdir(wd)



print("---------------------------------------------------")
print("      Loading a pickled file")
print("---------------------------------------------------")

# Import pickle package
#import pickle

# Open pickle file and load data: d
#with open('data.pkl', 'rb') as file:
#    d = pickle.load(file)

# Print d
#print(d)

# Print datatype of d
#print(type(d))


print("---------------------------------------------------")
print("      Listing sheets in Excel files")
print("---------------------------------------------------")
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)




print("---------------------------------------------------")
print("     Importing sheets from Excel files ")
print("---------------------------------------------------")

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)

# Print the head of the DataFrame df2
print(df2.head())



print("---------------------------------------------------")
print("      ")
print("---------------------------------------------------")
# Parse the first sheet and rename the columns: df1
#df1 = xl.parse(xl.sheet_names[0], skiprows=1, names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
#print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
#df2 = xl.parse(xl.sheet_name[1], parse_cols=1, skiprows=1, names=['Country'])

# Print the head of the DataFrame df2
#print(df2.head())


# Parse the first sheet and rename the columns: df1
#df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
#print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
#df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names='Country')

# Print the head of the DataFrame df2
#print(df2.head())

print("---------------------------------------------------")
print("     Importing SAS files ")
print("---------------------------------------------------")
# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('airline.sas7bdat') as file:
    df_sas = SAS7BDAT.to_data_frame(file)

print(df_sas.head())

pd.DataFrame.hist(df_sas[['L']])
plt.ylabel('count')
plt.show()

print("---------------------------------------------------")
print("      Using read_stata to import Stata files")
print("---------------------------------------------------")
df = pd.read_stata('disarea.dta')
print(df.head())

print("---------------------------------------------------")
print("      Importing Stata files")
print("---------------------------------------------------")

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of coutries')
plt.show()


print("---------------------------------------------------")
print("      Using h5py to import HDF5 files")
print("---------------------------------------------------")

# Import packages
import numpy as np
import h5py

# Assign filename: file
filename = 'H-H2_LOSC_4_V1-815341568-4096.hdf5'

# Load file: data
data = h5py.File(filename,'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)


print("---------------------------------------------------")
print("     Extracting data from your HDF5 file ")
print("---------------------------------------------------")
# Assign filename: file
filename = 'H-H2_LOSC_4_V1-815341568-4096.hdf5'

# Load file: data
data = h5py.File(filename,'r')

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.title("Extracting data from your HDF5 file")
plt.show()





print("---------------------------------------------------")
print("      Loading .mat files")
print("---------------------------------------------------")
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))



print("---------------------------------------------------")
print("     The structure of .mat in Python ")
print("---------------------------------------------------")

# Print the keys of the MATLAB dictionary
for key in mat.keys():
    print(key)

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()




