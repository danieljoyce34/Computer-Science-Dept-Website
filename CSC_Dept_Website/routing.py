from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404

@app.route('/')
def index():
	return render_template('main_template.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/academics')
def academics():
	return render_template('academics.html')

@app.route('/research')
def research():
	return render_template('research.html')

@app.route('/opportunities')
def opportunities():
	return render_template('opportunities.html')

@app.route('/news')
def news():
	return render_template('news.html')

if __name__ == '__main__':
	app.debug = True
	app.run(host = "127.0.0.1", port = 8001)