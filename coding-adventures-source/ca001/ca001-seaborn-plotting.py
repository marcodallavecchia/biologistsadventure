import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

time = np.arange(20)
data_dict1 = {}
data_dict2 = {}
for ii in range(10):
    name1 = 'y'+str(ii)
    name2 = 'z'+str(ii)
    data_dict1[name1] =np.linspace(1, ii, 20)
    data_dict2[name2] =np.linspace(9, ii, 20)

data_dict1['time'] = time
data_dict2['time'] = time
df1 = pd.DataFrame.from_dict(data_dict1).melt(id_vars='time')
df1.columns = ['time','label', 'value']
df1['group'] = 'y_group'
df2 = pd.DataFrame.from_dict(data_dict2).melt(id_vars='time')
df2.columns = ['time','label','value']
df2['group'] = 'z_group'
df = pd.concat([df1, df2])

# df.to_csv('mock_data.csv')
print(help(sns.set_context))
# sns.set(style='darkgrid', context='talk')

# sns.relplot(data=df, x='time', y='value',  
#     hue='group', kind='line', ci='sd'
#     )
# sns.relplot(data=df, x='time', y='value',  
#     hue='group', kind='line', ci=98
#     )

# sns.relplot(data=df, x='time', y='value',  
#     col='group', hue='label', kind='line', legend=False
#     )


# fig, ax = plt.subplots(figsize=(8,6))
# sns.lineplot(data=df, x='time', y='value', 
#     hue='group', ax=ax, err_kws={'zorder':100.0})
# sns.lineplot(data=df, x='time', y='value', 
#     estimator=None, units='label', 
#     style='group', color='lightgrey',
#     ax=ax, legend=False)

# plt.show()