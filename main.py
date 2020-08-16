from predictor import predictor, checker, get_data
import json
import requests
import os
import time

def main(model='NN', web_server=False):

    # use Riot Live Client to check if a game is being played
    time_sleep = checker()

    if not time_sleep:
        return

    open('lock.txt', 'x').close()

    time.sleep(time_sleep)

    if web_server:
        url = 'http://localhost:8000'
        get_data()
        with open('Code/data.json') as f:
            data = json.load(f)
        data['num'] = 10
        data['model'] = model
        prediction10 = requests.post(url, json=data).text
        print(prediction10)

        # time.sleep(300)

        get_data()
        with open('Code/data.json') as f:
            data = json.load(f)
        data['num'] = 15
        data['model'] = model
        prediction15 = requests.post(url, json=data).text
        print(prediction15)


    else:
        prediction10 = predictor(10, model)
        print(prediction10)

        time.sleep(300)

        prediction15 = predictor(15, model)
        print(prediction15)

    os.remove('lock.txt')


if __name__ == "__main__":

    if not os.path.exists('lock.txt'):
        main(web_server=False)