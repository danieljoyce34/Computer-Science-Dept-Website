from flask import render_template, request, jsonify, make_response, json
from flask import current_app, redirect, url_for, abort, Response, g, session
from app import app, db, loginManager
from .models import Image, Sideview, News, Alert, Faculty, User, Staff, Education
from .models import FacultyServices, FacultyInterests, CommitteeMembers, Committee, OfficeHours
import util
import jinja2
from jinja2 import TemplateNotFound
from flask.ext.login import login_user, logout_user, current_user, login_required
import os
import random

from werkzeug import secure_filename

from datetime import timedelta
from functools import update_wrapper
from sqlalchemy import desc

# Folder path for uploading images
UPLOAD_FOLDER = '/app/static/images/'
NEWS_UPLOAD_FOLDER = UPLOAD_FOLDER + 'news/'
SIDEBAR_UPLOAD_FOLDER = UPLOAD_FOLDER + 'sidebar/'
# File limitations for uploading images
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# Checks if a file is valid
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():
    sideviews = Sideview.query.all()
    sideview = sideviews[random.randint(0, len(sideviews) - 1)]

    alerts = Alert.query.order_by(desc(Alert.id)).all()

    news = News.query.limit(4).all()
    carouselNews = []
    for new in news:
        json = new.to_json_format()
        json['image_url'] = '/static/images/image1.jpg'
        carouselNews.append(json)

    return render_template('index.html', sideview=sideview, alerts=alerts,
                            carouselNews=carouselNews)

@app.route('/news/<int:news_id>')
def getNewsWithId(news_id):
    news = News.query.filter_by(id=news_id).first()
    if news is None:
        abort(404)
    if news.image is None:
        image = '/static/images/image1.jpg'
    else:
        image = '/static/images/news/' + news.image.image_name + '.' + news.image.image_extension
    return render_template('news/NewsArticle.html', news=news, image=image)

@app.route('/retrievePeople', methods=['GET'])
def allPeopleAjax():
    if request.method == 'GET':
        faculties = Faculty.query.all()

        people_result = []
        for faculty in faculties:
            json = {'user_id': faculty.user_id,
                    'name': faculty.user.fname + ' ' + faculty.user.lname,
                    'person_type': faculty.faculty_type,
                    'job_title': faculty.faculty_rank,
                    'image_url': '/static/images/image1.jpg'}
            people_result.append(json)

        staffs = Staff.query.all()
        for staff in staffs:
            json = {'user_id': staff.user_id,
                    'name': staff.user.fname + ' ' + staff.user.lname,
                    'person_type': 'staff',
                    'job_title': staff.position,
                    'image_url': '/static/images/image1.jpg'}
            people_result.append(json)
        return render_template('about/faculty.html', people=people_result)


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('user_options'))
    return render_template('login/login.html')

@app.route('/submitLogin', methods=['POST'])
def submitLogin():
    username = request.form['username']
    password = request.form['password']
    # user fake user below for now
    if username == 'graduate' and password == 'password':
        print(username)
        user = User.query.get(int(1))
        login_user(user, False)
        return redirect(request.args.get('next') or url_for('loggedInPage'))
    if username == 'faculty' and password == 'password':
        print(username)
        user = User.query.get(int(2))
        login_user(user, False)
        return redirect(request.args.get('next') or url_for('loggedInPage'))
    if username == 'staff' and password == 'password':
        print(username)
        user = User.query.get(int(3))
        login_user(user, False)
        return redirect(request.args.get('next') or url_for('loggedInPage'))
    if username == 'undergrad' and password == 'password':
        print(username)
        user = User.query.get(int(4))
        login_user(user, False)
        return redirect(request.args.get('next') or url_for('loggedInPage'))
    if username == 'webteam' and password == 'password':
        print(username)
        user = User.query.get(int(5))
        login_user(user, False)
        return redirect(request.args.get('next') or url_for('loggedInPage'))
    # on the machine that's whitelisted, we need to check if user already
    # exist in our db, if not create the user
    return redirect(url_for('login') + '?failed=true')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@loginManager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/sidebarEditor')
