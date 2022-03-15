# Import required packages
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset('penguins').dropna()
# Column names
# ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']

# Interested in sex differences amongst the 3 species
grouped_df = df.groupby(['species', 'sex'])
number_of_groups = len(grouped_df.groups) # groups is a dictionary so len(dict) will return the number of groups

# Example of why you might want to loop through groups
sns.set(context='notebook') # set style and labels size
f, axes = plt.subplots(2, int(number_of_groups/2), figsize=(10,8)) # create plots grid
for (g, dataframe), ax in zip(grouped_df, axes.ravel()):
    corr_table = dataframe.corr() # calculate correlation table for each group
    sns.heatmap(corr_table, ax=ax, annot=True) # make heatmap of corr table
    ax.set_title(g)
plt.tight_layout()
plt.show()

# grouped_df.describe() # calculate stats per group
# da = grouped_df.agg({'body_mass_g': [np.mean, np.std]}) # get specific stats on specific variable
# print(da.loc['Adelie', 'Female']['body_mass_g', 'mean']) # access specific values using loc
#
# daT = da.T # transpose to get categories as variables instead of indeces
# for species in daT.columns.levels[0]: # get high hierarchy categories
#     daT[species, 'body_mass_diff'] = daT[species, 'Male'] - daT[species, 'Female']
#
# # matrix-like difference between dataframes
# df_m = df[df['sex'] == 'Male'].reset_index().drop('index',axis=1).copy() # make a copy of filtered observations
# df_f = df[df['sex'] == 'Female'].reset_index().drop('index',axis=1).copy() # drop old index column
#
# df_diff = df_m.groupby('species').mean() - df_f.groupby('species').mean()
# print(df_diff)
