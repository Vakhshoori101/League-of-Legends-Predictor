from Code.client import client


# dense_layers = [3,4]
# layer_sizes = [32, 64, 128]
# drop_ratios = [0.6, 0.8]
dense_layers = [3]
layer_sizes = [32]
drop_ratios = [0.4]


# preprocess data
train_path = "/Users/rostamvakhshoori/Desktop/MatchTimelinesFirst10.csv"
newClient = client(train_path)
newClient.preprocess(label='blueWins', d=['gameId', 'blueWins', 'blueTotalExperience', 'redTotalExperience'])
newClient.train_NN()
newClient.analysis()
# train_path = "/Users/rostamvakhshoori/Desktop/MatchTimelinesFirst15.csv"

# X_train, X_test, y_train, y_test = preprocess(train_path)

# logisitic_regression_model = LogisticRegression()
# logisitic_regression_model.fit(X_train, y_train)
# print(logisitic_regression_model.score(X_test, y_test))

# clf = svm.SVC()
# clf.fit(X_train, y_train)
# print(clf.score(X_test, y_test))

# for dense_layer in dense_layers:
#     for layer_size in layer_sizes:
#         for drop_ratio in drop_ratios:
#
#             # create neural network model
#             model = Sequential()
#             model.add(Dense(layer_size, input_dim=36, activation='relu'))
#             # model.add(Dense(layer_size, input_dim=16, activation='relu'))
#             model.add(Dropout(drop_ratio))
#
#             for l in range(dense_layer - 1):
#                 model.add(Dense(layer_size, activation='relu'))
#                 model.add(Dropout(drop_ratio))
#
#             model.add(Dense(1, activation='sigmoid'))
#
#             model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#
#             model.fit(X_train, y_train, epochs=25, batch_size=64, verbose=0, validation_data=(X_test, y_test))
#
# predicted = model.predict(X_test)
# predicted = np.where(predicted > 0.5, 1, 0)
# print(confusion_matrix(y_test, predicted))
# print(accuracy_score(y_test, predicted))
# print(f1_score(y_test, predicted, average="micro"))

# for dense_layer in dense_layers:
#     for layer_size in layer_sizes:
#         for drop_ratio in drop_ratios:
#
#             NAME = f"{dense_layer}-dense-{layer_size}-nodes-{drop_ratio}-drop_ratio-{int(time.time())}"
#             tensorboard = TensorBoard(log_dir=f'logs/{NAME}')
#
#             # create neural network model
#             model = Sequential()
#             model.add(Dense(layer_size, input_dim=38, activation='relu'))
#
#             for l in range(dense_layer - 1):
#                 model.add(Dense(layer_size, activation='relu'))
#                 model.add(Dropout(drop_ratio))
#
#             model.add(Dense(1, activation='sigmoid'))
#
#             model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#
#             model.fit(X_train, y_train, epochs=25, batch_size=64, verbose=1, validation_data=(X_test, y_test), callbacks=[tensorboard])

