from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import json
import os
import sys
import logging
import numpy as np

# Initalise the Flask app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
