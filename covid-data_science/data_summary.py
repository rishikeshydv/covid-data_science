import numpy as np
import pandas as pd
from scipy.stats import pearsonr

file = pd.read_csv('covid_cases.csv')

'''for i in range(len(file)):
    values = file.values[:,1:]
    #rint(values)
    corr = pearsonr(values,values)[0]
    print(corr)
'''

popn = file['Population']
per_cap = file['per_capita/PPP($)']
max_t = file['max_temp/*C']
min_t = file['min_temp/*C']
life_span = file['Average age of People/years']
covid = file['COVID_Cases']
hosp = file['No. of Hospitals']
print(popn.describe())

#corelation

(corelation) = pearsonr(file['COVID_Cases'], file['No. of Hospitals']) 
print(corelation[0])
#No. of Hopitals and Population have the highest corelation where hospitals > popn