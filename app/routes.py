from flask import render_template
from app import app
from .models import Action

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/testing')
def testingPage():
	#Querying the Action table and retrieving all data
	actionTables = Action.query.all()
	return render_template('testingPage.html', actions=actionTables)