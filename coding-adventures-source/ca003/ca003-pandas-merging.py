import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


number_cells = 5
df = pd.DataFrame()

for idx in range(number_cells):
    time_array = np.arange(20)
    values_array = np.random.random(20)+idx+1
    label_array = np.repeat(idx, 20)
    
    df_dict = {"time": time_array, 
              "values": values_array,
              "labels": label_array}
    df = pd.concat([df, pd.DataFrame(df_dict)])


sns.set_context("talk")
g = sns.lineplot(data=df, x='time', y='values', hue='labels', palette=sns.color_palette("Paired", as_cmap=True))
g.set(title='Not normalized intensities in time', ylabel='Values', xlabel='Time (min)')
g.legend(bbox_to_anchor=(1,0.8))
plt.tight_layout()
plt.savefig("not_normalized.png")
plt.show()


df_time0 = df.loc[df.time == 0, ['labels', 'values']]
df_time0.columns = ['labels', 'values_time0']
df_tot = df.merge(df_time0, on='labels')
df_tot['values_norm'] = df_tot['values'] / df_tot['values_time0']

g = sns.lineplot(data=df_tot, x='time', y='values_norm', hue='labels', palette=sns.color_palette("Paired", as_cmap=True))
g.set(title='Normalized intensities in time', ylabel='Normalized Values', xlabel='Time (min)')
g.legend(bbox_to_anchor=(1,0.8))
plt.tight_layout()
plt.savefig("normalized.png")
plt.show()




