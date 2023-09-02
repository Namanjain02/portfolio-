import pandas as pd 
import matplotlib.pyplot as plt 

ipl=pd.read_csv(r"C:\Users\naman\Downloads\ipl\matches (1).csv")

ipl.head()

ipl.shape
 
ipl['player_of_match'].value_counts()

ipl['player_of_match'].value_counts()[0:5]

list(ipl['player_of_match'].value_counts()[0:5].keys())

plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color="g")
plt.show()

ipl['result'].value_counts()

ipl['toss_winner'].value_counts()

batting_first=ipl[ipl['win_by_runs']!=0]

batting_first.head()


plt.figure(figsize=(8,5))   
plt.hist(batting_first['win_by_runs'])
plt.title("distributions of runs")
plt.xlabel("runs")
plt.show()

batting_first['winner'].value_counts()[0:3]

list(batting_first['winner'].value_counts()[0:3].keys())


plt.figure(figsize=(8,5))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=["blue","yellow","orange"])
plt.show()


plt.figure(figsize=(8,8))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


batting_second=ipl[ipl['win_by_wickets']!=0]

batting_second.head()



plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


batting_second['winner'].value_counts()

batting_second['winner'].value_counts()[0:3]

list(batting_second['winner'].value_counts()[0:3].keys())


plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


ipl['season'].value_counts()


ipl['city'].value_counts()



import numpy as np 
np.sum(ipl['toss_winner']==ipl['winner'])


325/636


deliveries=pd.read_csv(r"C:\Users\naman\Downloads\ipl\deliveries.csv")


deliveries.head()


deliveries['match_id'].unique()

match_1=deliveries[deliveries['match_id']==1]


match_1.head()

match_1.shape


srh=match_1[match_1['inning']==1]

srh['batsman_runs'].value_counts()

srh['dismissal_kind'].value_counts()


rcb=match_1[match_1['inning']==2]

rcb['batsman_runs'].value_counts()

rcb['dismissal_kind'].value_counts()
