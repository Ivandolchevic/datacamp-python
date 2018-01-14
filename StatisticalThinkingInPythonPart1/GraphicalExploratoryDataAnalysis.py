'''
Created on Aug 25, 2017

@author: idolchevic
'''
import pandas as pd


print("---------------------------------------------------")
print("   Plotting a histogram of iris data ")
print("---------------------------------------------------")


versicolor_petal_length = [4.7000000000000002, 4.5, 4.9000000000000004, 4.0, 4.5999999999999996, 4.5, 4.7000000000000002, 3.2999999999999998, 4.5999999999999996, 3.8999999999999999, 3.5, 4.2000000000000002, 4.0, 4.7000000000000002, 3.6000000000000001, 4.4000000000000004, 4.5, 4.0999999999999996, 4.5, 3.8999999999999999, 4.7999999999999998, 4.0, 4.9000000000000004, 4.7000000000000002, 4.2999999999999998, 4.4000000000000004, 4.7999999999999998, 5.0, 4.5, 3.5, 3.7999999999999998, 3.7000000000000002, 3.8999999999999999, 5.0999999999999996, 4.5, 4.5, 4.7000000000000002, 4.4000000000000004, 4.0999999999999996, 4.0, 4.4000000000000004, 4.5999999999999996, 4.0, 3.2999999999999998, 4.2000000000000002, 4.2000000000000002, 4.2000000000000002, 4.2999999999999998, 3.0, 4.0999999999999996]

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
plt.hist(versicolor_petal_length)

# Show histogram
plt.show()




print("---------------------------------------------------")
print("   Axis labels! ")
print("---------------------------------------------------")


# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)

# Label axes
plt.xlabel('petal length (cm)')
plt.ylabel('count')

# Show histogram
plt.show()


print("---------------------------------------------------")
print("  Adjusting the number of bins in a histogram  ")
print("---------------------------------------------------")


# Import numpy
import numpy as np

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Plot the histogram
plt.hist(versicolor_petal_length, bins=n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()


print("---------------------------------------------------")
print("   Bee swarm plot ")
print("---------------------------------------------------")

df = pd.read_csv('iris.csv')

# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x='species', y='petal length (cm)', data=df)
# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')

# Show the plot
plt.show()



print("---------------------------------------------------")
print("   Computing the ECDF ")
print("---------------------------------------------------")

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y



print("---------------------------------------------------")
print("   Plotting the ECDF ")
print("---------------------------------------------------")

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

print(x_vers, '\n\n\n',y_vers)
# Generate plot
plt.plot(x_vers, y_vers, marker='.', linestyle = 'none')

# Make the margins nice
plt.margins(0.02)

# Label the axes
plt.xlabel('versicolor')
plt.ylabel('ECDF')


# Display the plot
plt.show()



print("---------------------------------------------------")
print("  Comparison of ECDFs  ")
print("---------------------------------------------------")

setosa_petal_length = [1.3999999999999999, 1.3999999999999999, 1.3, 1.5, 1.3999999999999999, 1.7, 1.3999999999999999, 1.5, 1.3999999999999999, 1.5, 1.5, 1.6000000000000001, 1.3999999999999999, 1.1000000000000001, 1.2, 1.5, 1.3, 1.3999999999999999, 1.7, 1.5, 1.7, 1.5, 1.0, 1.7, 1.8999999999999999, 1.6000000000000001, 1.6000000000000001, 1.5, 1.3999999999999999, 1.6000000000000001, 1.6000000000000001, 1.5, 1.5, 1.3999999999999999, 1.5, 1.2, 1.3, 1.5, 1.3, 1.5, 1.3, 1.3, 1.3, 1.6000000000000001, 1.8999999999999999, 1.3999999999999999, 1.6000000000000001, 1.3999999999999999, 1.5, 1.3999999999999999]
virginica_petal_length = [6.0, 5.0999999999999996, 5.9000000000000004, 5.5999999999999996, 5.7999999999999998, 6.5999999999999996, 4.5, 6.2999999999999998, 5.7999999999999998, 6.0999999999999996, 5.0999999999999996, 5.2999999999999998, 5.5, 5.0, 5.0999999999999996, 5.2999999999999998, 5.5, 6.7000000000000002, 6.9000000000000004, 5.0, 5.7000000000000002, 4.9000000000000004, 6.7000000000000002, 4.9000000000000004, 5.7000000000000002, 6.0, 4.7999999999999998, 4.9000000000000004, 5.5999999999999996, 5.7999999999999998, 6.0999999999999996, 6.4000000000000004, 5.5999999999999996, 5.0999999999999996, 5.5999999999999996, 6.0999999999999996, 5.5999999999999996, 5.5, 4.7999999999999998, 5.4000000000000004, 5.5999999999999996, 5.0999999999999996, 5.0999999999999996, 5.9000000000000004, 5.7000000000000002, 5.2000000000000002, 5.0, 5.2000000000000002, 5.4000000000000004, 5.0999999999999996]


# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virf = ecdf(virginica_petal_length)

# Plot all ECDFs on the same plot
_ = plt.plot(x_set, y_set, marker='.', linestyle = 'none')
_ = plt.plot(x_vers, y_vers, marker='.', linestyle = 'none')
_ = plt.plot(x_virg, y_virf, marker='.', linestyle = 'none')


# Make nice margins
plt.margins(0.02)

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()

print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")




print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")




print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")




print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")




print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")




print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")




