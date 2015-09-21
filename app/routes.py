from flask import render_template, request, jsonify, make_response, json
from flask import current_app, redirect, url_for, abort, Response
from app import app, db
from .models import Image, Sideview, News, Alert, Faculty, User, Staff, Education
from .models import FacultyServices, FacultyInterests, CommitteeMembers, Committee
import util
import jinja2
from jinja2 import TemplateNotFound
import os
import random

from datetime import timedelta
from functools import update_wrapper

def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):
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
    sideviews = Sideview.query.all()
    sideview = sideviews[random.randint(0, len(sideviews) - 1)]

    alerts = Alert.query.all()

    return render_template('index.html', sideview=sideview, alerts=alerts)

@app.route('/retrieveAlerts', methods=['GET'])
@crossdomain(origin='*')
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

@app.route('/retrieveAlerts/<int:alert_id>', methods=['GET'])
def alertsIdAjax(alert_id):
	if request.method == 'GET':
		alert = Alert.query.filter_by(id=alert_id).first()
		alert_result = []
		json = alert.to_json_format()
		alert_result.append(json)
		return jsonify(alert=alert_result)

@app.route('/news/<int:news_id>')
def getNewsWithId(news_id):
    news = News.query.filter_by(id=news_id).first()
    image = 'https://media.licdn.com/mpr/mpr/shrink_500_500/p/3/000/2c8/24c/039e2a7.jpg'
    return render_template('NewsArticle.html', news=news, image=image)


@app.route('/retrieveNews', methods=['GET'])
@crossdomain(origin='*')
def newsAjax():
    if request.method == 'GET':
        news = News.query.all()

        news_result = []
        for new in news:
            json = new.to_json_format()
            json['image_url'] = 'https://media.licdn.com/mpr/mpr/shrink_500_500/p/3/000/2c8/24c/039e2a7.jpg'
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

@app.route('/retrievePeople', methods=['GET'])
def allPeopleAjax():
    if request.method == 'GET':
        faculties = Faculty.query.all()

        people_result = []
        for faculty in faculties:
            json = {'id': faculty.id,
                    'name': faculty.user.fname + ' ' + faculty.user.lname,
                    'person_type': faculty.faculty_type,
                    'job_title': faculty.faculty_rank,
                    'image_url': 'https://media.licdn.com/mpr/mpr/shrink_500_500/p/3/000/2c8/24c/039e2a7.jpg'}
            people_result.append(json)

        staffs = Staff.query.all()
        for staff in staffs:
            json = {'id': staff.id,
                    'name': staff.user.fname + ' ' + staff.user.lname,
                    'person_type': 'staff',
                    'job_title': staff.position,
                    'image_url': 'https://media.licdn.com/mpr/mpr/shrink_500_500/p/3/000/2c8/24c/039e2a7.jpg'}
            people_result.append(json)
        return jsonify(people=people_result)


@app.route('/retrieveFullTimeFaculty', methods=['GET'])
def fullTimeFacultyAjax():
    if request.method == 'GET':
        faculties = Faculty.query.filter_by(faculty_type='full time').all()

        faculties_result = []
        for faculty in faculties:
            faculty_dict = faculty.to_json_format()
            user_dict = faculty.user.to_json_format()
            json = util._merge_two_dicts(user_dict, faculty_dict)
            faculties_result.append(json)
        return jsonify(faculties=faculties_result)


@app.route('/retrieveAdjunctFaculty', methods=['GET'])
def adjunctFacultyAjax():
    if request.method == 'GET':
        faculties = Faculty.query.filter_by(faculty_type='adjunct').all()

        faculties_result = []
        for faculty in faculties:
            faculty_dict = faculty.to_json_format()
            user_dict = faculty.user.to_json_format()
            json = util._merge_two_dicts(user_dict, faculty_dict)
            faculties_result.append(json)
        return jsonify(faculties=faculties_result)


@app.route('/retrieveStaff', methods=['GET'])
def staffAjax():
    if request.method == 'GET':
        staffs = Staff.query.all()

        staff_result = []
        for staff in staffs:
            staff_dict = staff.to_json_format()
            user_dict = staff.user.to_json_format()
            json = util._merge_two_dicts(user_dict, staff_dict)
            staff_result.append(json)
        return jsonify(staffs=staff_result)

