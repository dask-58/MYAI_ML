# Say df is the dataset

#import and read the csv file first
import pandas as pd
import numpy as np

df = pd.read_csv('path')
#check for missing data in the head first
df.head()

#count of missing data points per column
missing_count = df.isnull().sum()

#fill all missing values with the median / mean

df.fillna(mean, inplace=True) 
#or
df.fillna(0)
#or
df.fillna(median)