#@login_required
def sidebarEditor():
    sideviews = Sideview.query.order_by(desc(Sideview.id)).all()
    return render_template('sidebar/sidebarEditor.html', sideviews=sideviews)

@app.route('/addSidebar', methods=['POST'])
def addSideview():
    title = request.form['title']
    content = request.form['content']
    category = request.form['category']
    active = 1 if 'active' in request.form else 0
    # Saves image to static/image folder
    imgfile = request.files['img']
    if secure_filename(imgfile.filename) == "":
        sideview = Sideview(title = title, content = content, category = category, active = active)
        db.session.add(sideview)
        db.session.commit()
        newSideview = Sideview.query.order_by(desc(Sideview.id)).first()
    elif imgfile and allowed_file(imgfile.filename):
        filename = secure_filename(imgfile.filename)
        imgfile.save(os.path.join(app.config['SIDEBAR_UPLOAD_FOLDER'], filename))
        filenameList = filename.split('.')
        sideImage = Image(image_type='sidebar', image_name=filenameList[0], image_extension=filenameList[1])
        db.session.add(sideImage)
        sideview = Sideview(title = title, content = content, category = category, active = active, image=sideImage)
        db.session.add(sideview)
        db.session.commit()

        newSideview = Sideview.query.order_by(desc(Sideview.id)).first()
    return json.dumps({'status' : 'OK', 'sideviewID' : newSideview.id})

@app.route('/editSidebar/<int:sidebar_id>', methods=['POST'])
def editSideview(sidebar_id):
    sideview = Sideview.query.filter_by(id=sidebar_id).first()
    sideview.title = request.form['title']
    sideview.content = request.form['content']
    sideview.category = request.form['category']
    sideview.active = 1 if 'active' in request.form else 0
    # Saves image to static/image folder
    imgfile = request.files['img']
    if secure_filename(imgfile.filename) == "":
        db.session.commit()
        return json.dumps({'status' : 'OK'})
    elif imgfile and allowed_file(imgfile.filename):
        filename = secure_filename(imgfile.filename)
        imgfile.save(os.path.join(app.config['SIDEBAR_UPLOAD_FOLDER'], filename))
    
        db.session.commit()
        return json.dumps({'status' : 'OK'})
    return json.dumps({'status' : 'ERROR'})
@app.route('/admin')
@login_required
def loggedInPage():
    return render_template('user_options.html')

@app.route('/newsEditor')
@login_required
def newsEditor():
    news = News.query.order_by(desc(News.id)).all()
    return render_template('news/newsEditor.html', news=news)

@app.route('/addNews', methods=['POST'])
def addNews():
    headline = request.form['headline']
    intro = request.form['intro']
    article = request.form['article']
    start = request.form['start_date']
    end = request.form['end_date']
    # Saves image to static/image folder
    imgfile = request.files['img']
    if secure_filename(imgfile.filename) == "":
        news = News(headline=headline, intro=intro, article=article, start_date=start, end_date=end)
        db.session.add(news)
        db.session.commit()

        newNews = News.query.order_by(desc(News.id)).first()
        return json.dumps({'status' : 'OK', 'newsID' : newNews.id})
    elif imgfile and allowed_file(imgfile.filename):
        filename = secure_filename(imgfile.filename)
        imgfile.save(os.path.join(app.config['NEWS_UPLOAD_FOLDER'], filename))
        filenameList = filename.split('.')
        newsImage = Image(image_type='news', image_name=filenameList[0], image_extension=filenameList[1])
        db.session.add(newsImage)

        news = News(headline=headline, intro=intro, article=article, start_date=start, end_date=end, image=newsImage)
        db.session.add(news)
        db.session.commit()

        newNews = News.query.order_by(desc(News.id)).first()
        return json.dumps({'status' : 'OK', 'newsID' : newNews.id})
    return json.dumps({'status' : 'ERROR'})

