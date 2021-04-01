---
title: "Seaborn plotting approaches"
excerpt: "Plotting individual and grouped data in Seaborn"
---
### Seaborn automatically groups data
The beauty of using the [Seaborn package](https://seaborn.pydata.org/) in scientificy data visualization, and especially for scientific publications, is that your data is automatically grouped together during plotting so you don't have to manually calculate for example **MEAN** and **STD** for the data you want to plot.

#### Plotting grouped data only
Let's say that I want to plot a time-series of a variable per group (i.e. a condition) and plot the mean value and the standard deviation of each group:
```python
sns.relplot(data=df, x='time', y='value',  
    hue='group', kind='line', ci='sd'
    )
```
**Returns**

<figure style="width: 500px" class="align-center">
        <img src="{{ site.url }}{{ site.baseurl }}/coding-adventures-source/ca001/Figure_1.png" alt="Figure 1">
</figure>

Here I am using **relplot** because it's the best to start with if you are exploring _the relationship between many variables_. You don't always have to use it if you just need to generate the plot above, but I often start with replot and the change to other functions if needed.

Let's say that the journal you are submitting to doesn't want **STD** for your plots but uses the **confidence interval** as the convention:
```python
sns.relplot(data=df, x='time', y='value',  
    hue='group', kind='line', ci=98
    )
```
**Returns**

<figure style="width: 500px" class="align-center">
        <img src="{{ site.url }}{{ site.baseurl }}/coding-adventures-source/ca001/Figure_2.png" alt="Figure 2">
</figure>

At times it's preferable to show multiple grouping based on different variables. Often you have many data points that would make it hard to use line type / colors and or markers to differentiate those groups. Thus, I often rely on multiple panels:
```python
sns.relplot(data=df, x='time', y='value',  
    col='group', hue='label', kind='line', legend=False
    )
```
**Returns**

<figure style="width: 500px" class="align-center">
        <img src="{{ site.url }}{{ site.baseurl }}/coding-adventures-source/ca001/Figure_3.png" alt="Figure 3">
</figure>

#### Plotting the individual and grouped traces together
It's often useful to plot both the individual data and the group data on top of each other for scientific publications. So you not only show the trends and average behaviors, but you can also highlight the heterogeneity in your dataset.

I struggled with this hard before, as I was always _very close_ to make what I wanted, but could never succeed to have it **exactly** like I wanted. This is the whole reason I am making this post.

- First, we need to create a common Axes object for both grouped and individual plots to be displayed on the same figure.
- Second, the parameter _units_ allows us to display individual traces, but that requires us to set **manually** the parameter _estimator_ to None.
- Third, I chose not to display the legend on one plot in order not to have too much information displayed.
- Fourth, plotting the two plots together causes some very frustrating interactions: in particular the shading areas of the grouped plot will display **below** all the traces by default, and we need to **manually** set the _zorder_ parameter to a high number inside the _err\_kws_ setting of seaborn.
```python
fig, ax = plt.subplots(figsize=(8,6))
sns.lineplot(data=df, x='time', y='value', 
    estimator=None, units='label', 
    style='group', color='lightgrey',
    ax=ax, legend=False)
sns.lineplot(data=df, x='time', y='value', 
    hue='group', ax=ax, err_kws={'zorder':100.0})
```
**Returns**

<figure style="width: 500px" class="align-center">
        <img src="{{ site.url }}{{ site.baseurl }}/coding-adventures-source/ca001/Figure_4.png" alt="Figure 4">
</figure>

### Using seaborn.set to prettify the plots
I am very bad at **manually** set figures/ticks/markers size, labels font, line colors etc.. so I really appreciate if there is an **automatic** way to create aesthetically pleasant plots consistently with readable ticks and labels right away! And indeed seaborn provides this, it does still sometimes take some adjustments but overall the results are very satisfying.

The line below shows the _style_ and _context_ used in the plots in this post.
```python
sns.set(style='darkgrid', context='talk')
```
For _style_ you can choose amongst: "dark", "white", "whitegrid", "darkgrid", and "ticks" to choose how the overall figure looks.
For _context_ you can choose amongst: "notebook", "paper", "talk", "poster" to choose how your labels, ticks and much more will look in the final figure. You can imagine how useful this can be depending on the reason you are making the figure for.