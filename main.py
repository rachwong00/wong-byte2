# Imports
import os
import jinja2
import webapp2
import logging
import json
import urllib


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    

from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def hello():
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    return template.render(headers=cols, content=rows)
    
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
    
TABLE_ID = '1UJoloZuGbQ75LZt6-be6HktjB85WZMpYE2IDj-t_'
API_KEY = 'AIzaSyBFJIMR8IQl2UIUT07gwrfDu4Ifnn1txEA'

# This uses discovery to create an object that can talk to the 
# fusion tables API using the developer key
service = build('fusiontables', 'v1', developerKey=API_KEY)