# TensorFlow y tf.keras
import tensorflow as tf
from tensorflow import keras

# Librerias de ayuda
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage import io
import cv2
from imutils import paths
import os

# Load images
print("Loading images...")
folders = os.listdir('images')
imagePaths = {}
for folder in folders:
    imagePaths[folder] = list(paths.list_images("images/" + folder))

# Train images
image_list = list(paths.list_images("images"))

# Train labels
labels = {}
for label in imagePaths.keys():
    labels[label] = [list(imagePaths.keys()).index(label)] * len(imagePaths[label])
    #labels.append([label] * len(imagePaths[label]))

labels = [item for lista in labels.values() for item in lista]
labels = np.array(labels)

# Transforming the image
print("Transforming to array...")
prepared_list = []

def transform_image_to_array(image):
  pixeled_array = []
  pixeled_image = (io.imread(image))
  pixeled_array.append(pixeled_image)
  return np.array(pixeled_array)

for i in image_list:
    pixeled_image = (io.imread(i))
    prepared_list.append(pixeled_image)

# Training set
training = np.array(prepared_list)
training = training / 255

# Building the model
print("Building the model...")

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(250, 250)),
    keras.layers.Dense(300, activation='relu'),
    keras.layers.Dense(len(imagePaths.keys()), activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("Your training shape is ", training.shape)
print("Your labels shape is ", labels.shape)
model.fit(training, labels, epochs=10)
model.summary()
