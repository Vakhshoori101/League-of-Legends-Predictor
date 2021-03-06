import requests
import json

base = 'https://{region}.api.riotgames.com/{url}'
summoner_by_name = '/lol/summoner/v{version}/summoners/by-name/{summonerName}'
version = 4

class RiotAPI():

    def __init__(self, api_key=None, region='na1'):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key':self.api_key}
        for key,value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            base.format(region=self.region, url=api_url),
            params=args)
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = summoner_by_name.format(version=version, summonerName=name)
        return self._request(api_url)

    def get_live_data(self):
        try:
            data = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify="Code/riotgames.pem")
            with open('Code/data.json', 'w') as f:
                json.dump(data.json(), f)
        except:
            return 'No live games.'
