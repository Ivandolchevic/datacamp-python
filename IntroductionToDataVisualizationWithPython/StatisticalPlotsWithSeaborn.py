'''
Created on Aug 22, 2017

@author: idolchevic
'''

import pandas as pd

print("---------------------------------------------------")
print("   Simple linear regressions")
print("---------------------------------------------------")

auto = pd.read_csv('auto-mpg.csv')

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Plot a linear regression between 'weight' and 'hp'
sns.lmplot(x='weight', y='hp', data=auto)

# Display the plot
plt.show()




print("---------------------------------------------------")
print("   Plotting residuals of a regression ")
print("---------------------------------------------------")

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto, color='green')

# Display the plot
plt.show()




print("---------------------------------------------------")
print("   Higher-order regressions ")
print("---------------------------------------------------")
print(auto.head())
# Generate a scatter plot of 'weight' and 'mpg' using red circles
plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')

# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, color='blue', label='order 1')

# Plot in green a linear regression of order 2 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, color='green', label='order 2', order=2)

# Add a legend and display the plot
plt.legend(loc='upper right')
plt.show()




print("---------------------------------------------------")
print("   Grouping linear regressions by hue ")
print("---------------------------------------------------")

# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(x='weight', y='hp', data=auto, hue='origin',palette='Set1')

# Display the plot
plt.show()




print("---------------------------------------------------")
print("   Grouping linear regressions by row or column ")
print("---------------------------------------------------")

# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(x='weight', y='hp', data=auto, row='origin')

# Display the plot
plt.show()




print("---------------------------------------------------")
print("   Constructing strip plots ")
print("---------------------------------------------------")


# Make a strip plot of 'hp' grouped by 'cyl'
plt.subplot(2,1,1)
sns.stripplot(x='cyl', y='hp', data=auto)

# Make the strip plot again using jitter and a smaller point size
plt.subplot(2,1,2)
sns.stripplot(x='cyl', y='hp', data=auto, jitter=True, size=3)

# Display the plot
plt.show()



print("---------------------------------------------------")
print("   Constructing swarm plots ")
print("---------------------------------------------------")


# Generate a swarm plot of 'hp' grouped horizontally by 'cyl'  
plt.subplot(2,1,1)
sns.swarmplot(x='cyl', y='hp', data=auto)

# Generate a swarm plot of 'hp' grouped vertically by 'cyl' with a hue of 'origin'
plt.subplot(2,1,2)
sns.swarmplot(x='hp', y='cyl', data=auto,orient='h', hue='origin')

# Display the plot
plt.show()



print("---------------------------------------------------")
print("   Constructing violin plots ")
print("---------------------------------------------------")

# Generate a violin plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.violinplot(x='cyl', y='hp', data=auto)

# Generate the same violin plot again with a color of 'lightgray' and without inner annotations
plt.subplot(2,1,2)
sns.violinplot(x='cyl', y='hp', data=auto, inner=None,color='lightgray')

# Overlay a strip plot on the violin plot
sns.stripplot(x='cyl', y='hp', data=auto, jitter=True, size=1.5)

# Display the plot
plt.show()

