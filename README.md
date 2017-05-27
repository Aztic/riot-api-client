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
	for i in champions['champions']:
		if i['freeToPlay'] is True:
			ids.append(i['id'])
	for i in ids:
		print(client.get('lol/static-data/v3/champions/',i,region=region)['name'])
  
```


