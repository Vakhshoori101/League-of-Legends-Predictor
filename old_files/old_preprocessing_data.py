import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

def preprocess(csv_file, label, d=[]):
    # read csv file
    df = pd.read_csv(csv_file)


    # drop specified columns
    X = df.drop(d)
    # X = df.drop(['gameId', 'blueWins', 'blueTotalExperience', 'redTotalExperience'], axis=1)
    # X = df.drop(['Unnamed: 0', 'matchId', 'blue_win'], axis=1)

    # scale the data
    X = preprocessing.scale(X)

    # create label
    y = df[label]
    # y = df['blueWins']
    # y = df['blue_win']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    return X_train, X_test, y_train, y_test
