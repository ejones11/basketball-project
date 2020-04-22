#!/usr/bin/env python
# coding: utf-8

# In[32]:


import requests

key='a135d562f81946ae8aa641cb331294a0'

url='https://api.sportsdata.io/v3/nba/scores/json/Players'
params={'key':key}
response= requests.get(url,params)
data=response.json()
data
for player in data:
    print(player['YahooName'], player['PlayerID'])


    

     


# In[40]:


import requests
playerid= input("Enter player id")
key='a135d562f81946ae8aa641cb331294a0'

url=f'https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStatsByPlayer/2019/{playerid}'
param={'key':key}
response=requests.get(url, params=param)
data=response.json()
print(data)
    


# In[ ]:





# In[ ]:




