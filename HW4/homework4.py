import pylab as pl
import pandas as pd
import numpy as np
import ggplot as ggplot
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')

import os
os.chdir("/Users/luke/dropbox/PUI2015/HW4")
## read citibikes data: Feb.2015 
df = pd.read_csv("201502-citibike-tripdata.csv")

#df is the dataframe where the content of the csv file is stored
df['ageM'] = 2015-df['birth year'][(df['usertype'] == 'Subscriber') & (df['gender'] == 1)]
df['ageF'] = 2015-df['birth year'][(df['usertype'] == 'Subscriber') & (df['gender'] == 2)]


df_male= 2015-df['birth year'][(df['usertype'] == 'Subscriber') & (df['gender'] == 1)]
df_female = 2015-df['birth year'][(df['usertype'] == 'Subscriber') & (df['gender'] == 2)]

male = pd.DataFrame(df_male)
male = {'age':list(male['birth year']),'Gender':'Male'}
male = pd.DataFrame(male)

female = pd.DataFrame(df_female)
female = {'age':list(female['birth year']),'Gender':'Female'}
female = pd.DataFrame(female)

frame = [male,female]
agedata = pd.concat(frame)

ggplot.ggplot(aes(x='age'), data=agedata)+ geom_histogram(fill='white',colour='black')+facet_grid('Gender',scales="free")



import scipy.stats

ks=scipy.stats.ks_2samp(male['age'], female['age'])
print ks

format_male = np.random.choice(male['age'],len(female['age']),replace=False)


scipy.stats.pearsonr(format_male, female['age'])

scipy.stats.spearmanr(format_male, female['age'])

################################################
df['date'] = pd.to_datetime(df['starttime'])
df['hour'] = df['date'].dt.hour

age_dt = 2015-df['birth year'][(df['usertype'] == 'Subscriber')&((df['hour'] >= 6) & (df['hour']<=19))]
age_nt = 2015-df['birth year'][(df['usertype'] == 'Subscriber')&((df['hour'] > 19) | (df['hour']<6))]


dt = pd.DataFrame(age_dt)
dt = {'age':list(dt['birth year']),'Type':'Daytime'}
dt = pd.DataFrame(dt)

nt = pd.DataFrame(age_nt)
nt = {'age':list(nt['birth year']),'Type':'Nighttime'}
nt = pd.DataFrame(nt)

frame = [dt,nt]
agedata = pd.concat(frame)

ggplot.ggplot(aes(x='age'), data=agedata)+ geom_histogram(fill='white',colour='black')+facet_grid('Type',scales="free")

ks=scipy.stats.ks_2samp(dt['age'], nt['age'])
print ks

format_dt = np.random.choice(dt['age'],len(nt['age']),replace=False)


scipy.stats.pearsonr(format_dt, nt['age'])

scipy.stats.spearmanr(format_dt, nt['age'])


## https://github.com/yhat/ggplot/issues/417