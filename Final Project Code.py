#!/usr/bin/env python
# coding: utf-8

# In[14]:





def get_playerid(enter):
    url='https://api.sportsdata.io/v3/nba/scores/json/Players'
    params={'key':key}
    response= requests.get(url,params)
    data=response.json()
    for player in data:
        if player['YahooName'].lower() == enter.lower():
            playerid= player['PlayerID']
    return playerid 




# ## Player Bios

# In[16]:


import pandas as pd
import requests
enter=input("Enter a player")
playerid= get_playerid(enter)


url=f'https://api.sportsdata.io/v3/nba/scores/json/Player/{playerid}'
params={'key':key}
response=requests.get(url,params)
data=response.json()
data
info=[]
info.append({'Last Name':data['LastName'],'First Name':data['FirstName'],'Height':data['Height'],'Team':data['Team'],'Position':data['Position'],'Number':data['Jersey'],'College':data['College'],'Salary':data['Salary']})
info_data=pd.DataFrame(info)
info_data


# ## Season Totals

# In[17]:


enter=input("Enter a player")
playerid= get_playerid(enter)
url=f'https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStatsByPlayer/2019/{playerid}'
param={'key':key}
response=requests.get(url, params=param)
data=response.json()
stats=[]
stats.append({'player':data['Name'],'G':data['Games'],'Points':data['Points'],'FGA':data['FieldGoalsAttempted'],'FGM':data['FieldGoalsMade'],'FG%':data['FieldGoalsPercentage'], 'EFG%':data['EffectiveFieldGoalsPercentage'], 'FTA':data['FreeThrowsAttempted'], 'FTM':data['FreeThrowsMade'],'FT%':data['FreeThrowsPercentage'], 'ORB':data['OffensiveRebounds'], 'DRB': data['DefensiveRebounds'], 'TRB': data['Rebounds'], 'AST':data['Assists'], 'TOV': data['Turnovers'], 'STL':data['Steals'], 'BLK': data['BlockedShots'], 'PF':data['PersonalFouls'],'+/-':data['PlusMinus'], 'PER':data['PlayerEfficiencyRating']})
stats_data=pd.DataFrame(stats)
stats_data


# ## Per Game Stats
# 

# In[18]:


pergame=[]
pergame.append({'player':data['Name'],'G':data['Games'],'Points':(data['Points']/data['Games']), 'FGA':(data['FieldGoalsAttempted']/data['Games']), 'FGM':(data['FieldGoalsMade']/data['Games']), 'FG%':data['FieldGoalsPercentage'], 'EFG%':data['EffectiveFieldGoalsPercentage'],'FTA':(data['FreeThrowsAttempted']/data['Games']),'FT%':data['FreeThrowsPercentage'], 'ORB':(data['OffensiveRebounds']/data['Games']), 'DRB':(data['DefensiveRebounds']/data['Games']), 'TRB':(data['Rebounds']/data['Games']), 'AST':(data['Assists']/data['Games']),'TOV':(data['Turnovers']/data['Games']), 'STL':(data['Steals']/data['Games']),'BLK':(data['BlockedShots']/data['Games']),'PF':(data['PersonalFouls']/data['Games']), '+/-':data['PlusMinus'],'PER':data['PlayerEfficiencyRating']})
pergame_data=pd.DataFrame(pergame)
pergame_data.round(decimals=1)


# ## Glossary
# G - Games Played
# FGA- Field Goals Attempted
# FGM - Field Goals Made
# FG% - Field Goal Percentage
# EFG% - Effective Field Goal Percentage; the formula is (FG + 0.5 * 3P) / FGA. This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.
# FTA-Free Throws Attempts 
# FTM-Free Throws Made
# FT%- Free Throw Percentage
# ORB- Offensive Rebounds
# DRB- Defensive Rebounds
# TRB- Total Rebounds 
# AST- Assists
# TOV-Turnovers
# STL- Steals
# BLKS- Blocks
# PF- Personal Fouls
# +/- - Plus-Minus. It is the point differential when a player or team is on the floor
# PER- Player Effeciency Rating. PER is a rating developed by ESPN.com columnist John Hollinger. In John's words, "The PER sums up all a player's positive accomplishments, subtracts the negative accomplishments, and returns a per-minute rating of a player's performance.
# 
# 
# 

# ## League Leaders 

# In[19]:


import requests
import pandas as pd
url='https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/2019'
key='ed8594eb244145cdbc24f75b1da1e48b'
params={'key':key}
response=requests.get(url, params=params)
data=response.json()
data
data_df = pd.DataFrame(data)


enter=input("Enter the stat: Points, Rebounds, Assists,BlockedShots or Steals")
leaders=data_df[ ['Name', 'Points', 'Rebounds', 'Assists', 'BlockedShots','Steals'] ]
leaders2=leaders.sort_values(enter,ascending=False)
leaders3=leaders2.head(25)
leaders
leaders3[['Name', enter]]


# In[ ]:




