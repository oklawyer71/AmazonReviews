"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template, request
import os

# instantiate index page
@app.route("/")
def index():
    print(os.getcwd())
    return render_template("./home.html")

# instantiate dashboard page
#@app.route("/dashboard")
#def dashboard():
    #textout = "Home page of Flask Application."
    #return render_template("dashboard.jinja2",textout=textout)

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
@app.route("/data-modelling")
def datamodel1():
    textout = "Data Modelling"
    return render_template("data-modelling.html", textout=textout)
    
# instantiate intertopic page
@app.route("/intertopic")
def intertopic():
    textout = "Intertopic Map"
    return render_template("intertopic.html", textout=textout)

# instantiate Milestone 1's page
@app.route("/individual-project")
def individualproject():
    textout = "Individual Project"
    return render_template("individual-project.html", textout=textout)

# instantiate Milestone 2's page
@app.route("/milestones")
def milestones():
    textout = "Milestones"
    return render_template("milestones.html", textout=textout)

# instantiate Citations page
@app.route("/citations")
def citations():
    textout = "Citations"
    return render_template("citations.html", textout=textout)
