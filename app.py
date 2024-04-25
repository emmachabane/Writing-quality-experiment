from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
from random import randrange
import csv
import pandas as pd
import os

app = Flask(__name__)


with open('FINAL_sentence_compare.json') as file:
    data = json.load(file)

# Send answers to CSV
def save_to_csv(batch_id, answers):
    with open('exp_results.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([batch_id] + answers)

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

# Routes for submitting to CSV and redirecting
@app.route("/submit_responses", methods=["POST"])
def submit_responses():
    batch_id = request.form['batch_id']
    answers = [request.form.get(f'task{i}') for i in range(1, 11)]
    save_to_csv(batch_id, answers)
    return redirect(url_for('thank_you'))

@app.route("/thank_you")
def thank_you():
    return 'Your responses have been successfully submitted. Thank you for participating!'

if __name__ == "__main__":
    app.run(debug=True)



