from Code.client import client

# enter 10 to create model for 10 minute marker
# enter 15 to create model for 15 minute marker
def NN_Model(num):

    # get info depending on 10 or 15
    path, label, d = get_info(num)

    # preprocess csv file
    newClient = client(path)
    newClient.preprocess(label=label, d=d)

    newClient.train_NN()

    return newClient.model


# enter 10 to create model for 10 minute marker
# enter 15 to create model for 15 minute marker
def SVM_Model(num):

    # get info depending on 10 or 15
    path, label, d = get_info(num)

    # preprocess csv file
    newClient = client(path)
    newClient.preprocess(label=label, d=d)

    newClient.train_SVM()

    return newClient.model


def get_info(num):

    if num == 10:
        path = "MatchTimelinesFirst10.csv"
        label = 'blueWins'
        d = ['gameId', 'blueWins', 'blueWardsPlaced', 'blueWardsDestroyed', 'blueTotalGold', 'blueTotalExperience',
             'blueTotalJungleMinionsKilled', 'blueGoldDiff', 'blueExperienceDiff', 'blueGoldPerMin',
             'redWardsPlaced', 'redWardsDestroyed', 'redTotalGold', 'redTotalExperience',
             'redTotalJungleMinionsKilled', 'redGoldDiff', 'redExperienceDiff', 'redGoldPerMin']
    else:
        path = "MatchTimelinesFirst15.csv"
        label = 'blue_win'
        d = ['Unnamed: 0', 'matchId', 'blue_win', 'blueGold', 'blueJungleMinionsKilled', 'redGold',
             'redJungleMinionsKilled']

    return path, label, d
