'''
Created on Sep 8, 2017

@author: idolchevic
'''

import numpy as np

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)
    
    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n
    
    return x, y

def pearson_r(x,y):
    covariance = np.cov(x,y)
    
    std_product = np.std(x) * np.std(y)
    
    return covariance[0,1] / std_product


def bs_replicate_1d(data, func):
    bs_sample = np.random.choice(data,len(data))
    return func(bs_sample)
    
def draw_bs_pairs_linreg(x,y,size):
    inds = np.arange(len(x))    
    
    bs_slopes = np.empty(size)
    bs_intercepts  = np.empty(size)
    
    for i in range(size):
        bs_inds = np.random.choice(inds, len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_slopes[i],bs_intercepts[i] = np.polyfit(bs_x,bs_y,1)
        
    return bs_slopes, bs_intercepts

def permuatation_sample(data_1, data_2):
    '''draw a permutation simple from two datasets'''
    
    # concatenate the datas 
    concatenated_datas = np.concatenate((data_1, data_2))
    
    # permute the values
    permutated_values = np.random.permutation(concatenated_datas)
    
    # get the two permuted samples
    perm_sample_1 = permutated_values[:len(data_1)]
    perm_sample_2 = permutated_values[len(data_2):]
    
    return perm_sample_1,perm_sample_2
    
def diff_of_means(data_1, data_2):
    '''return the difference of the means of two datasets'''
    return np.mean(data_1) - np.mean(data_2)

def draw_perm_reps(data_1,data_2,func,size=10000):
    '''draw a permutation simple from two datasets'''
       
    # permutation replicates 
    perm_reps = np.empty(size)
    
    # get the two permuted samples
    for i in range(size):
        perm_sample_1,perm_sample_2 = permuatation_sample(data_1, data_2)
        
        # calculate the permutation replicate
        perm_reps[i] = func(perm_sample_1,perm_sample_2)                
    
    return perm_reps

def draw_bs_reps(data, func, size):
    ''' draw boootstrap replicates for of the data'''
    bs_replicates = np.empty(size)
    
    for i in range(size):
        bs_replicates[i] = bs_replicate_1d(data, func)
        
    return bs_replicates