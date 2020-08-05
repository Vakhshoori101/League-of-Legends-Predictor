from Code.client import client
import json
from Code.parse_json import parse_json
from Code.RiotAPI import RiotAPI

def predictor(num, model):

    # get live data
    API = RiotAPI()
    API.get_live_data()

    # preprocess data
    j = parse_json('Code/data.json')
    x, player_info = j.get_Info(num)

    new_client = client()

    # load specified model
    if model == 'NN':
        new_client.load_model(f'Models/NN_Model_{num}')
    else:
        new_client.load_model(f'Models/SVM_Model_{num}.pkl')

    # predict
    prediction = new_client.predict(x)

    # format prediction
    player_info['team'] = 'Blue'
    if player_info['team'] == 'CHAOS':
        prediction = 1 - prediction
        player_info['team'] = 'Red'
    prediction = "{:.2f}".format(prediction * 100)
    prediction = f'{player_info["summoner_name"]}, {player_info["champion"]} has a {prediction}% of winning on the {player_info["team"]} team after {num} minutes since the game\'s start.'

    return prediction

def checker():

    API = RiotAPI()

    # check if live game
    if API.get_live_data():
        return False

    with open('Code/data.json') as f:
        data = json.load(f)
    game_mode = data['gameData']['gameMode']
    game_time = data['gameData']['gameTime']

    # check if game is not Classic or Rank
    if game_mode not in ['CLASSIC', 'RANK']:
        return False

    # calculate time to call API
    sleep_time = 600 - game_time

    # check if markers to calculate probability have passed
    if sleep_time < 0:
        return False

    return sleep_time
