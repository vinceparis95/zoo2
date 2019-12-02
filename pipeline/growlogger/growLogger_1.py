import pandas as pd
import glob, os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''
We can log the daily batch to a historical record of the crop in the environment
'''

csvs = glob.glob("/Users/vinceparis/dev/dfyb/GrowLogs/eii/eiidailyData/*.csv")
df = pd.concat((pd.read_csv(f, header = 0) for f in csvs))
df.drop(['Unnamed: 0'],axis=1,inplace=True)
dfSorted = df.sort_values(by=['id'], ascending=False)

# add environment column
col = dfSorted.__len__()
n = np.full((1, col), 2)
dataFrame = pd.DataFrame(n)
dataFrame = dataFrame.T
output = dfSorted.join(dataFrame)
output = output.rename(columns={0: "env"})
e2GrowLog = output.sort_values(by=['featureSum'], ascending=False)
print(output)
e2GrowLog = e2GrowLog.to_csv("/Users/vinceparis/dev/dfyb/GrowLogs/eii/growLogs/e2growlog.csv", index=False)
