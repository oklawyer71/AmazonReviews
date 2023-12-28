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
@app.route("/intertopic")
def index():
    print(os.getcwd())
    return render_template("./intertopic.html")


# feedback from Michael: the @app.route("/") try to add some text after the "/" and see what that does.
# https://www.geeksforgeeks.org/flask-app-routing/
