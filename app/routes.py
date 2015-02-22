from flask import render_template, request, jsonify
from app import app
from .models import Image, Sideview, News, Alert

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/alerts', methods=['GET'])
def alerts():
	if request.method == 'GET':
		alerts = Alert.query.all()

		json_result = []
		for alert in alerts:
			json = alert.to_json_format()
			json_result.append(json)
	return jsonify(alerts=json_result)