## riot-api-client
An unofficial python client for [Riot API](https://developer.riotgames.com/).

## Usage

``` python
#Let's show the free-week champions

import os
from riot_client import Riot

RIOT_KEY = os.getenv('RIOT_API_KEY')
client = Riot(RIOT_KEY)
ids = []

champions = client.get('lol/platform/v3/champions',region='na1')
for champion in champions['champions']:
	if champion['freeToPlay'] is True:
		ids.append(champion['id'])
for id in ids:
	print(client.get('lol/static-data/v3/champions/',id,region=na1)['name'])
  
```


