from collections import defaultdict
import cv2
import numpy as np
import pickle
from sklearn import tree

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
        return [img[50:55, 50:55]]
    return best_tiles

def load_model(model_path):
    return pickle.load(open(model_path, 'rb'))

def process_input(input_file):
    hsv_tiles = img_to_hsv_tiles(input_file, 100, 5, 0.25)
    hsv_tiles = np.array(hsv_tiles)
    hsv_tiles = hsv_tiles.reshape(hsv_tiles.shape[0], 75)
    return hsv_tiles

def pred_to_dict(pred):
    label_counts = defaultdict(int)
    for label in pred:
        label_counts[label] = label_counts[label] + 1
    return dict(label_counts)

def select_best(pred_dict):
    max_label = 'NO_PRODUCE_FOUND'
    max_count = 0
    count_sum = 0
    for label, count in pred_dict.items():
        if count > max_count:
            max_count = count
            max_label = label
        count_sum += count
    score = max_count/count_sum
    return max_label, score

def label_img(model_path, img_path):
    dt = load_model(model_path)
    hsv_tiles = process_input(img_path)
    pred = dt.predict(hsv_tiles)
    pred_dict = pred_to_dict(pred)
    label, confidence = select_best(pred_dict)
    return label, confidence

def label_imgs(model_path, img_paths):
    pred_dicts = []
    labels = []
    conf_scores = []

    dt = load_model(model_path)
    for img_path in img_paths:
        hsv_tiles = process_input(img_path)
        pred = dt.predict(hsv_tiles)
        pred_dict = pred_to_dict(pred)
        label, confidence = select_best(pred_dict)

        pred_dicts.append(pred_dict)
        labels.append(label)
        conf_scores.append(confidence)
    return labels, conf_scores, pred_dicts
