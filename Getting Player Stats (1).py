#!/usr/bin/env python
# coding: utf-8

# In[29]:


import requests
enter=input("Enter a player" )
key='ed8594eb244145cdbc24f75b1da1e48b'
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
key='ed8594eb244145cdbc24f75b1da1e48b'

url=f'https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStatsByPlayer/2019/{playerid}'
param={'key':key}
response=requests.get(url, params=param)
data=response.json()
data














My Code...
import requests
import panda as pd
url = 'https://api.sportsdata.io/v3/nba/scores/json/Players?key=ed8594eb244145cdbc24f75b1da1e48b'
param={'key':key}
response=requests.get(url, params=param)
data=response.json()
data


info = []
info.append({'first name':data['FirstName']})
info_data = pd.DataFrame(info)
info_data

for i in data:
    print(i)






