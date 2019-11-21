import pandas as pd
import numpy as np
import datetime
import glob
import re

'''
this program takes a daily batch of classifications for an environment,
and creates a matrix, containing 'id', 'age', and 'feature sum' columns.
These matrices are sent to output folders, one for each environment.
'''

# create 'file' column from yolo json
dataFrame = []
for image in glob.iglob('/Users/vinceparis/dev/dfyb/GrowLogs/eii/_images/out/*.json'):
    file = re.findall(r'\d+', image)
    dataFrame.append(file)
fileColumn = np.c_[dataFrame]
dataFrame = pd.DataFrame(fileColumn)

# create feature column from the sum of features
dataFrameB = pd.DataFrame()
for image in glob.iglob('/Users/vinceparis/dev/dfyb/GrowLogs/eii/_images/out/*.json'):
    df = pd.read_json(image)
    df = df.dropna()
    dfFiltered = df.filter(items=['label', '0'])
    dfSum = dfFiltered.sum(axis=0)
    dataFrameB = dataFrameB.append(dfSum, ignore_index=True)

# concatenate id and feature, sort by feature
dfF = pd.concat([dataFrame, dataFrameB], axis=1)
dfSorted = dfF.sort_values(by=['label'], ascending=False)
dfSorted = dfSorted.dropna()
dfSorted = dfSorted.rename(columns={0:'id'})
dfSorted = dfSorted.rename(columns={'label': 'featureSum'})
dfOutput = dfSorted.to_csv('/Users/vinceparis/dev/dfyb/utils/test.csv')
naturans = pd.read_csv('/Users/vinceparis/dev/dfyb/utils/test.csv')

# to the id and feature columns, we will add an 'age' column.
# first, create a 'planted time' column;
time = []
planted = pd.Timestamp('2019-03-07 18:53:29.751762')
col = dfSorted.__len__()
for x in range(0, col):
    time.append(planted)
plantedColumn = np.c_[time]
plantedColumn = pd.DataFrame(plantedColumn)
output = naturans.join(plantedColumn)
output = output.rename(columns={0: "planted"})
output = output.filter(items=('id', 'featureSum', 'planted'))
# print(output)

# second, create 'current time' column.
time2 = []
for x in range (0, col):
    time2.append(pd.Timestamp.now())
currentColumn = np.c_[time2]
output2 = pd.DataFrame(currentColumn)
output2 = output.join(output2)
output2 = output2.rename(columns={0: "current time"})
# print(output2)

# derive 'age' by subtracting 'planted time' from 'current time'
output2['age'] = output2['current time'] - output2['planted']
print(output2['age'])
output2 = output2.filter(items=('id', 'age', 'featureSum'))
output2['age'] = output2['age'].astype(str).str[0:2]
# output2['age'] = output2['age'].astype(float)
print(output2)

# send to environment folders (with a datetime)
now = datetime.datetime.now()
now = now.strftime("%m-%d")
output = output2.to_csv('/Users/vinceparis/dev/dfyb/GrowLogs/eii/eiidailyData/e2gL'+str(now)+'.csv')


