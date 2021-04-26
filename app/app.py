import classifier
import cv2
from flask import (
    Flask, render_template, request
)
import json
import search
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload_img.html', name="JOE")

@app.route('/upload', methods=['POST'])
def upload_file():
    model_path = 'app/model/dt5.sav'
    f = request.files["file"]
    img_path = 'app/uploads/' + secure_filename(f.filename)
    f.save(img_path)
    label, conf = classifier.label_img(model_path, img_path)
    return label

@app.route('/recipes/<ingredient>/<meal_type>', methods=['GET'])
def recipes(ingredient, meal_type):
    mt_copy = meal_type
    if meal_type == "all":
        mt_copy = None

    rows = search.query_for_videos(ingredient, mt_copy)
    videos = []

    for row in rows:
        vid = dict()
        vid['title'] = row['title']
        vid['type'] = row['type'].capitalize()
        vid['yt_link'] = row['yt_link'].replace('watch?v=', 'embed/')
        videos.append(vid)

    data = {
        "ingredient": ingredient,
        "meal_type": meal_type,
        "results_found": len(videos) > 0,
        "videos": videos
    }
    return render_template('recipes.html', data=data)
