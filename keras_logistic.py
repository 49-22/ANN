from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
# taken from lukas/ml-class
from keras.utils import to_categorical

import wandb
from wandb.keras import WandbCallback

# logging code
run = wandb.init()
config = run.config

# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
img_width = X_train.shape[1]
img_height = X_train.shape[2]


# printing
X_train.shape, y_train.shape, X_test.shape

class Config:
    pass

config = Config()
config.image_height = img_height
config.image_width = img_width


import matplotlib.pyplot as plt
plt.imshow(X_train[0], cmap= 'gray')
plt.title('Digit {}'.format(y_train[0]))
#EXERCISE: Normalize, keep to 32 bits, change lr, batch size


# one hot encode outputs
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
labels = range(10)

num_classes = y_train.shape[1]

# create model
model = Sequential()
model.add(Flatten(input_shape=(img_width, img_height)))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam',
              metrics=['accuracy'])
model.summary()
# Fit the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test),
          callbacks=[WandbCallback(data_type="image", labels=labels, save_model=False)])
