import app.classifier
import os
import random

MODEL_PATH = 'model/dt5.sav'
LABELS = ["apple", "lemon", "mango", "onion", "orange", "tomato"]

def prep_dataset(dir_path="train", num=200, rand=True):
    file_paths = []
    target_labels = []

    for label in LABELS:
        path = dir_path + "/" + label
        files = os.listdir(path)

        if ".DS_Store" in files:
            files.remove('.DS_Store')

        if rand:
            files = random.sample(os.listdir(path), num)

        for filename in files:
            file_paths.append(path + "/" + filename)
            target_labels.append(label)

    return file_paths, target_labels

def calc_label_accuracy(target_labels, predictions):
    count_dict = {}
    for label in LABELS:
        count_dict[label] = {}
        count_dict[label]["correct"] = 0
        count_dict[label]["wrong"] = 0
        count_dict[label]["predicted_as"] = []

    for i in range(len(target_labels)):
        target_label = target_labels[i]
        pred = predictions[i]
        if target_label == pred:
            count_dict[target_label]["correct"] += 1
        else:
            count_dict[target_label]["wrong"] += 1
            count_dict[target_label]["predicted_as"].append(pred)

    return count_dict


file_paths, target_labels = prep_dataset(dir_path="imgs/user_input", num=400, rand=False)
predictions, conf_scores, pred_dicts = app.classifier.label_imgs(MODEL_PATH, file_paths)
print(calc_label_accuracy(target_labels, predictions))




