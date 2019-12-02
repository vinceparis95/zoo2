# import pandas library
import pandas as pd
import glob
import re
import numpy as np


dataFrameB = pd.DataFrame()
dataFrameC = pd.DataFrame()
for image in glob.iglob('/Users/vinceparis/dev/dfyb/GrowLogs/ei/_images/out/*.json'):
    df = pd.read_json(image)
    dfFiltered = df.filter(items=['label', '0'])
    dfFiltered = dfFiltered.replace('yellowing', -45.0)

    dataFrameB = dataFrameB.append(dfFiltered)
    dfSum = dfFiltered.sum(axis=0)
    dataFrameC = dataFrameC.append(dfSum, ignore_index=True)

print(dataFrameC.dropna())