from flask import Flask, render_template, jsonify, request
import json
from random import randrange


app = Flask(__name__)


with open('FINAL_sentence_compare.json') as file:
    data = json.load(file)

@app.route("/")
def index():
    rand_HIT = randrange(100)
    return render_template('index.html', rand_HIT=rand_HIT)

@app.route("/get_text_pairs", methods=["POST"])
def get_text_pairs():
    index = request.json['index']
    rand_HIT = int(request.json['rand_HIT'])
    group_id = list(data.keys())[rand_HIT]  
    text_pairs = data[group_id][index]
    return jsonify(text_pairs)

if __name__ == "__main__":
    app.run(debug=True)



