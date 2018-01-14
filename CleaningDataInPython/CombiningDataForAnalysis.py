'''
Created on Aug 10, 2017

@author: idolchevic
'''
import pandas as pd

uber1 = pd.read_csv('uber-raw-data-apr14.csv', nrows=99)
uber2 = pd.read_csv('uber-raw-data-may14.csv', nrows=99)
uber3 = pd.read_csv('uber-raw-data-jun14.csv', nrows=99)
 
 
print("---------------------------------------------------")
print("    Combining rows of data ")
print("---------------------------------------------------")

# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1,uber2,uber3])

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())



print("---------------------------------------------------")
print("    Combining columns of data ")
print("---------------------------------------------------")

# Concatenate ebola_melt and status_country column-wise: ebola_tidy
# ebola_tidy = pd.concat([ebola_melt,status_country],axis=1)

# Print the shape of ebola_tidy
# print(ebola_tidy.shape)

# Print the head of ebola_tidy
# print(ebola_tidy.head())



print("---------------------------------------------------")
print("   Finding files that match a pattern  ")
print("---------------------------------------------------")

# Import necessary modules
import glob
import pandas as pd

# Write the pattern: pattern
pattern = '*.csv'

# Save all file matches: csv_files
csv_files = glob.glob(pattern)

# Print the file names
print(csv_files)

# Load the second file into a DataFrame: csv2
csv2 = pd.read_csv(csv_files[1])

# Print the head of csv2
print(csv2.head())



print("---------------------------------------------------")
print("    Iterating and concatenating all matches ")
print("---------------------------------------------------")


# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in glob.glob('uber*.csv'):

    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    
    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)

# Print the shape of uber
print(uber.shape)

# Print the head of uber
print(uber.head())


print("---------------------------------------------------")
print("     1-to-1 data merge")
print("---------------------------------------------------")

# Merge the DataFrames: o2o
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print o2o
print(o2o)




print("---------------------------------------------------")
print("    Many-to-1 data merge ")
print("---------------------------------------------------")

# Merge the DataFrames: o2o
m2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print o2o
print(m2o)


print("---------------------------------------------------")
print("   Many-to-many data merge ")
print("---------------------------------------------------")

# Merge site and visited: m2m
m2m = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')

# Print the first 20 lines of m2m
print(m2m.head(20))