@app.route('/retrieveStaff/<int:staff_id>', methods=['GET'])
def staffIdAjax(staff_id):
    if request.method == 'GET':
        staff = Staff.query.filter_by(id=staff_id).first()

        staff_result = []
        staff_dict = staff.to_json_format()
        user_dict = staff.user.to_json_format()
        json = util._merge_two_dicts(user_dict, staff_dict)
        staff_result.append(json)
        return jsonify(staff=staff_result)

@app.route('/retrieveFaculty/<int:faculty_id>', methods=['GET'])
def facultyIdAjax(faculty_id):
    if request.method == 'GET':
        faculty = Faculty.query.filter_by(id=faculty_id).first()

        faculty_result = []
        faculty_dict = faculty.to_json_format()
        user_dict = faculty.user.to_json_format()
        json = util._merge_two_dicts(user_dict, faculty_dict)

        educations = faculty.educations
        edu_list = []
        for edu in educations:
            edu_list.append(edu.to_json_format())
        json = util._append_to_dict(json, edu_list, 'educations')

        faculty_services = faculty.faculty_services
        service_list = []
        for service in faculty_services:
            service_list.append(service.name)
        json = util._append_to_dict(json, service_list, 'services')

        faculty_interests = faculty.faculty_interests
        interest_list = []
        for interest in faculty_interests:
            interest_list.append(interest.interest)
        json = util._append_to_dict(json, interest_list, 'interests')

        faculty_committee_members = faculty.committee_members
        department_committee = []
        college_committee = []
        university_committee = []
        inter_department_committee = []
        professional_committee = []
        for member in faculty_committee_members:
            committee = member.committee
            if committee.category == 'department':
                department_committee.append(committee.name)
            elif committee.category == 'college':
                college_committee.append(committee.name)
            elif committee.category == 'university':
                university_committee.append(committee.name)
            elif committee.category == 'professional':
                professional_committee.append(committee.name)
            else:
                inter_department_committee.append(committee.name)
        json = util._append_to_dict(json, department_committee,
                                    'department_committee')
        json = util._append_to_dict(
            json, college_committee, 'college_committee')
        json = util._append_to_dict(json, university_committee,
                                    'university_committee')
        json = util._append_to_dict(json, inter_department_committee,
                                    'inter_department_committee')
        json = util._append_to_dict(json, professional_committee,
                                    'professional_committee')

        faculty_result.append(json)
        return jsonify(faculty=faculty_result)

@app.route('/newsEditor')
def newsEditor():
    news = News.query.all()
    return render_template('news/newsEditor.html', news=news)

@app.route('/submitNews', methods=['POST'])
def submitNews():
	#if not session.get('logged_in'):
	#	abort(401)
	news = News(headline=request.form['edit-news-headline'], intro=request.form['edit-news-intro'], 
		article=request.form['edit-news-article'])
	db.session.add(news)
	db.session.commit()
	news = News.query.all()
	#return render_template('editnews.html', news=news)
	return redirect(url_for('newsEditor'))

@app.route('/submitNewsEdits/<int:news_id>', methods=['POST'])
def submitNewsEdits(news_id):
	#if not session.get('logged_in'):
	#	abort(401)
	news = News.query.filter_by(id=news_id).first()
	news.headline = request.form['ne-title-edit']
	news.intro = request.form['ne-intro-edit']
	news.article = request.form['ne-article-edit']
	news.start_date = request.form['ne-sdate-edit']
	news.end_date = request.form['ne-edate-edit']
	db.session.commit()
	news = News.query.all()
	#return render_template('editnews.html', news=news)
	return redirect(url_for('newsEditor'))

@app.route('/alertEditor')
def alertEditor():
    alerts = Alert.query.all()
    return render_template('alerts/alertEditor.html', alerts=alerts)

@app.route('/addAlert', methods=['POST'])
def addAlert():
	#if not session.get('logged_in'):
	#	abort(401)
	alert = Alert(
        content=request.form['content'], 
		category=request.form['category'], 
		start_date=request.form['start_date'], 
        end_date=request.form['end_date']
    )
	db.session.add(alert)
	db.session.commit()
	return "Alert was successfully added."

@app.route('/editAlerts')
def editAlerts():
	alerts = Alert.query.all()
	return render_template('editalerts.html', alerts=alerts)

@app.route('/editAlerts/<int:alert_id>')
def editAlertsWithId(alert_id):
	#if not session.get('logged_in'):
	#	abort(401)
	alerts = Alert.query.filter_by(id=alert_id).first()
	return render_template('editalertsform.html', alerts=alerts)

