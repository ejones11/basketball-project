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
import pandas as pd
import requests
url = 'https://api.sportsdata.io/v3/nba/scores/json/Players?key=ed8594eb244145cdbc24f75b1da1e48b'

response = requests.get(url)
data = response.json()
data
data_df = pd.DataFrame(data)
info = data_df[ ['FirstName','LastName','Height','Team','Position','Jersey','College','Salary'] ]
info





