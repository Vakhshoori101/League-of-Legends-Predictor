from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
from sklearn import preprocessing, svm
import time
from tensorflow.keras.callbacks import TensorBoard

class client():

    def __init__(self, csv_file=None):
        if csv_file:
            self.df = pd.read_csv(csv_file)
            self.dense_layer = 3
            self.layer_size = 32
            self.drop_ratio = 0.4
            self.epochs = 10
            self.verbose = 0
            self.model = Sequential()

    def preprocess(self, label, d=[]):
        # drop specified columns
        X = self.df.drop(d, axis=1)

        self.input_dim = X.shape[1]

        # scale the data
        X = preprocessing.scale(X)

        # create label
        y = self.df[label]

        # split and shuffle data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    def train_NN(self, board=False):
        if board:
            NAME = f"{self.dense_layer}-dense-{self.layer_size}-nodes-{self.drop_ratio}-drop_ratio-{int(time.time())}"
            tensorboard = TensorBoard(log_dir=f'logs/{NAME}')

        self.model.add(Dense(self.layer_size, input_dim=self.input_dim, activation='relu'))
        self.model.add(Dropout(self.drop_ratio))

        for l in range(self.dense_layer - 1):
            self.model.add(Dense(self.layer_size, activation='relu'))
            self.model.add(Dropout(self.drop_ratio))

        self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        self.model.fit(self.X_train, self.y_train,
                       epochs=self.epochs,
                       batch_size=64,
                       verbose=self.verbose,
                       validation_data=(self.X_test, self.y_test),
                       callbacks=[tensorboard] if board else [])

    def train_SVM(self):
        self.model = svm.SVC(probability=True)
        self.model.fit(self.X_train, self.y_train)
        print(self.model.score(self.X_test, self.y_test))

    def train_LR(self):
        self.model = LogisticRegression()
        self.model.fit(self.X_train, self.y_train)
        print(self.model.score(self.X_test, self.y_test))

    def analysis(self):
        predicted = self.model.predict(self.X_test)
        predicted = np.where(predicted > 0.5, 1, 0)
        print("Confusion Matrix:\n", confusion_matrix(self.y_test, predicted))
        print("Accuracy score:", accuracy_score(self.y_test, predicted))
        print("F1 score:", f1_score(self.y_test, predicted, average="micro"))

    def predict(self, X):
        X = X.to_numpy().reshape(-1, X.shape[1])
        if isinstance(self.model, svm.SVC):
            prediction = self.model.predict_proba(X)
        else:
            prediction = self.model.predict(X)
        while isinstance(prediction, np.ndarray):
            prediction = prediction[0]
        return prediction

    def load_model(self, model_name):
        if 'SVM' in model_name:
            with open(model_name, 'rb') as file:
                self.model = pickle.load(file)
        else:
            self.model = load_model(model_name)