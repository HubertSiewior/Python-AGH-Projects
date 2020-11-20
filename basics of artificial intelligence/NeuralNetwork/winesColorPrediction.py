# Import Required Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

from tensorflow import keras
from sklearn.model_selection import train_test_split

def wine_color():
    # Read in white wine data
    white = pd.read_csv("winequality-white.csv", sep=';')

    # Read in red wine data
    red = pd.read_csv("winequality-red.csv", sep=';')

    print(red.head())
    print(white.tail() )
    print(white.describe() )
    print(red.sample(5) )


    # Create Histogram
    fig, ax = plt.subplots(1, 2)

    ax[0].hist(red.alcohol, 10, facecolor='red',
               alpha=0.5, label="Red wine")

    ax[1].hist(white.alcohol, 10, facecolor='white',
               ec="black", lw=0.5, alpha=0.5,
               label="White wine")

    fig.subplots_adjust(left=0, right=1, bottom=0,
                        top=0.5, hspace=0.05, wspace=1)

    ax[0].set_ylim([0, 1000])
    ax[0].set_xlabel("Alcohol in % Vol")
    ax[0].set_ylabel("Frequency")
    ax[1].set_ylim([0, 1000])
    ax[1].set_xlabel("Alcohol in % Vol")
    ax[1].set_ylabel("Frequency")
    fig.suptitle("Distribution of Alcohol in % Vol")
    plt.show()


    # Add `type` column to `red` with price one
    red['type'] = 1

    # Add `type` column to `white` with price zero
    white['type'] = 0

    # Append `white` to `red`
    wines = red.append(white, ignore_index=True)

    X = wines.iloc[:, 0:11]
    print(X)
    y = np.ravel(wines.type)
    scaler = StandardScaler().fit(X)
    rescaledX = scaler.transform(X)
    # Spliting the data set for training and validating
    x_train, x_test, y_train, y_test = train_test_split(
        rescaledX, y, test_size=0.34, random_state=45)

    # Initialize the constructor

    model = keras.models.Sequential()

    # Add an input layer
    model.add(keras.layers.Dense(100, activation='relu', input_shape=(11,)))

    # Add one hidden layer
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(32, activation='relu'))
    model.add(keras.layers.Dense(32, activation='relu'))

    model.add(keras.layers.Dropout(0.5))
    # Add an output layer
    model.add(keras.layers.Dense(2, activation='softmax'))

    # Model output shape
    model.output_shape

    # Model summary
    model.summary()

    # Model config
    print(model.get_config())

    # List all weight tensors
    print(model.get_weights())

    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])

    # Training Model
    model.fit(x_train, y_train, epochs=20,
              batch_size=32, verbose=2)

    # Predicting the Value
    y_pred = model.predict(x_test)
    model.evaluate(x_test, y_test, batch_size=64, verbose=2)

    y_pred2 = []
    for i in y_pred:
        if i[0] > i[1]:
            y_pred2.append(0)
        else:
            y_pred2.append(1)

    fig, axs = plt.subplots(1, 2, tight_layout=True)
    # We can set the number of bins with the `bins` kwarg
    axs[0].hist(y_pred2, bins=20)
    axs[1].hist(y_test, bins=20)
    plt.show()

def main():
    wine_color()
if __name__ == '__main__':
    main()