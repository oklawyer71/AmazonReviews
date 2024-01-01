from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import json
import os
import sys
import logging
import pickle
from sklearn.preprocessing import StandardScaler
model_filename="./model"
import numpy as np

# Initalise the Flask app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# instantiate index page
@app.route("/")
def index():
    print(os.getcwd())
    return render_template("./home.html")

# instantiate dataset page
@app.route("/dataset")
def dataset():
    textout = "Dataset Used"
    return render_template("dataset.html", textout=textout)

# instantiate data preparation page
@app.route("/data-preparation")
def dataprep():
    textout = "Data Preparation"
    return render_template("data-preparation.html", textout=textout)

# instantiate data modelling page
@app.route("/data-modelling1")
def datamodel1():
    textout = "Data Modelling 1"
    return render_template("data-modelling1.html", textout=textout)

# instantiate data modelling page
@app.route("/data-modelling2")
def datamodel2():
    textout = "Data Modelling 2"
    return render_template("data-modelling2.html", textout=textout)
    
# instantiate intertopic page
@app.route("/intertopic")
def intertopic():
    textout = "Intertopic Map"
    return render_template("intertopic.html", textout=textout)

# instantiate Milestone 1's page
@app.route("/milestone1")
def milestone1():
    textout = "Milestone 1 - Exploratory Data Analysis (EDA)"
    return render_template("milestone1.html", textout=textout)

# instantiate Milestone 2's page
@app.route("/milestone2")
def milestone2():
    textout = "Milestone 2 - Bidirectional Encoder Representations from Transformers (BERT)"
    return render_template("milestone2.html", textout=textout)

# instantiate Milestone 3's page
@app.route("/milestone3")
def milestone3():
    textout = "Milestone 3 - Sentiment Analysis"
    return render_template("milestone3.html", textout=textout)

# instantiate Milestone 4's page
@app.route("/milestone4")
def milestone4():
    textout = "Milestone 4 - Final Project"
    return render_template("milestone4.html", textout=textout)

# instantiate Citations page
@app.route("/citations")
def citations():
    textout = "Citations"
    return render_template("citations.html", textout=textout)
