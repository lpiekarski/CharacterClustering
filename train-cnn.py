from models.CNN import create_model
from image_transform import get_prepared_images
import tensorflow as tf
import numpy as np
import random
import os

dataset_dir = 'dataset-cnn'
model_path = 'trained/cnn_128_3'
# 2_64 ~84%
# 2_128 ~85%
N = 40000  # 400000
letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '_']


def R_squared(y, y_pred):
  residual = tf.reduce_sum(tf.square(tf.subtract(y, y_pred)))
  total = tf.reduce_sum(tf.square(tf.subtract(y, tf.reduce_mean(y))))
  r2 = tf.subtract(1.0, tf.divide(residual, total))
  return r2


def acc(y, y_pred):
    equality = tf.equal(tf.argmax(y), tf.argmax(y_pred))
    cast_equality = tf.cast(equality, tf.float32)
    return tf.reduce_mean(cast_equality)

def find_letter(l):
    for i in range(len(letters)):
        if letters[i] == l:
            return i
    return len(letters)


image_filenames = [dataset_dir + '/' + str(x) + '.png' for x in range(N)]
image_label_filenames = [dataset_dir + '/' + str(x) + '.txt' for x in range(N)]
print('preprocessing images')
X = get_prepared_images(image_filenames, img_size=128)
y = np.zeros((N, 56))
i = 0
for x in image_label_filenames:
    with open(x) as label_file:
        # y[i] = find_letter(label_file.read().strip())
        y[i, find_letter(label_file.read().strip())] = 1
    i = i + 1

model = None
if os.path.exists(model_path):
    model = tf.keras.models.load_model(model_path)
else:
    model = create_model()

#model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_squared_error'])
model.fit(X, y, epochs=10, validation_split=0.1, batch_size=128)
good = 0
for i in range(N):
    j = i #random.randint(0, N - 1)
    #print('filename: ' + image_filenames[j])
    #print('prediction: ' + letters[np.argmax(model(np.array([X[j, :, :]])))])
    #print('truth: ' + letters[np.argmax(y[j, :])])
    #print()
    if np.argmax(model(np.array([X[j, :, :]]))) == np.argmax(y[j, :]):
        good = good + 1
print('accuracy: ' + str(100. * good / N) + '%')
if not os.path.exists(model_path):
    os.mkdir(model_path)
model.save(model_path)
