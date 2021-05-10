import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#boxplot
file = pd.read_csv('covid_cases.csv')
sns.boxplot(x = 'Population', data = file)
plt.xticks(rotation = 0)
#plt.show()

#heatmap
file2 = pd.read_csv('covid_cases.csv')
df = file2[['Population','COVID_Cases','Districts']]  ##POPN is a to be changed everytime

heatmap1_data = pd.pivot_table(df, values='COVID_Cases', index=['Districts'], columns='Population')
sns.heatmap(heatmap1_data, cmap="YlGnBu")
plt.show()



