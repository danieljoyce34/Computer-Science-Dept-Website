from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/carousel')
def carousel():
	return render_template('carousel.html')

@app.route('/article', methods=['POST', 'GET'])
	e=request.args['articleNumber']

	#QUERY DATABASE HERE
	results = {}
	results['articleImage'] ='120003' 
	results['articleHeader']='There is some data'
	results['articleContent']='We have contempt for our content'

	return render_template('article', data=results)

@app.route('/getArticleNumber')
def getArticleNumber():
	return 12

