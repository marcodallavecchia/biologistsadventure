# Import required packages
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

sns.set(context='talk') # set context to have nice big labels
# Load dataset
# of course we go for penguins because PENGUINS
# drop na because we don't like them
df = sns.load_dataset('penguins').dropna()

# let's see what's in here
# possible interesting categorical variables
# for cat in ['species','island','sex']:
#     print(cat, df[cat].unique())
#
# print(df.head())
# let's explore the data using seaborn
g = sns.catplot(data=df, x='island', y='body_mass_g',
            hue='sex',
            col='species',
            kind='box', sharey=True)
g.set_axis_labels('Island','Body Mass (grams)')
#
# #  we can see that some combinations of island and species are not present in the dataset
# # Species Adelie is the only one that has measurements in all 3 islands let's focus on that one
adele = df[df['species'] == 'Adelie'].copy()
# let's make a violinplot instead of a boxplot with the data points overlayed
sns.violinplot(data=adele, x='island', y='body_mass_g', hue='sex')
sns.swarmplot(data=adele, x='island', y='body_mass_g', hue='sex',
            dodge=True, palette=['lightgray', 'black']).set(xlabel='Island',ylabel='Body Mass (grams)')
#
# # let's check the other variables
# # we can use the powerful lmplot figure-level function to investigate the relationship between flipper and bill length per species
g = sns.lmplot(data=df, x='flipper_length_mm', y='bill_length_mm', hue='species')
g.set(xlabel='Flipper Length (mm)',
    ylabel='Bill Length (mm)')

plt.show()
