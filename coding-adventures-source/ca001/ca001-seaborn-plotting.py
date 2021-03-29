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
df1 = pd.DataFrame.from_dict(data_dict1).melt(id_vars='time').drop('variable', axis=1)
df1.columns = ['time', 'Y']
df2 = pd.DataFrame.from_dict(data_dict2).melt(id_vars='time').drop('variable', axis=1)
df2.columns = ['time', 'Z']

df = df1.merge(df2, on='time')
# df.to_csv('mock_data.csv')
# df_melted = df.melt(id_vars=['time'])
# df_melted.to_csv('mock_data_melted.csv')
print(df)
# sns.lineplot(data=df_melted, x='time', y='value', hue='variable')
# plt.show()