@app.route('/editNews/<int:news_id>', methods=['POST'])
def editNews(news_id):
    news = News.query.filter_by(id=news_id).first()
    news.headline = request.form['headline']
    news.intro = request.form['intro']
    news.article = request.form['article']
    news.start = request.form['start_date']
    news.end = request.form['end_date']
    # Saves image to static/image folder
    imgfile = request.files['img']
    if secure_filename(imgfile.filename) == "":
        db.session.commit()
        return json.dumps({'status' : 'OK'})
    if imgfile and allowed_file(imgfile.filename):
        filename = secure_filename(imgfile.filename)
        imgfile.save(os.path.join(app.config['NEWS_UPLOAD_FOLDER'], filename))
        db.session.commit()
        return json.dumps({'status' : 'OK'})
    return json.dumps({'status' : 'ERROR'})

@app.route('/alertEditor')
@login_required
def alertEditor():
    alerts = Alert.query.order_by(desc(Alert.id)).all()
    return render_template('alerts/alertEditor.html', alerts=alerts)

@app.route('/addAlert', methods=['POST'])
def addAlert():
    content = request.json['content']
    category = request.json['category']
    start_date = request.json['start_date']
    end_date = request.json['end_date']
    alert = Alert(content=content, category=category, start_date=start_date, end_date=end_date, user_id=1)
    db.session.add(alert)
    db.session.commit()
    newAlert = Alert.query.order_by(desc(Alert.id)).first()
    user = User.query.filter_by(id=newAlert.user_id).first()
    alertUser = user.lname + ', ' + user.fname
    return json.dumps({'status' : 'OK', 'alertID' : newAlert.id, 'alertPostDate' : newAlert.post_date, 'alertUser' : alertUser })


@app.route('/editAlert/<int:alert_id>', methods=['POST'])
def submitAlertEdits(alert_id):
    alert = Alert.query.filter_by(id=alert_id).first()
    alert.content = request.json['content']
    alert.category = request.json['category']
    alert.start_date = request.json['start_date']
    alert.end_date = request.json['end_date']
    db.session.commit()
    return json.dumps({'status' : 'OK'})

@app.route('/carousel')
def carousel():
    return render_template('carousel.html')

###STATIC ROUTES SERVIN' UP SOME GOOD OL' FASHIONED HTML###
##MMMmmm MM good ol fashioned cooking!##

@app.route('/aboutUs', defaults={'subpage':None})
@app.route('/aboutUs/', defaults={'subpage':None})
@app.route('/aboutUs/<subpage>')
def aboutUs(subpage):
    if subpage is not None:
        uri = 'about/%s' % subpage + '.html'
        try:
            if subpage == 'faculty':
                return allPeopleAjax()
            else:
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
        faculty = Faculty.query.filter_by(user_id=faculty_id).first()

        faculty_result = []
        faculty_dict = faculty.to_json_format()
        user_dict = faculty.user.to_json_format()
        json = util._merge_two_dicts(user_dict, faculty_dict)

        educations = faculty.educations
        edu_list = [e.to_json_format() for e in educations]
        json = util._append_to_dict(json, edu_list, 'educations')

        faculty_services = faculty.faculty_services
        service_list = [service.name for service in faculty_services]
        json = util._append_to_dict(json, service_list, 'services')

        faculty_interests = faculty.faculty_interests
        interest_list = [interest.interest for interest in faculty_interests]
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

        officeHours = OfficeHours.query.filter_by(user_id=faculty_id)
        #for h in officeHours:
        #    hs = util._get_time(h.start_time) + " - " + util._get_time(h.start_time) + h.days
        hours = [util._get_time(h.start_time) + "-" + util._get_time(h.start_time) + " " + h.days for h in officeHours]
        #start_time = [util._get_time(oh.start_time) for oh in officeHours]
        #end_time = [util._get_time(oh.end_time) for oh in officeHours]
        #days = [oh.days for oh in officeHours]
        #hours = {'start':start_time, 'end':end_time, 'days':days}
        json = util._append_to_dict(json, hours, 'office_hours')
        #json = util._append_to_dict(json, start_time, 'office_hours_start')
        #json = util._append_to_dict(json, end_time, 'office_hours_end')
        #json = util._append_to_dict(json, days, 'office_hours_days')

        faculty_result.append(json)
        # return jsonify(faculty=faculty_result)
        return render_template("about/profile.html", data=faculty_result[0])
