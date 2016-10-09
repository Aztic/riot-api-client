## riot-api-client
A python client for [Riot API](https://developer.riotgames.com/).

## Usage

``` python
#Let's show the free-week champions

import os
from riot_client import Riot

RIOT_KEY = os.getenv('RIOT_API_KEY')
client = Riot(RIOT_KEY)
ids = []

champions = client.get('api/lol/na/v1.2/champion')

for i in champions['champions']:
  if i['freeToPlay'] is True:
    ids.append(i['id'])

for i in ids:
  print(client.get('api/lol/static-data/na/champion/',i)['name']
  
```


