""" 
Wind Statistics
----------------

Topics: Using array methods over different axes, fancy indexing.

The data in 'wind.data' has the following format::

        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71
   
The first three columns are year, month and day.  The remaining 12 columns are average windspeeds in knots at 12 cities in Ireland on that day.


2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds in Ireland.  In other words, reduce all the wind measurements
   from all the days and all the locations to a single set of statistics 
   for the entire dataset. 

3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds for each of the cities (columns).  You should end up with 12
   results for each of the statistics.
   
4. Calculate the min, max and mean windspeed and standard deviations of the 
   windspeeds for every day (rows) in the data set.  Here you'll reduce all 
   the cities numbers to a set of statistics for each day.  There a thousands
   of days, so your resulting data sets will be large.
   
5. Find the city which has the greatest windspeed on each day 
   (an integer column number for each day). 

6. Find the year, month and day on which the greatest windspeed was recorded.

7. Find the average windspeed in January for each city.

You should be able to perform all of these operations without using a for
loop or other looping construct.

Bonus
~~~~~

1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (It's ok to use
   a loop in this one.)


Notes
~~~~~

These data were analyzed in detail in the following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.

"""
import numpy as np

"""
1. Use the <var> = np.loadtxt(<file>) to read the data into an array. Use <array>.shape to see the dimensions of the array with the data.
"""
file = np.loadtxt("wind.data")
print(file.shape)

"""
2. As stated in the introduction, the first 3 columns of the data file are the dates. The remaining columns are the wind speed data. Use array slicing to create an array containing only the wind speed data. 
<var> = <array>[<rows>, <columns>]
"""
dt = file[:,3:]


"""
3. Print the minimum (<array>.min()), maximum (<array.max()), mean (<array>.mean()), and standard deviation (<array>.std()), for ALL the wind speed data.)
"""
print(dt.min())
print(dt.max())
print(dt.mean())
print(dt.std())

"""
4. As stated above, each column in the data file contains wind speed data for a different city. Print the min, max, mean, and standard deviation for each city.

The min is found using <array>.min(axis=0)
"""

print(dt.min(axis=0))
print(dt.max(axis=0))
print(dt.mean(axis=0))
print(dt.std(axis=0))

"""
5. As stated above, each row in the data file contains wind speed data for each day. Print the min, max, mean, and standard deviation for each day.__doc__

The min is found using <array>.min(axis=1)
"""
print(dt.min(axis=1))
print(dt.max(axis=1))
print(dt.mean(axis=1))
print(dt.std(axis=1))

"""
6. Use <array>.argmax(axis=1) to create an array that shows the index of the windiest city each day. Then use the following code to determine the index of the city that is the windiest most often.
<var> = np.unique(<array>, return_counts=True)
"""

ind = dt.argmax(axis=1)
windi, counts = np.unique(ind, return_counts=True)
print(windi[np.where(counts==max(counts))[0][0]])

"""
7. As stated in the very beginning, the 2nd column (index 1) of the data file is the month number. Use the following code to get the indices of the rows that contain March data:
<var> = <array>[:, 1] == 3
Then create a new array containing only the rows that have March data. The following code should help.
<var> = <array>[<indices>]
Finally, find the mean wind speed for all of the March data.
"""
mar = file[:,1] == 3
m_dat = dt[mar]
print(m_dat.mean())

"""
BONUS: Create an array with the average wind speed for each month.
"""
# For each month (Jan to Dec)
for month in range(1,13):
  mon = file[:,1] == month
  o_dat = dt[mon]
  print(o_dat.mean())


# For each month in data
for year in range(61, 79):
  yea = file[:,0] == year
  y_dat = file[yea]
  for month in range(1,13):
    mont = y_dat[:,1] == month
    o_dt = y_dat[:,3:]
    o_dat = o_dt[mont]
    print(o_dat.mean())

