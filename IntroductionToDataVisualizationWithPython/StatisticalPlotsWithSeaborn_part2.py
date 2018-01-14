'''
Created on Aug 22, 2017

@author: idolchevic
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

auto = pd.read_csv('auto-mpg.csv')

print("---------------------------------------------------")
print("   Plotting joint distributions (1) ")
print("---------------------------------------------------")

# Generate a joint plot of 'hp' and 'mpg'
sns.jointplot(x='hp',y='mpg',data=auto)

# Display the plot
plt.show()



print("---------------------------------------------------")
print("   Plotting joint distributions (2) ")
print("---------------------------------------------------")

# Generate a joint plot of 'hp' and 'mpg' using a hexbin plot
sns.jointplot(x='hp',y='mpg',data=auto,kind='hex')

# Display the plot
plt.show()




print("---------------------------------------------------")
print("   Plotting distributions pairwise (1) ")
print("---------------------------------------------------")

# Print the first 5 rows of the DataFrame
print(auto.head())

# Plot the pairwise joint distributions from the DataFrame 
sns.pairplot(auto)

# Display the plot
plt.show()




print("---------------------------------------------------")
print("   Plotting distributions pairwise (2) ")
print("---------------------------------------------------")


# Print the first 5 rows of the DataFrame
print(auto.head())

# Plot the pairwise joint distributions grouped by 'origin' along with regression lines
sns.pairplot(auto,kind='reg',hue='origin')

# Display the plot
plt.show()


print("---------------------------------------------------")
print("   Visualizing correlations with a heatmap ")
print("---------------------------------------------------")


# Print the covariance matrix
print(cov_matrix)

# Visualize the covariance matrix using a heatmap
____

# Display the heatmap
plt.show()



print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")





print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")





