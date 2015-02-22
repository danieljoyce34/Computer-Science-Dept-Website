from flask import render_template, request, jsonify
from app import app
from .models import Image, Sideview, News, Alert

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/testing', methods=['GET'])
def alerts():
	if request.method == 'GET':
		alerts = Alert.query.all()
		news = News.query.all()
		images = Image.query.all()
		sideviews = Sideview.query.all()

		alert_result = []
		news_result = []
		image_result = []
		sideview_result = []
		for alert in alerts:
			json = alert.to_json_format()
			alert_result.append(json)
		for new in news:
			json = new.to_json_format()
			news_result.append(json)
		for image in images:
			json = image.to_json_format()
			image_result.append(json)
		for sideview in sideviews:
			json = sideview.to_json_format()
			sideview_result.append(json)
	return jsonify(alerts=alert_result, news=news_result, images=image_result,
					sideviews=sideview_result)