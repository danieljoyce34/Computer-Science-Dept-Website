from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/carousel')
def carousel():
	return render_template('carousel.html')