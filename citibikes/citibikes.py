import pandas as pd
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
sample_values = [[14.7*5.64,85.3*5.64],[11.9*4.09,88.1*4.09]]
 
chisqstat= lambda N, values, expect : N*((values[0][0]*values[1][1]-values[0][1]*values[1][0])**2)/(expect)

print chisqstat(Ntot,  sample_values, expected)

