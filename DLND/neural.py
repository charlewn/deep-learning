import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = 'Bike-Sharing-Dataset/hour.csv'

rides = pd.read_csv(data_path)

rides.head()

rides[:24*10].plot(x='dteday', y='cnt')


#plt.show()
dummy_fields = ['season', 'weathersit', 'mnth', 'hr', 'weekday']

for each in dummy_fields:
	dummies = pd.get_dummies(rides[each], prefix=each, drop_first=False)
	rides = pd.concat([rides, dummies], axis=1)

fields_to_drop = ['instant', 'dteday', 'season', 'weathersit', 'weekday', 'atemp', 'mnth', 'workingday', 'hr']

quant_features = ['casual', 'registered', 'cnt', 'temp', 'hum', 'windspeed']

data = rides.drop(fields_to_drop, axis=1)

data.head()