""" 
Percent Daily Return Exercise

In this exercise, you are given the stock values for several consecutive days for acme corporation. Your job is to calculate the "percent daily return" for each day. The percent daily return is the percentage that the stock changes each compared to the day before.

Note: the percent daily return = 100 * (current day - previous day)/previous day

Below you are given the stock prices (there are only 4 days in this example). First convert to a numpy array. Then use slicing and numeric operations to calculate the percent daily return (no for loops!).
"""
import numpy as np

acme = [10, 11.5, 11, 10, 12]
ac = np.array(acme)
day1 = ac[0:2]
day2 = ac[1:3]
day3 = ac[2:4]
day4 = ac[3:5]


print(100 * ((day1[1]-day1[0])/day1[0]))
print(100 * ((day2[1]-day2[0])/day2[0]))
print(100 * ((day3[1]-day3[0])/day3[0]))
print(100 * ((day4[1]-day4[0])/day4[0]))

