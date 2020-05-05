#!/usr/bin/env python
# coding: utf-8

# In[1]:


key='a135d562f81946ae8aa641cb331294a0'
try:
    def get_playerid(enter):
 
        url='https://api.sportsdata.io/v3/nba/scores/json/Players'
        params={'key':key}
        response= requests.get(url,params)
        data=response.json()
        for player in data:
            if player['YahooName'].lower() == enter.lower():
                playerid= player['PlayerID']
        return playerid
        
except IndexError:
    print("Error")
except json.decoder.JSONDecodeError as e: 
    print("ERROR:Cannot decode the response into json"")
    print("DETAILS", e)

# response not ok
except requests.exceptions.HTTPError as e:
    print("ERROR")
    print("DETAILS:", e)
        
# internet is broken
except requests.exceptions.RequestException as e: 
    print("ERROR: Cannot connect to ", url)
    print("DETAILS:", e)
        


# In[2]:


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


# In[6]:


import pandas as pd
import requests
try:
    enter=input("Enter a player")
    playerid= get_playerid(enter)

    print("error")

    url=f'https://api.sportsdata.io/v3/nba/scores/json/Player/{playerid}'
    params={'key':key}
    response=requests.get(url,params)
    data=response.json()


    info=[]
    info.append({'Last Name':data['LastName'],'First Name':data['FirstName'],'Height':data['Height'],'Team':data['Team'],'Position':data['Position'],'Number':data['Jersey'],'College':data['College'],'Salary':data['Salary']})

info_data=pd.DataFrame(info)
except:
    prin
info_data

#Cant figure out try except for wrong input. Once I do one exception another pops up. When I try.. except the whole block of code, I get no output.


# In[ ]:





# In[ ]:




