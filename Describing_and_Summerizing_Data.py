'''
pandas.DataFrame.describe
DataFrame.describe(percentiles=None, include=None, exclude=None, datetime_is_numeric=False)[source]
'''

'''
DataFrame.count
Count number of non-NA/null observations.

DataFrame.max
Maximum of the values in the object.

DataFrame.min
Minimum of the values in the object.

DataFrame.mean
Mean of the values.

DataFrame.std
Standard deviation of the observations.

DataFrame.select_dtypes
Subset of a DataFrame including/excluding columns based on their dtype.
'''

                # Describing a numeric Series.

>>>s = pd.Series([1, 2, 3])
>>>s.describe()
count    3.0
mean     2.0
std      1.0
min      1.0
25%      1.5
50%      2.0
75%      2.5
max      3.0
dtype: float64


                # Describing a categorical Series.

>>>s = pd.Series(['a', 'a', 'b', 'c'])
>>>s.describe()
count     4
unique    3
top       a
freq      2
dtype: object

                # Describing a timestamp Series.

>>>s = pd.Series([
  np.datetime64("2000-01-01"),
  np.datetime64("2010-01-01"),
  np.datetime64("2010-01-01")
])
>>>s.describe(datetime_is_numeric=True)
count                      3
mean     2006-09-01 08:00:00
min      2000-01-01 00:00:00
25%      2004-12-31 12:00:00
50%      2010-01-01 00:00:00
75%      2010-01-01 00:00:00
max      2010-01-01 00:00:00
dtype: object

