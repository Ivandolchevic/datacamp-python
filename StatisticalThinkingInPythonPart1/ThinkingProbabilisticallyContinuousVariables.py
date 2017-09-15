'''
Created on Aug 25, 2017

@author: idolchevic
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

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
print("   The Normal PDF ")
print("---------------------------------------------------")

# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
samples_std1 = np.random.normal(20, 1, size=100000) 
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 =  np.random.normal(20, 10, size=100000)


# Make histograms
plt.hist(samples_std1,bins=100, normed=True, histtype='step')
plt.hist(samples_std3,bins=100, normed=True, histtype='step')
plt.hist(samples_std10,bins=100, normed=True, histtype='step')

# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()



print("---------------------------------------------------")
print("  The Normal CDF  ")
print("---------------------------------------------------")

# Generate CDFs
x_std1, y_std1 = ecdf(samples_std1)
x_std3, y_std3 = ecdf(samples_std3) 
x_std10, y_std10 = ecdf(samples_std10)

# Plot CDFs
plt.plot(x_std1, y_std1, marker='.',linestyle='none')
plt.plot(x_std3, y_std3, marker='.',linestyle='none')
plt.plot(x_std10, y_std10, marker='.',linestyle='none')

# Make 2% margin
plt.margins(0.02)

# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()



print("---------------------------------------------------")
print("  Are the Belmont Stakes results Normally distributed?  ")
print("---------------------------------------------------")
def time_to_sec(t):
    return float(str(int(t.split(':')[0]) * 60 + int(t.split('.')[0].split(':')[1])) + '.' + str(int(t.split('.')[0].split(':')[1])))

df = pd.read_csv('belmont.csv')
belmont_no_outliers = df[(df.Year != 1970) & (df.Year != 1973)]['Time'].map(time_to_sec).values

# Compute mean and standard deviation: mu, sigma
mu = np.mean(belmont_no_outliers)
sigma = np.std(belmont_no_outliers) 

# Sample out of a normal distribution with this mu and sigma: samples
samples = np.random.normal(mu,sigma,10000)

# Get the CDF of the samples and of the data
x_theor, y_theor = ecdf(samples)
x, y = ecdf(belmont_no_outliers)

# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('Belmont winning time (sec.)')
_ = plt.ylabel('CDF')
plt.show()

print("---------------------------------------------------")
print("   What are the chances of a horse matching or beating Secretariat's record? ")
print("---------------------------------------------------")

# Take a million samples out of the Normal distribution: samples
samples = np.random.normal(mu,sigma,1000000)

# Compute the fraction that are faster than 144 seconds: prob
prob = len(samples[samples < 144]) / len(samples) 

# Print the result
print('Probability of besting Secretariat:', prob)



print("---------------------------------------------------")
print("   If you have a story, you can simulate it! ")
print("---------------------------------------------------")


def successive_poisson(tau1, tau2, size=1):
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size)

    return t1 + t2

print("---------------------------------------------------")
print("   Distribution of no-hitters and cycles ")
print("---------------------------------------------------")


# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764,715,100000)

# Make the histogram
plt.hist(waiting_times,bins=100, normed=True,  histtype='step')


# Label axes
plt.xlabel('waiting time')
plt.ylabel('PDF')


# Show the plot
plt.show()


x, y = ecdf(waiting_times)
# Plot the CDFs and show the plot
_ = plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('Waiting time')
_ = plt.ylabel('CDF')
plt.show()