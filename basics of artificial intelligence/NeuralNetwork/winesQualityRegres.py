import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras
def wines_regres():
    white = pd.read_csv("winequality-white.csv", sep=';')
    red = pd.read_csv("winequality-red.csv", sep=';')
    # wines = pd.read_csv("winequality-white.csv", sep=';')
    red['type'] = 1
    # Add `type` column to `white` with price zero
    white['type'] = 0
    # Append `white` to `red`
    wines = red.append(white, ignore_index=True)
    # wines['grade'] = 1 # good
    # wines.grade[wines.quality < 7] = 0 # not good
    y = wines['quality']
    X = wines.drop(['quality'], axis=1)

    scaler = StandardScaler().fit(X)
    rescaledX = scaler.transform(X)
    y_new=np.array(y)
    x_train, x_test, y_train, y_test = train_test_split(rescaledX, y_new, test_size=0.2, random_state=7)

    model = keras.models.Sequential()
    model.add(keras.layers.Dense(128, input_dim=12, activation='relu'))
    model.add(keras.layers.Dense(64, activation='relu'))
    #model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(64, activation='relu'))
    #model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(32, activation='relu'))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    h=model.fit(x_train, y_train, epochs=60, verbose=2, batch_size=32)

    # Predicting the Value
    y_pred = model.predict(x_test)
    model.evaluate(x_test, y_test, batch_size=32, verbose=2)
    y_pred2=[]
    for i in y_pred:
        y_pred2.append(round(float(i)))
    plt.hist(y_pred, bins=20)
    plt.title("regres_ypred")
    plt.show()
    fig, axs = plt.subplots(1, 2, tight_layout=True)
    # We can set the number of bins with the `bins` kwarg
    axs[0].hist(y_pred2, bins=20)
    axs[1].hist(y_test, bins=20)
    plt.title("regres")
    plt.show()

    plt.plot(h.history['loss'])
    plt.plot(h.history['mae'])
    plt.xlabel('Epoch')
    plt.show()
def main():
    wines_regres()

if __name__ == '__main__':
    main()