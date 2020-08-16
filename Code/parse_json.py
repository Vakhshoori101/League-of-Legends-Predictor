import json
import pandas as pd

class parse_json():

    def __init__(self, file_name=None, j=None):
        if file_name:
            with open(file_name) as f:
                self.data = json.load(f)
        else:
            self.data = j
        self.summonerName_to_championName = {}
        for player in self.data['allPlayers']:
            self.summonerName_to_championName[player['summonerName']] = [player['championName'], player['team']]

    def get_active_player(self):
        username = self.data['activePlayer']['summonerName']
        champion, team = self.summonerName_to_championName[username]
        return {'summoner_name':username,
                'champion': champion,
                'team': team}

    def get_Ward_Scores(self) -> {str:int}:
        allPlayers = self.data['allPlayers']
        ward_scores = {}
        for player in allPlayers:
            ward_scores[player['championName']] = player["scores"]["wardScore"]
        return ward_scores

    def get_First_Blood(self) -> {str:int}:
        events = self.data['events']['Events']
        first_blood = {"CHAOS":0, "ORDER":0}
        for event in events:
            if event['EventName'] == 'FirstBlood':
                first_blood_team = self.summonerName_to_championName[event['Recipient']][1]
                first_blood[first_blood_team] += 1
                return first_blood
        return first_blood

    def get_Kills(self) -> {str:int}:
        allPlayers = self.data['allPlayers']
        kill_score = {}
        for player in allPlayers:
            kill_score[player['championName']] = player["scores"]["kills"]
        return kill_score

    def get_Deaths(self) -> {str:int}:
        allPlayers = self.data['allPlayers']
        death_score = {}
        for player in allPlayers:
            death_score[player['championName']] = player["scores"]["deaths"]
        return death_score

    def get_Assists(self) -> {str:int}:
        allPlayers = self.data['allPlayers']
        assists_score = {}
        for player in allPlayers:
            assists_score[player['championName']] = player["scores"]["assists"]
        return assists_score

    def get_Elite_Monsters(self) -> {str:{str:int}}:
        events = self.data['events']['Events']
        elite_monsters = {"CHAOS": {"HeraldKill":0, "DragonKill":0},
                          "ORDER": {"HeraldKill":0, "DragonKill":0}}
        for event in events:
            if event['EventName'] == 'DragonKill' or event['EventName'] == 'HeraldKill':
                elite_monster_team = self.summonerName_to_championName[event['KillerName']][1]
                elite_monsters[elite_monster_team][event['EventName']] += 1
        return elite_monsters

    def get_Team_Scores(self) -> {str:{str:int}}:
        allPlayers = self.data['allPlayers']
        team_scores = {"CHAOS": {"assists":0, "creepScore":0, "deaths":0, "kills":0, "wardScore":0, "average_level":0, "creepScore_per_min":0},
                       "ORDER": {"assists":0, "creepScore":0, "deaths":0, "kills":0, "wardScore":0, "average_level":0, "creepScore_per_min":0}}
        for player in allPlayers:
            team = player["team"]
            for score, value in player["scores"].items():
                team_scores[team][score] += value
            team_scores[team]['average_level'] += player['level']

        team_scores['CHAOS']['average_level'] /= 5
        team_scores['ORDER']['average_level'] /=5
        team_scores['CHAOS']['creepScore_per_min'] = team_scores['CHAOS']['creepScore'] / 10
        team_scores['ORDER']['creepScore_per_min'] = team_scores['ORDER']['creepScore'] / 10

        return team_scores

    def get_Team_Events(self) -> {str:{str:int}}:
        events = self.data['events']['Events']
        team_events = {"CHAOS": {"HeraldKill": 0, "DragonKill": 0, "FirstBlood":0, "TurretKilled":0},
                       "ORDER": {"HeraldKill": 0, "DragonKill": 0, "FirstBlood":0, "TurretKilled":0}}
        for event in events:
            if event['EventName'] in team_events['CHAOS'].keys():
                if event['EventName'] == 'TurretKilled':
                    if 'T1' in event['KillerName']:
                        team_events['CHAOS']['TurretKilled'] += 1
                    else:
                        team_events['CHAOS']['TurretKilled'] += 1
                else:
                    wanted_name = 'Recipient' if event['EventName'] == 'FirstBlood' else 'KillerName'
                    team_event = self.summonerName_to_championName[event[wanted_name]][1]
                    team_events[team_event][event['EventName']] += 1
        return team_events

    def get_Info(self, t=10) -> (pd.DataFrame,{}):
        team_scores = self.get_Team_Scores()
        team_events = self.get_Team_Events()
        if t==10:
            data = {'blueFirstBlood':[team_events['ORDER']['FirstBlood']],
                    'blueKills':team_scores['ORDER']['kills'],
                    'blueDeaths':team_scores['ORDER']['deaths'],
                    'blueAssists':team_scores['ORDER']['assists'],
                    'blueEliteMonsters':team_events['ORDER']['HeraldKill'] + team_events['ORDER']['DragonKill'],
                    'blueDragons':team_events['ORDER']['DragonKill'],
                    'blueHeralds':team_events['ORDER']['HeraldKill'],
                    'blueTowersDestroyed':team_events['ORDER']['TurretKilled'],
                    'blueAvgLevel':team_scores['ORDER']['average_level'],
                    'blueTotalMinionsKilled':team_scores['ORDER']['creepScore'],
                    'blueCSPerMin':team_scores['ORDER']['creepScore_per_min'],
                    'redFirstBlood':team_events['CHAOS']['FirstBlood'],
                    'redKills':team_scores['CHAOS']['kills'],
                    'redDeaths':team_scores['CHAOS']['deaths'],
                    'redAssists':team_scores['CHAOS']['assists'],
                    'redEliteMonsters':team_events['CHAOS']['HeraldKill'] + team_events['CHAOS']['DragonKill'],
                    'redDragons':team_events['CHAOS']['DragonKill'],
                    'redHeralds':team_events['CHAOS']['HeraldKill'],
                    'redTowersDestroyed':team_events['CHAOS']['TurretKilled'],
                    'redAvgLevel':team_scores['CHAOS']['average_level'],
                    'redTotalMinionsKilled':team_scores['CHAOS']['creepScore'],
                    'redCSPerMin':team_scores['CHAOS']['creepScore_per_min']}
        else:
            data = {'blueTotalMinionsKilled': [team_scores['ORDER']['creepScore']],
                    'blueAvgLevel': team_scores['ORDER']['average_level'],
                    'redTotalMinionsKilled': team_scores['CHAOS']['creepScore'],
                    'redAvgLevel': team_scores['CHAOS']['average_level'],
                    'blueKills': team_scores['ORDER']['kills'],
                    'blueHeralds': team_events['ORDER']['HeraldKill'],
                    'blueDragons': team_events['ORDER']['DragonKill'],
                    'blueTowersDestroyed': team_events['ORDER']['TurretKilled'],
                    'redKills': team_scores['CHAOS']['kills'],
                    'redHeralds': team_events['CHAOS']['HeraldKill'],
                    'redDragons': team_events['CHAOS']['DragonKill'],
                    'redTowersDestroyed': team_events['CHAOS']['TurretKilled'],}

        return pd.DataFrame.from_dict(data), self.get_active_player()