@app.route('/submitAlertEdits/<int:alert_id>', methods=['POST'])
def submitAlertEdits(alert_id):
	#if not session.get('logged_in'):
	#	abort(401)
	alert = Alert.query.filter_by(id=alert_id).first()
	alert.content = request.form['content']
	alert.category = request.form['category']
	alert.location = request.form['location']
	alert.start_date = request.form['start_date']
	alert.end_date = request.form['end_date']
	db.session.commit()
	return "Alert was successfully edited."


@app.route('/carousel')
def carousel():
    return render_template('carousel.html')

@app.route('/getArticleNumber')
def getArticleNumber():
    return 12

@app.route('/general', methods=['POST', 'GET'])
def generalPage():
    e = request.args['content']
    return render_template('pageTemplate.html', content=e)


@app.route('/loadJSON', methods=['POST', 'GET'])
def loadJson():
	j = open(os.path.join(os.path.dirname(__file__), 'static/json-data/about-page.json'), 'r')
	data = json.load(j)
	return jsonify(data)

###STATIC ROUTES SERVIN' UP SOME GOOD OL' FASHIONED HTML###
##MMMmmm MM good ol fashioned cooking!##

@app.route('/aboutUs', defaults={'subpage':None})
@app.route('/aboutUs/', defaults={'subpage':None})
@app.route('/aboutUs/<subpage>')
def aboutUs(subpage):
    if subpage is not None:
        uri = 'about/%s' % subpage + '.html'
        try:
            return render_template(uri)
        except TemplateNotFound:
            abort(404)
    else:
        return render_template('/about/index.html')


@app.route('/academics')
def academics():
    return render_template('academics/index.html')

@app.route('/research')
def research():
    return render_template('research/index.html')

@app.route('/opportunities')
def opportunites():
    return render_template('opportunities/index.html')

@app.route('/events')
def events():
    return render_template('events/index.html')

# @app.route('/support/')

##URLS are silly in flask, need to use a colon to separate the page, else if there's a trailing slash everything breaks###
@app.route('/support', defaults={'subpage':None})
@app.route('/support/', defaults={'subpage':None})
@app.route('/support/<subpage>')
def support(subpage):
    if subpage is not None:
        uri = 'support/%s' % subpage + '.html'
        try:
            return render_template(uri)
        except TemplateNotFound:
            abort(404)
    else:
        return render_template('/support/index.html')

#@app.route('/about')
# def aboutGeneral():
# return render_template('pageTemplate.html', content="about")

# @app.route('/academics')
# def aboutGeneral():
# 	return render_template('pageTemplate.html', content="academics")

@app.route('/loadProfile', methods=['POST', 'GET'])
def loadProfile():
    faculty_id = request.args['id']
    if request.method == 'GET':
        faculty = Faculty.query.filter_by(id=faculty_id).first()

        faculty_result = []
        faculty_dict = faculty.to_json_format()
        user_dict = faculty.user.to_json_format()
        json = util._merge_two_dicts(user_dict, faculty_dict)

        educations = faculty.educations
        edu_list = []
        for edu in educations:
            edu_list.append(edu.to_json_format())
        json = util._append_to_dict(json, edu_list, 'educations')

        faculty_services = faculty.faculty_services
        service_list = []
        for service in faculty_services:
            service_list.append(service.name)
        json = util._append_to_dict(json, service_list, 'services')

        faculty_interests = faculty.faculty_interests
        interest_list = []
        for interest in faculty_interests:
            interest_list.append(interest.interest)
        json = util._append_to_dict(json, interest_list, 'interests')

        faculty_committee_members = faculty.committee_members
        department_committee = []
        college_committee = []
        university_committee = []
        inter_department_committee = []
        professional_committee = []
        for member in faculty_committee_members:
            committee = member.committee
            if committee.category == 'department':
                department_committee.append(committee.name)
            elif committee.category == 'college':
                college_committee.append(committee.name)
            elif committee.category == 'university':
                university_committee.append(committee.name)
            elif committee.category == 'professional':
                professional_committee.append(committee.name)
            else:
                inter_department_committee.append(committee.name)
        json = util._append_to_dict(json, department_committee,
                                    'department_committee')
        json = util._append_to_dict(
            json, college_committee, 'college_committee')
        json = util._append_to_dict(json, university_committee,
                                    'university_committee')
        json = util._append_to_dict(json, inter_department_committee,
                                    'inter_department_committee')
        json = util._append_to_dict(json, professional_committee,
                                    'professional_committee')

        faculty_result.append(json)
        # return jsonify(faculty=faculty_result)
        return render_template("about/profile.html", data=faculty_result[0])
