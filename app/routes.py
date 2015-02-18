from flask import render_template
from app import app
from .models import Image, Sideview, News, Alert

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/testing')
def testingPage():
	#Querying Image and Sideview table and retrieving all data
	image_table = Image.query.all()
	sideview_table = Sideview.query.all()
	news_table = News.query.all()
	alerts_table = Alert.query.all()
	return render_template('testingPage.html', sideview=sideview_table, news=news_table, alerts=alerts_table)