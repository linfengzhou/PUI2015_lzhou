import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
# plt.style.use('ggplot')

import os
os.chdir("/Users/luke/dropbox/PUI2015/citibikes")
## read citibikes data: May.2015 
#data = pd.read_csv("201505-citibike-tripdata.csv")

data = pd.read_csv("201502-citibike-tripdata.csv")

## remove outliers


###data[(np.abs(stats.zscore(data)) < 3).all(axis=1)]


## explore data
type(data)
data.info()
data.keys()

usertype = data['usertype']
tripduration = data['tripduration']
gender = data['gender']

data['date'] = pd.to_datetime(data['starttime'])
data['weekday'] = data['date'].dt.weekday

###################
######chi-sq test
crosscounts = pd.crosstab(data['usertype'], data['weekday'])
# crosscounts = pd.crosstab(data['usertype'], data['gender'])
customer = crosscounts[0:1]
subscriber = crosscounts[1:2]
customer_weekday = customer[[0,1,2,3,4]].sum(axis=1)[0] / 5 
customer_weekend = customer[[5,6]].sum(axis=1)[0] / 2 
subscriber_weekday = subscriber[[0,1,2,3,4]].sum(axis=1)[0] / 5
subscriber_weekend = subscriber[[5,6]].sum(axis=1)[0] / 2 

a = customer_weekday 
b = customer_weekend
c = subscriber_weekday
d = subscriber_weekend

Ntot = customer_weekday + customer_weekend + subscriber_weekday + subscriber_weekend 
expected = (a+b)*(c+d)*(a+c)*(b+d)
sample_values = [[a,c],[b,d]]
 
chisqstat= lambda N, values, expect : N*((values[0][0]*values[1][1]-values[0][1]*values[1][0])**2)/(expect)

print chisqstat(Ntot,  sample_values, expected)
##############################


## selecting data
d1 = data['tripduration'][data['weekday']==0]
d2 = data['tripduration'][data['weekday']==1]
d3 = data['tripduration'][data['weekday']==2]
d4 = data['tripduration'][data['weekday']==3]
d5 = data['tripduration'][data['weekday']==4]
d6 = data['tripduration'][data['weekday']==5]
d7 = data['tripduration'][data['weekday']==6]

weekday = d1 
weekday = weekday.append(d2)
weekday = weekday.append(d3)
weekday = weekday.append(d4)
weekday = weekday.append(d5)
weekend = d6
weekend = weekend.append(d7)

## remove outlier
weekday1 = weekday[~((weekday-weekday.mean()).abs()>3*weekday.std())]
weekend1 = weekend[~((weekend-weekend.mean()).abs()>3*weekend.std())]

##  plot 
plt.figure(figsize=(12, 9)) 
ax1 = plt.subplot(1,2,1) 
ax1.spines["top"].set_visible(False)  
ax1.spines["right"].set_visible(False) 
ax1.get_xaxis().tick_bottom()  
ax1.get_yaxis().tick_left()  
plt.xlabel('Weekday_Tripduration',fontsize=10)
plt.ylabel('Counts ',fontsize=10)
weekday1.hist(alpha=0.6)

ax2 = plt.subplot(1,2,2) 
weekend1.hist(alpha=0.6)
ax2.spines["top"].set_visible(False)  
ax2.spines["right"].set_visible(False) 
ax2.get_xaxis().tick_bottom()  
ax2.get_yaxis().tick_left()  
plt.xlabel('Weekdend_Tripduration',fontsize=10)
plt.ylabel('Counts ',fontsize=10)


## t-test
stats.ttest_ind(weekday1,weekend1)




