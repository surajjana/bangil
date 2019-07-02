from bottle import Bottle, run, route, static_file, request, response, template
from pymongo import MongoClient
from bson.json_util import dumps
from string import Template
import json
import pymongo
import requests
import datetime
import time
import hashlib
import smtplib
import os

from extra_functions import *

app = Bottle(__name__)

# client = MongoClient()
# db = client.bae_chat

# client = MongoClient('mongodb://ocl:ocl@18.212.25.180/ocl')
# db = client.ocl

@app.route('/')
def root():
	return static_file('index.html', root='templates/')

@app.route('/manifest')
def manifest():
    return static_file('manifest.json', root='')

# @app.get('/apply')
# def apply():
# 	return static_file('application.html', root='templates/')

# @app.post('/apply')
# def apply_post():
# 	fname = request.forms.get('fname').title()
# 	lname = request.forms.get('lname').title()
# 	email = request.forms.get('email').lower()
# 	phone = request.forms.get('phone')
# 	story = request.forms.get('story')
# 	goals = request.forms.get('goals')
# 	track = request.forms.get('track')

# 	cur = db.ocl_fellowship_applications.insert({'fname': fname, 'lname': lname, 'email': email, 'phone': phone, 'story': story, 'goals': goals, 'track': track, 'time_stamp': time.time()})

# 	sendApplicationEmail(fname, email)

# 	return static_file('message.html', root='templates/')


# Static Routes
@app.route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(jpg|png|gif|ico|svg)>')
def images(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static')

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'