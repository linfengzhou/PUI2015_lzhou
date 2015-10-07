import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

import os
os.chdir("/Users/luke/dropbox/PUI2015/citibikes")
## read citibikes data: May.2015 
data = pd.read_csv("201505-citibike-tripdata.csv")

## explore data
type(data)
data.info()
data.keys()

usertype = data['usertype']
tripduration = data['tripduration']
gender = data['gender']

data['date'] = pd.to_datetime(data['starttime'])
data['weekday'] = data['date'].dt.weekday


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

##plt.figure(figsize=(12, 9)) 
#ax = plt.subplot(111) 
#ax.spines["top"].set_visible(False)  
#ax.spines["right"].set_visible(False) 
#ax.get_xaxis().tick_bottom()  
#ax.get_yaxis().tick_left()  
#plt.xlabel('sample mean',fontsize=16)
#plt.ylabel('N',fontsize=16)
#plt.hist(q1,alpha=0.5,color="#3F5D7D")

stats.ttest_ind(weekday,weekend)


