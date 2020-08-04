from keras.models import Sequential
from keras.layers import Dense, Dropout
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm
from tensorflow import keras

# path = "/Users/rostamvakhshoori/Desktop/MatchTimelinesFirst15.csv"
# label = 'blue_win'
# d = ['Unnamed: 0', 'matchId', 'blue_win', 'blueGold', 'blueJungleMinionsKilled', 'redGold', 'redJungleMinionsKilled']
path = "/Users/rostamvakhshoori/Desktop/MatchTimelinesFirst10.csv"
label = 'blueWins'
d = ['gameId', 'blueWins', 'blueWardsPlaced', 'blueWardsDestroyed', 'blueTotalGold', 'blueTotalExperience', 'blueTotalJungleMinionsKilled', 'blueGoldDiff', 'blueExperienceDiff', 'blueGoldPerMin', 'redWardsPlaced', 'redWardsDestroyed', 'redTotalGold', 'redTotalExperience', 'redTotalJungleMinionsKilled', 'redGoldDiff', 'redExperienceDiff', 'redGoldPerMin']

# drop specified columns
df = pd.read_csv(path)
X = df.drop(d, axis=1)

input_dim = X.shape[1]

# scale the data
X = preprocessing.scale(X)

# create label
y = df[label]

# split and shuffle data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# dense_layer = 3
# layer_size = 32
# drop_ratio = 0.4
# epochs = 20
# verbose = 1
# model = Sequential()
# model.add(Dense(layer_size, input_dim=input_dim, activation='relu'))
# model.add(Dropout(drop_ratio))
#
# for l in range(dense_layer - 1):
#     model.add(Dense(layer_size, activation='relu'))
#     model.add(Dropout(drop_ratio))
#
# model.add(Dense(1, activation='sigmoid'))
#
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#
# model.fit(X_train, y_train,
#                epochs=epochs,
#                batch_size=64,
#                verbose=verbose,
#                validation_data=(X_test, y_test))
#
# model.save('NN_Model_15')
# model = keras.models.load_model('NN_Model_10')
# print(model.summary())
model = svm.SVC(probability=True)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
with open('SVM_Model_10.pkl', 'wb') as f:
    pickle.dump(model, f)
# with open('SVM_Model_10.pkl', 'rb') as f:
#     model = pickle.load(f)
print(model.score(X_test, y_test))
