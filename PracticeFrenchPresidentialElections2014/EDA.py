'''
Created on Sep 7, 2017

@author: idolchevic
'''
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import seaborn as sns
import statfunc.distribution as disfunc
from statfunc.distribution import draw_perm_reps
from scipy.special.basic import perm


sns.set()
np.random.seed(42)

filesnames = glob.glob("*.csv")

def explore_file():
    # check file format 
    with open(filesnames[0], 'r', encoding = "ISO-8859-1") as file:
        for _ in range(10):
            print(file.readline())

# read the file using the right separator
df = pd.read_csv(filesnames[0],sep=';', encoding = "ISO-8859-1",skiprows=1)

def explore_dataframe():
    print('\ndataframe:\n',df.head(),'\nformat:',df.info())

def convert_string_to_float(value):
    return float(str(value).replace(',','.').strip())

def convert_string_to_int(value):
    return int(''.join(re.findall('[0-9]',value)))    

# create a new DataFrame with all votes results
df_votes = pd.DataFrame(df['CC'])
df_votes['lepen'] = df['%Mme Marine LE PEN'].map(convert_string_to_float)
df_votes['macron'] = df['%M. Emmanuel MACRON'].map(convert_string_to_float)
df_votes['melenchon'] = df['%M. Jean-Luc MÉLENCHON'].map(convert_string_to_float)
df_votes['fillon'] = df['%M. François FILLON'].map(convert_string_to_float)
df_votes.dropna(inplace=True)

def calculate_total_count_df():
    df_total_votes = pd.DataFrame(df['CC'])
    df_total_votes['lepen'] = df['Mme Marine LE PEN - TOTAL'].map(convert_string_to_int)
    df_total_votes['macron'] = df['M. Emmanuel MACRON - TOTAL'].map(convert_string_to_int)
    df_total_votes['melenchon'] = df['M. Jean-Luc MÉLENCHON - TOTAL'].map(convert_string_to_int)
    df_total_votes['fillon'] = df['M. François FILLON - TOTAL'].map(convert_string_to_int)    
    df_total_votes.dropna(inplace=True)
    
    return df_total_votes



# calculate mean by counties
df_votes = df_votes.groupby('CC')['CC','lepen','macron','melenchon','fillon'].mean()

# calculate the total votes by consulate
df_total_votes = calculate_total_count_df().groupby('CC')['CC','lepen','macron','melenchon','fillon'].sum()

# pivot the table
df_votes = pd.DataFrame(df_votes.stack(level=0))
df_votes.reset_index(inplace=True)
df_votes.columns = ['CC','candidate','votes']

df_total_votes = pd.DataFrame(df_total_votes.stack(level=0))
df_total_votes.reset_index(inplace=True)
df_total_votes.columns = ['CC','candidate','total_votes']

def bee_swarm_plot():
    ''' plot the bee swarm plot '''
    _ = sns.swarmplot(x='candidate',y='votes',data=df_votes)
    _ = plt.xlabel('Candidates')
    _ = plt.ylabel('Percent votes for candidates')

    plt.show()


# get the list of results for Macron
macron_votes = np.array(list(df_votes[df_votes.candidate == 'macron']['votes']))
macron_total_votes = np.array(list(df_total_votes[df_total_votes.candidate == 'macron']['total_votes']))

# get the list of results for Melenchon
melenchon_votes = np.array(list(df_votes[df_votes.candidate == 'melenchon']['votes']))
melenchon_total_votes = np.array(list(df_total_votes[df_total_votes.candidate == 'melenchon']['total_votes']))

def ecdf_macron():
    '''Plot the cummulative distribution of votes for Macron '''
    x,y = disfunc.ecdf(macron_votes)
    _ = plt.plot(x,y,marker='.',linestyle='none')
    _ = plt.xlabel('Votes for Macron')
    _ = plt.ylabel('ECDF')
    _ = plt.title('ECDF of votes for Macron')
    
    plt.show()
    
def box_plot():
    _ = sns.boxplot(x='candidate',y='votes',data=df_votes)
    _ = plt.xlabel('candidates')
    _ = plt.ylabel('percentages of votes by CC')
    plt.show()

def macron_variance_and_standard_deviation():
    diff_from_mean = macron_votes - np.mean(macron_votes) 
    square_of_diff = diff_from_mean ** 2
    variance = np.mean(square_of_diff)
    
    print('variance custom: ',variance, '\nvariance: ',np.var(macron_votes))
        
    standard_deviation = np.sqrt(variance)

    print('standard deviation custom: ',standard_deviation, '\nstandard deviation: ',np.std(macron_votes))

