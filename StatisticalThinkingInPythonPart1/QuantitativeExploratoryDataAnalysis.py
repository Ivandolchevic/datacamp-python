'''
Created on Aug 25, 2017

@author: idolchevic
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


versicolor_petal_length = [4.7000000000000002, 4.5, 4.9000000000000004, 4.0, 4.5999999999999996, 4.5, 4.7000000000000002, 3.2999999999999998, 4.5999999999999996, 3.8999999999999999, 3.5, 4.2000000000000002, 4.0, 4.7000000000000002, 3.6000000000000001, 4.4000000000000004, 4.5, 4.0999999999999996, 4.5, 3.8999999999999999, 4.7999999999999998, 4.0, 4.9000000000000004, 4.7000000000000002, 4.2999999999999998, 4.4000000000000004, 4.7999999999999998, 5.0, 4.5, 3.5, 3.7999999999999998, 3.7000000000000002, 3.8999999999999999, 5.0999999999999996, 4.5, 4.5, 4.7000000000000002, 4.4000000000000004, 4.0999999999999996, 4.0, 4.4000000000000004, 4.5999999999999996, 4.0, 3.2999999999999998, 4.2000000000000002, 4.2000000000000002, 4.2000000000000002, 4.2999999999999998, 3.0, 4.0999999999999996]

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y


# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)
df = pd.read_csv('iris.csv')

sns.set()

print("---------------------------------------------------")
print("   Computing means ")
print("---------------------------------------------------")

# Compute the mean: mean_length_vers
mean_length_vers = np.mean(versicolor_petal_length)
# Print the result with some nice formatting
print('I. versicolor:', mean_length_vers, 'cm')


print("---------------------------------------------------")
print("   Computing percentiles ")
print("---------------------------------------------------")


# Specify array of percentiles: percentiles
percentiles = np.array([ 2.5,25,50,75,97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

# Print the result
print(ptiles_vers)

print("---------------------------------------------------")
print("   Comparing percentiles to ECDF ")
print("---------------------------------------------------")

# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
plt.margins(0.02)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',
         linestyle='none')

# Show the plot
plt.show()




print("---------------------------------------------------")
print("   Box-and-whisker plot ")
print("---------------------------------------------------")

# Create box plot with Seaborn's default settings
_ = sns.boxplot(x='species', y='petal length (cm)', data=df)


# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')

# Show the plot
plt.show()



print("---------------------------------------------------")
print("   Computing the variance ")
print("---------------------------------------------------")

# Array of differences to mean: differences
differences = versicolor_petal_length - np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq = differences ** 2 

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length)

# Print the results
print(variance_explicit,variance_np)



print("---------------------------------------------------")
print("  The standard deviation and the variance  ")
print("---------------------------------------------------")

# Compute the variance: variance
variance = np.var(versicolor_petal_length)

# Print the square root of the variance
print(np.sqrt(variance))

# Print the standard deviation
print(np.std(versicolor_petal_length))



print("---------------------------------------------------")
print("   Scatter plots ")
print("---------------------------------------------------")
versicolor_petal_length = np.array(df['petal length (cm)'])
versicolor_petal_width = np.array(df['petal width (cm)'])

# Make a scatter plot
_ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')

# Set margins
plt.margins(0.02)

# Label the axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('petal width (cm)')


# Show the result
plt.show()


print("---------------------------------------------------")
print("  Computing the covariance  ")
print("---------------------------------------------------")

# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0,1]

# Print the length/width covariance
print(petal_cov)



print("---------------------------------------------------")
print("  Computing the Pearson correlation coefficient  ")
print("---------------------------------------------------")

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x,y)

    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)

# Print the result
print(r)


