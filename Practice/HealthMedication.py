'''
Created on Aug 15, 2017

@author: idolchevic
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# list of drugs
CIS_bdpm_file = 'CIS_bdpm.txt'

# list of drugs presentations
CIS_CIP_bdpm_file = 'CIS_CIP_bdpm.txt'

# HAS ASMR opinions after 2002
CIS_HAS_ASMR_bdpm_file = 'CIS_HAS_ASMR_bdpm.txt'

# HAS SMR opinions after 2002 
CIS_HAS_SMR_bdpm_file = 'CIS_HAS_SMR_bdpm.txt'


def getDataframe(filename,index='CIS'):
    ''' read the file and add headers '''
    # read the data file
    df = pd.read_csv(filename,header=None,sep='\t', encoding='latin-1')
    
    #read the header file
    list_headers = pd.read_csv(filename.replace('.txt', '_header.csv')).columns.values
    
    # set dataframe header
    df.columns = list_headers
    
    # set the index
    df.set_index(index,inplace=True)
    
    return df
  
def getDataframeTimeIndexed(df,srcColumn='MA_date (DD/MM/YYYY)',destColumn='MA_date',date_format='%d/%m/%Y'):
    # format the date
    df[destColumn] = pd.to_datetime(df[srcColumn] , format=date_format)

    # drop the old date column
    df = df.drop(srcColumn, 1)

    # create a time serie
    return pd.DataFrame(df.values,index=df[destColumn], columns=df.columns)

def getTopMask(df,top=8,aggr='holder'):
    # count reports by aggr and sort them
    countAggr = df.groupby([aggr])[aggr].count().sort_values(ascending=[False])
    
    # get ndarray  
    top = countAggr[:top].index.values
    
    # create a mask 
    return df[aggr].isin(top)

def displayCISgraph(df1, df2, df3):
    '''display the graph of the list of medicinal products marketed or discontinued since less than three years.'''
    fig = plt.figure(figsize=(12, 9))
    
    def plot_curves():
        # plot time series
        df1.resample('A').count()['holder'].plot(y='count', kind='area', label='all laboraties',legend=True, alpha=0.5,color='#555555',linewidth=0)
        df2.resample('A').count()['holder'].plot(y='count', kind='area', label='others laboraties',legend=True, alpha=0.5,color='#31aecd',linewidth=0)
        df3.resample('A').count()['holder'].plot(y='count', kind='area',label='top laboraties', legend=True, alpha=1,color='#f9bb00',linewidth=0)    

    def plot_axes():
        # Remove the plot frame lines. They are unnecessary chartjunk.  
        ax = plt.subplot(111)  
        ax.spines["top"].set_visible(False)  
        ax.spines["right"].set_visible(False) 
        ax.spines['bottom'].set_color('#cdcdcd')
        ax.spines['left'].set_color('#cdcdcd')
        
        # Ensure that the axis ticks only show up on the bottom and left of the plot.  
        # Ticks on the right and top of the plot are generally unnecessary chartjunk.  
        ax.get_xaxis().tick_bottom()  
        ax.get_yaxis().tick_left()  
        
        ax.tick_params(axis=u'both', which=u'both',colors='#888888')
        ax.set_xlabel('marketing authorization date')
        ax.set_ylabel('drugs count')

        legend = ax.legend(loc='upper center', framealpha=0.5)
        legend.get_frame().set_linewidth(0.0)
    
    def plot_title():
        plt.title('Drugs authorizations by laboratories', loc='right')
    
    plot_curves()
    plot_axes()
    plot_title()
    plt.show()

# get the datas
df_CIS_bdpm = getDataframe(CIS_bdpm_file)

# index the datas using some time values
df_CIS = getDataframeTimeIndexed(df_CIS_bdpm)

# get the mask for top
top_mask = getTopMask(df_CIS,top=10) 

# top laboratories registerd drugs
df_top = df_CIS[top_mask] 

# others laboratories registerd drugs
df_rest = df_CIS[~top_mask]

# show the graph
# displayCISgraph(df_CIS,df_rest,df_top)

#read the SMR
df_SMR_dbpm = getDataframe(CIS_HAS_SMR_bdpm_file)

# get holder affected by the SMR review
df_CIS_SMR_dbpm = pd.merge(df_SMR_dbpm, df_CIS_bdpm.loc[:,['holder']],left_index=True, right_index=True, sort=False)

# keep only emitted review
mask_ignored = (df_CIS_SMR_dbpm.SMR_value == 'Non précisé') | (df_CIS_SMR_dbpm.SMR_value == 'Commentaires')
df_CIS_SMR_dbpm = df_CIS_SMR_dbpm[~ mask_ignored]

def compute_SMR(value):    
    if value == 'Faible':
        return 0
    elif value == 'Insuffisant':
        return 1
    elif value == 'Modéré':
        return 2
    elif value == 'Important': 
        return 3
    
    
df_CIS_SMR_dbpm['computed_SMR'] = df_CIS_SMR_dbpm.SMR_value.apply(compute_SMR)

df_CIS_SMR_dbpm = df_CIS_SMR_dbpm.sort_values('computed_SMR')
print(df_CIS_SMR_dbpm['computed_SMR'])

# get top and rest dataframes
top_mask = getTopMask(df_CIS_SMR_dbpm)
df_top = df_CIS_SMR_dbpm[top_mask]
df_rest = df_CIS_SMR_dbpm[~top_mask]

top_SMR = df_top.groupby(['computed_SMR'])['computed_SMR'].count()
rest_SMR = df_rest.groupby(['computed_SMR'])['computed_SMR'].count()

print(top_SMR)
top_SMR = top_SMR / top_SMR.sum()
rest_SMR = rest_SMR / rest_SMR.sum() 

# data to plot
n_groups = 4
means_top = top_SMR.values
means_rest = rest_SMR.values
 
# create plot
fig, ax = plt.subplots(figsize=(8, 5))
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, means_top, bar_width,
                 alpha=opacity,
                 color='#f9bb00',
                 label='top 10 laboratories')
 
rects2 = plt.bar(index + bar_width, means_rest, bar_width,
                 alpha=opacity,
                 color='#31aecd',
                 label='not in top 10 laboratories')
 
plt.xlabel('SMR value')
plt.ylabel('SMR rate')

# Remove the plot frame lines. They are unnecessary chartjunk.  
  
ax.spines["top"].set_visible(False)  
ax.spines["right"].set_visible(False) 
ax.spines['bottom'].set_color('#cdcdcd')
ax.spines['left'].set_color('#cdcdcd')
        
# Ensure that the axis ticks only show up on the bottom and left of the plot.  
# Ticks on the right and top of the plot are generally unnecessary chartjunk.  
ax.get_xaxis().tick_bottom()  
ax.get_yaxis().tick_left()  
plt.xticks(index + bar_width/2, ('Weak','Poor','Reasonable','Significant'))        
ax.tick_params(axis=u'both', which=u'both',colors='#888888')

legend = ax.legend(loc='upper center', framealpha=0.5)
legend.get_frame().set_linewidth(0.0)


          
#plt.tight_layout()

plt.title('Medical benefit - SMR by HAS reviews', loc='right')
plt.savefig('HAS_SMR.png')
plt.show()

