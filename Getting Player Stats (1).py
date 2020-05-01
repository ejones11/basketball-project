#!/usr/bin/env python
# coding: utf-8

# In[29]:


import requests
enter=input("Enter a player" )
key='a135d562f81946ae8aa641cb331294a0'
THIS IS THE NEW API 'ed8594eb244145cdbc24f75b1da1e48b'
url='https://api.sportsdata.io/v3/nba/scores/json/Players'
params={'key':key}
response= requests.get(url,params)
data=response.json()
data
for player in data:
    if player['YahooName'].lower() == enter.lower():
        print(player['YahooName'], player['PlayerID'])
   
    

    

     


# In[9]:



    


# In[22]:


import requests
import pandas as pd
playerid= input("Enter player id" )
key='a135d562f81946ae8aa641cb331294a0'

url=f'https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStatsByPlayer/2019/{playerid}'
param={'key':key}
response=requests.get(url, params=param)
data=response.json()
data




# In[28]:


stats=[]
stats.append({'player':data['Name'],'FGA':data['FieldGoalsAttempted'],'FGM':data['FieldGoalsMade'],'FG%':data['FieldGoalsPercentage'], 'EFG%':data['EffectiveFieldGoalsPercentage']})
stats_data=pd.DataFrame(stats)
stats_data



# In[ ]:




