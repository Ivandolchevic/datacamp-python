'''
Created on Aug 9, 2017

@author: idolchevic
'''
print("---------------------------------------------------")
print("      Loading and viewing your data")
print("---------------------------------------------------")

# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings.csv')
df_subset = pd.read_csv('dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())
#df[:12846].to_csv('dob_job_application_filings_subset.csv')

#df_subset = pd.read_csv('dob_job_application_filings_subset.csv')
#print(df_subset.shape)
# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

print(df.head().loc[:,['Initial Cost','Total Est. Fee']])
df_subset['initial_cost'] = list(map((lambda cost:float(cost[1:])),df_subset['Initial Cost'])) 
df_subset['total_est_fee'] = list(map((lambda cost:float(cost[1:])),df_subset['Total Est. Fee']))

# Print the head and tail of df_subset
#print(df_subset.head())
#print(df_subset.tail())



print("---------------------------------------------------")
print("    Further diagnosis  ")
print("---------------------------------------------------")

# Print the info of df
print(df.info())

# Print the info of df_subset
print(df_subset.info())



print("---------------------------------------------------")
print("    Frequency counts for categorical data  ")
print("---------------------------------------------------")

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))



print("---------------------------------------------------")
print("    Visualizing single variables with histograms  ")
print("---------------------------------------------------")

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot the histogram
df_subset['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()


print("---------------------------------------------------")
print("    Visualizing multiple variables with boxplots  ")
print("---------------------------------------------------")

# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create the boxplot
df_subset.boxplot(column='initial_cost', by='Borough', rot=90)

# Display the plot
plt.show()



print("---------------------------------------------------")
print("    Visualizing multiple variables with scatter plots  ")
print("---------------------------------------------------")

# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create and display the first scatter plot
df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

# Create and display the second scatter plot
df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()


