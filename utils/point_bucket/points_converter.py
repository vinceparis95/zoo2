import numpy as np
import pandas as pd

############################################################

# pull farmer a weekly log
farmer_a = "/home/vince/zoo/utils/points/farmer_a.csv"
a = pd.read_csv(farmer_a).sum()
a_val = a.iloc[0]
# get total points
print("farmer_a points: ", a_val)

# pull farmer b weekly log
farmer_b = "/home/vince/zoo/utils/points/farmer_b.csv"
b = pd.read_csv(farmer_b).sum()
b_val = b.iloc[0]
# get total points
print("farmer b points: ", b_val)

# sum points
simple_sum = (a_val+b_val)
print("sum of all farmers points: ", simple_sum)

#############################################################

num = a_val/simple_sum
num = round(num, 3)
print("\nfarmer_a's ", a_val, " divided by the total of ", simple_sum, "= ", num)

contributions = 40

pay = num*contributions
print("farmer a can trade points in for ", pay, " dollars :) ")