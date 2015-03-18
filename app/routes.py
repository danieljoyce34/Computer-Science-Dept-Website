from flask import render_template, request, jsonify
from app import app
from .models import Image, Sideview, News, Alert

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/retrieveAlerts', methods = ['GET'])
def alertsAjax():
	if request.method == 'GET':
		alerts = Alert.query.all()

		alert_result = []
		image_result = []
		sideview_result = []
		for alert in alerts:
			json = alert.to_json_format()
			alert_result.append(json)
		return jsonify(alerts=alert_result, images=image_result,
					sideviews=sideview_result)

@app.route('/retrieveNews', methods = ['GET'])
def newsAjax():
	if request.method == 'GET':
		news = News.query.all()

		news_result = []
		for new in news:
			json = new.to_json_format()
			news_result.append(json)
		return jsonify(news=news_result)

@app.route('/retrieveSideviews', methods = ['GET'])
def sideviewsAjax():
	if request.method == 'GET':
		sideviews = Sideview.query.all()

		sideview_result = []
		for sideview in sideviews:
			json = sideview.to_json_format()
			sideview_result.append(json)
		return jsonify(sideviews=sideview_result)

@app.route('/carousel')
def carousel():
	return render_template('carousel.html')

@app.route('/article', methods=['POST', 'GET'])
def article():
	#e=request.args['articleNumber']

	#QUERY DATABASE HERE
	results = {}
	results['articleImage'] ='120003' 
	results['articleHeader']='There is some data'
	results['articleContent']='We have contempt for our content'

	return render_template('article.html', data=results)

@app.route('/getArticleNumber')
def getArticleNumber():
	return 12

@app.route('/general', methods=['POST', 'GET'])
def generalPage():
	e = request.args['content']
	return render_template('pageTemplate.html', content=e)

#@app.route('/about')
#def aboutGeneral():
# #	return render_template('pageTemplate.html', content="about")

# @app.route('/academics')
# def aboutGeneral():
# 	return render_template('pageTemplate.html', content="academics")