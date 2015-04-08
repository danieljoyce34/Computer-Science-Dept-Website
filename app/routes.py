from flask import render_template, request, jsonify, make_response, current_app
from app import app, db
from .models import Image, Sideview, News, Alert, Faculty, User, Staff, Education
from .models import FacultyServices, FacultyInterests, CommitteeMembers, Committee
import util

from datetime import timedelta
from functools import update_wrapper

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

#@app.route('/manageNews')
#def manageNews():
#	return render_template('manageNews.html')

#@app.route('/manageAlerts')
#def manageAlerts():
#	return render_template('manageAlerts.html')

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
@crossdomain(origin='*')
def newsAjax():
	if request.method == 'GET':
		news = News.query.all()

		news_result = []
		for new in news:
			json = new.to_json_format()
			news_result.append(json)
		return jsonify(news=news_result)

@app.route('/retrieveNews/<int:news_id>', methods=['GET'])
def newsIdAjax(news_id):
	if request.method == 'GET':
		news = News.query.filter_by(id=news_id).first()
		news_result = []
		json = news.to_json_format()
		json['image_url'] = 'https://media.licdn.com/mpr/mpr/shrink_500_500/p/3/000/2c8/24c/039e2a7.jpg'
		news_result.append(json)
		return jsonify(news=news_result)

@app.route('/retrieveAlerts/<int:alert_id>', methods=['GET'])
def alertsIdAjax(alert_id):
	if request.method == 'GET':
		alert = Alert.query.filter_by(id=alert_id).first()
		alert_result = []
		json = alert.to_json_format()
		alert_result.append(json)
		return jsonify(alert=alert_result)

@app.route('/retrieveSideviews', methods = ['GET'])
def sideviewsAjax():
	if request.method == 'GET':
		sideviews = Sideview.query.all()

		sideview_result = []
		for sideview in sideviews:
			json = sideview.to_json_format()
			sideview_result.append(json)
		return jsonify(sideviews=sideview_result)

#TODO return statements
@app.route('/addNews', methods=['POST'])
def addNews():
	#if not session.get('logged_in'):
	#	abort(401)
	news = News(headline=request.form['headline'], intro=request.form['intro'], 
		article=request.form['article'])
	db.session.add(news)
	db.session.commit()
	return "News entry was successfully added."

@app.route('/editNews/<int:news_id>', methods=['POST'])
def editNews():
	#if not session.get('logged_in'):
	#	abort(401)
	news = News.query.filter_by(id=news_id).first()
	news.headline = request.form['headline']
	news.intro = request.form['intro']
	news.article = request.form['article']
	db.session.commit()
	return "News entry was successfully edited."

@app.route('/addAlert', methods=['POST'])
def addAlert():
	#if not session.get('logged_in'):
	#	abort(401)
	alert = Alert(content=request.form['content'], 
		category=request.form['category'], location=request.form['location'], 
		start_date=request.form['start_date'], end_date=request.form['end_date'])
	db.session.add(alert)
	db.session.commit()
	return "Alert entry was successfully added."

@app.route('/editAlert/<int:alert_id>', methods=['POST'])
def editAlert():
	#if not session.get('logged_in'):
	#	abort(401)
	alert = Alert.query.filter_by(id=alert_id).first()
	alert.content = request.form['content']
	alert.category = request.form['category']
	alert.location = request.form['location']
	alert.start_date = request.form['start_date']
	alert.end_date = request.form['end_date']
	db.session.commit()
	return "Alert entry was successfully edited."

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

@app.route('/editNews')
def editNewsList():
	return render_template('editnews.html')