def macron_scatter_plot():
    _ = plt.plot(macron_total_votes / 1000, macron_votes, marker='.', linestyle='none')
    _ = plt.xlabel('Total votes (thousands)')
    _ = plt.ylabel('Percent of votes for Macron')
    
    # plot total votes mean
    total_votes_mean =  np.full(len(macron_total_votes),np.mean(macron_total_votes))    
    _ = plt.plot(total_votes_mean / 1000,macron_votes)
    
    # plot votes mean
    votes_mean =  np.full(len(macron_votes),np.mean(macron_votes))
    _ = plt.plot(macron_total_votes / 1000,votes_mean)
    
    plt.show()

def macron_votes_covariance():
    mean_total_votes = np.mean(macron_total_votes)
    mean_votes = np.mean(macron_votes)
    
    diff_to_mean_product =  (macron_total_votes - mean_total_votes) * (macron_votes - mean_votes)    
    covariance = diff_to_mean_product.sum() / (len(diff_to_mean_product) - 1)
    
    print('\ncovariance custom : ',covariance, ',\ncovariance:\n',np.cov(macron_total_votes,macron_votes))


def macron_pearson_r():
    print('\npearson_r correlation coefficient : ',disfunc.pearson_r(macron_total_votes, macron_votes))
 

def macron_replay_firstround():
    bs_replicates = np.empty(10000)
    for i in range(10000):
        bs_replicates[i] = disfunc.bs_replicate_1d(macron_votes,np.mean)

    _ = plt.hist(bs_replicates, bins=30,normed=True)
    _ = plt.xlabel('mean percentage of votes')
    _ = plt.ylabel('PDF')
    
    plt.show()

def melenchon_replay_firstround():
    bs_replicates = np.empty(10000)
    for i in range(10000):
        bs_replicates[i] = disfunc.bs_replicate_1d(melenchon_votes,np.mean)

    _ = plt.hist(bs_replicates, bins=30,normed=True)
    _ = plt.xlabel('mean percentage of votes')
    _ = plt.ylabel('PDF')
    
    plt.show()
    
def macron_linear_bootstrap():
    bs_slopes, bs_intercepts = disfunc.draw_bs_pairs_linreg(macron_votes,macron_total_votes, 1000)
    
    for i in range(len(bs_slopes)):
        _ = plt.plot(macron_votes, bs_slopes[i]*macron_votes + bs_intercepts[i],linewidth=0.5, alpha=0.2, color='red')

    plt.show()
    
def get_df_macron():
    df_macron = pd.DataFrame(df[['Pays','CC']])    
    df_macron['macron'] = df['%M. Emmanuel MACRON'].map(convert_string_to_float)    
    df_macron.dropna(inplace=True)
    return df_macron

df_macron = get_df_macron()

# get votes for Macron from Canada and United States of America

macron_votes_allemagne = np.array(df_macron[df_macron['Pays'] == 'ALLEMAGNE']['macron'])
macron_votes_belgique = np.array(df_macron[df_macron['Pays'] == 'BELGIQUE']['macron'])
macron_votes_canada = np.array(df_macron[df_macron['Pays'] == 'CANADA']['macron'])
macron_votes_suisse = np.array(df_macron[df_macron['Pays'] == 'SUISSE']['macron'])
macron_votes_usa = np.array(df_macron[df_macron['Pays'] == 'ÉTATS-UNIS']['macron'])

def plot_macron_ecdfs():
    #x_allemagne,y_allemagne = disfunc.ecdf(macron_votes_allemagne)
    #x_belgique,y_belgique = disfunc.ecdf(macron_votes_belgique)
    x_canada,y_canada = disfunc.ecdf(macron_votes_canada)
    x_suisse,y_suisse = disfunc.ecdf(macron_votes_suisse)
    #x_us,y_us = disfunc.ecdf(macron_votes_usa)

    #_ = plt.plot(x_allemagne, y_allemagne,marker='.',linestyle='none',color='yellow',label='ALLEMAGNE')
    #_ = plt.plot(x_belgique, y_belgique,marker='.',linestyle='none',color='brown',label='BELGIQUE')
    _ = plt.plot(x_canada, y_canada,marker='.',linestyle='none',color='red',label='CANADA')
    _ = plt.plot(x_suisse, y_suisse,marker='.',linestyle='none',color='green',label='SUISSE')
    #_ = plt.plot(x_us, y_us,marker='.',linestyle='none',color='blue',label='USA')
    
    _ = plt.xlabel('Percentage of votes for Macron')
    _ = plt.ylabel('ECDF')
    _ = plt.legend(loc='lower right')
    plt.show()

# H0 (null hypothesis) : the distribution of the votes for Macron is the same in US and CANADA
# difference of means

origin_diff_of_means = np.mean(macron_votes_canada) - np.mean(macron_votes_suisse)
print('original difference of means: ',origin_diff_of_means)

