# 开始时间：2022/6/7 22:45
import pandas as pd
import numpy as np
euro12 = pd.read_csv('./Euro_2012_stats_TEAM.csv')

print(euro12.columns)
#Step 4. Select only the Goal column.
print(euro12['Goals'])
#How many team participated in the Euro2012?
print(euro12.duplicated('Team').count())
#What is the number of columns in the dataset?
print(euro12.shape[1])
# View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12.loc[:,['Team','Yellow Cards','Red Cards']]
print(discipline.shape)
# Sort the teams by Red Cards, then to Yellow Cards
ed=euro12.sort_values(['Red Cards','Yellow Cards'])
#Calculate the mean Yellow Cards given per Team
print(round(euro12['Yellow Cards'].mean()))
#Filter teams that scored more than 6 goals
print(euro12[euro12.Goals>6].Team)

#Select the first 7 columns
print(euro12.iloc[:,0:7])

#Select all columns except the last 3.
print(euro12.iloc[:,0:len(euro12)-3])


print(euro12.loc[['England','Italy','Russia'],['Shots on target']])

#Select the teams that start with G
print(euro12[euro12.Team.str.startswith('G')])

#Present only the Shooting Accuracy from England, Italy and Russia
euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]