from flask import Flask, request, render_template
from wtforms import Form, StringField, validators
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

projects = []


class project():

    def __init__(self, json):
        self.name = json['name']
        self.description = json['description']

    def __str__(self):
        return self.name


@app.route("/", methods=['Get'])
def return_projects():
    return render_template("index.html", projects=[p.name for p in projects])


@app.route("/store", methods=['GET', 'POST'])
def store():
    error = {}
    if request.json['name'] and request.json['description']:
        projects.append(project(request.json))
        return {'message': 'Project Created!'}
    else:
        if not request.json['name']:
            error['name'] = "The name field is required"
        if not request.json['description']:
            error['description'] = "The description field is required"
        return error, 422