# calculate the difference of means for 10000 permutation replicates
def macron_can_suisse_perm_diff_of_means(size=10000):
    diff_of_means = np.empty(size)
    for i in range(size):        
        # draw the permutation replicates
        perm_replicates_1,perm_replicates_2 = disfunc.permuatation_sample(macron_votes_canada, macron_votes_suisse) 
        
        # calculate the difference of the means 
        diff_of_means[i] = disfunc.diff_of_means(perm_replicates_1, perm_replicates_2)

    return diff_of_means

def plot_perms_diff_of_means(size=10000):
    ''' Plot an histogram of all differences of means'''
    diff_of_means = macron_can_suisse_perm_diff_of_means(size)    
        
    _ = plt.hist(diff_of_means, bins=30,normed=True)
    _ = plt.plot([origin_diff_of_means]*2,[0,0.3])
    plt.show()
 
def macron_can_suisse_p_value():
    ''' calculate the permutation replicates of the votes for Macron in Canada and Switzerland ''' 
    perm_reps = disfunc.draw_perm_reps(macron_votes_canada, macron_votes_suisse, disfunc.diff_of_means, 10000) 

    p = np.sum(perm_reps >= origin_diff_of_means) / len(perm_reps)
    
    return p


def check_p_value():
    plot_macron_ecdfs()
    
    plot_perms_diff_of_means()

    p = macron_can_suisse_p_value()

    print('Null hypothesis : votes in Switzerland are distributed similarily to the votes in Canada\n\tp-value: ',p)   
    if (p < 0.05):
        print('hypothesis is significant')
    else:
        print('hypothesis isn\'t significant')

def get_shifted_canada_votes_switzerland():
    ''' shift the votes for Macron in Canada using the mean votes for macron in Switzerland '''
    
    shifted_canada_votes = macron_votes_canada - np.mean(macron_votes_canada) + np.mean(macron_votes_suisse)
    
    return shifted_canada_votes

def get_shifted_canada_votes_usa():
    ''' shift the votes for Macron in Canada using the mean votes for macron in USA '''
    
    shifted_canada_votes = macron_votes_canada - np.mean(macron_votes_canada) + np.mean(macron_votes_usa)
    
    return shifted_canada_votes

def plot_ecdf_shifted():
    shifted_votes = get_shifted_canada_votes_switzerland()
    
    x,y = disfunc.ecdf(macron_votes_canada)
    x_shifted,y_shifted = disfunc.ecdf(shifted_votes)
    
    _ = plt.plot(x, y,marker='.',linestyle='none',color='red',label='CANADA')
    _ = plt.plot(x_shifted, y_shifted,marker='.',linestyle='none',color='green',label='CANADA shifted')
        
    _ = plt.xlabel('Percentage of votes for Macron')
    _ = plt.ylabel('ECDF')
    _ = plt.legend(loc='lower right')
    plt.show()
    
def hypothesis_testing():
  
    # shift the data
    shifted_canada_votes = get_shifted_canada_votes_switzerland()
    
    # generate bootstrap replicates of the shifted data
    bs_replicates = disfunc.draw_bs_reps(shifted_canada_votes, np.mean, 1000)
    
    # calculate the p-value
    p_value_switzerland = np.sum(bs_replicates <= np.mean(macron_votes_canada)) / len(bs_replicates)
    
    # shift the data
    shifted_canada_votes = get_shifted_canada_votes_usa()
    
    # generate bootstrap replicates of the shifted data
    bs_replicates = disfunc.draw_bs_reps(shifted_canada_votes, np.mean, 1000)
    
    # calculate the p-value
    p_value_usa = np.sum(bs_replicates <= np.mean(macron_votes_canada)) / len(bs_replicates)
    
    print('hypothesis testing p-values:\n\t> Switzerland : ',p_value_switzerland,'\n\t> USA : ',p_value_usa)
    
def test_hyposthesis_on_correlation():
    r_obs = disfunc.pearson_r(macron_total_votes,macron_votes)
        
    perm_replicates = np.empty(10000)
    
    for i in range(10000):
        # Permute 
        macron_total_votes_permuted = np.random.permutation(macron_total_votes)
        
        # Compute Pearson correlation
        perm_replicates[i] = disfunc.pearson_r(macron_total_votes_permuted,macron_votes)    
    
    p_value = np.sum(perm_replicates >= float(str(r_obs))) / len(perm_replicates)
    
    print('test_hyposthesis_on_correlation, p-value:',p_value)
    
    _ = plt.hist(perm_replicates, bins=30)
    _ = plt.plot([r_obs]*2,[0,1200])
    plt.show()
    
test_hyposthesis_on_correlation()