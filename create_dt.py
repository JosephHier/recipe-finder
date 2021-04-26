import cv2
import numpy as np
import os
import pickle
from sklearn import tree

def build_decision_tree(samples, labels):
    samples = np.array(samples)
    samples = samples.reshape(samples.shape[0], 75)
    print(samples.shape)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(np.array(samples), labels)
    return clf

def get_dataset(train_path):
    samples = []
    labels = []
    for label in os.listdir(train_path):
        if not (label == '.DS_Store'):
            for img_file in os.listdir(train_path + '/' + label):
                if not (img_file == '.DS_Store'):
                    file_path = train_path + '/' + label + '/' + img_file
                    hsv_tiles = img_to_hsv_tiles(file_path, 100, 5, 0.2)
                    for hsv_tile in hsv_tiles:
                        samples.append(hsv_tile)
                        labels.append(label)
    return samples, labels

def img_to_hsv_tiles(file_path, img_resize=100, tilesize=10, threshold=0.25):
    img = cv2.imread(file_path)
    img = cv2.resize(img, (img_resize, img_resize), interpolation = cv2.INTER_NEAREST)
    tiles = img_to_tiles(img, tilesize, threshold)
    hsv_tiles = []
    for tile in tiles:
        hsv = cv2.cvtColor(tile, cv2.COLOR_BGR2HSV)
        hsv_tiles.append(hsv)
    return hsv_tiles

def img_to_tiles(img, tilesize, threshold):
    height, width = img.shape[:2]
    top, btm = 0, tilesize
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    best_tiles = []

    while btm < height:
        left, right = 0, tilesize
        while right < width:
            tile = gray[top:btm, left:right]
            white_pixels = np.sum(tile == 255)
            percent_white = white_pixels/(tilesize * tilesize)
            if percent_white < threshold:
                best_tiles.append(img[top:btm, left:right])
            left += tilesize
            right +=tilesize
        top += tilesize
        btm += tilesize

    if len(best_tiles) == 0:
        return [img[40:60, 40:60]]
    return best_tiles

def save_model(model, model_path):
    pickle.dump(model, open(model_path, 'wb'))

train_path = 'train'
model_path = 'model/dt5.sav'

samples, labels = get_dataset(train_path)
dt = build_decision_tree(samples, labels)
print("DT built")
save_model(dt, model_path)
print("DT saved in " + model_path)
