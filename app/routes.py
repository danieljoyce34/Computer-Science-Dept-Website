from flask import render_template, request, jsonify, make_response, json
from flask import current_app, redirect, url_for, abort, Response, g, session
from app import app, db, loginManager
from .models import Image, Sideview, News, Colloquia, Alert, Faculty, User, Staff, Education
from .models import FacultyServices, FacultyInterests, CommitteeMembers, Committee
from .models import OfficeHours, Course
import util
import jinja2
from jinja2 import TemplateNotFound
from flask.ext.login import login_user, logout_user, current_user, login_required
import os
import random

from werkzeug import secure_filename

import datetime
from datetime import timedelta
from functools import update_wrapper
from sqlalchemy import desc

# Checks if a file is valid
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSION']

@app.route('/')
@app.route('/index')
def index():
    # Get active sideviews and randomly select 1
    sideviews = Sideview.query.filter_by(active=1).all()
    sideview = sideviews[random.randint(0, len(sideviews) - 1)]
    # Get alerts (most recent first)
    currDate = datetime.datetime.now()
    alerts = Alert.query.filter(Alert.end_date>=currDate).filter(Alert.start_date<=currDate).order_by(desc(Alert.id)).all()
    news = News.query.filter(News.end_date>=currDate).filter(News.start_date<=currDate).order_by(desc(News.post_date)).limit(10).all()
    carouselNews = []
    i = 1
    for new in news:
        json = new.to_json_format()
        if new.image is not None:
            json['image_url'] = '/static/images/news/' + new.image.image_name + '.' + new.image.image_extension
            json['num'] = i
        else:
            json['image_url'] = '/static/images/news/news-placeholder.jpg'
            json['num'] = i
        carouselNews.append(json)
        i = i+1
    return render_template('index.html', sideview=sideview, alerts=alerts, carouselNews=carouselNews)

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

@app.route('/colloquia/<int:colloquia_id>')
def getColloquiaWithId(colloquia_id):
    colloquia = Colloquia.query.filter_by(id=colloquia_id).first()
    if colloquia is None:
        abort(404)
    return render_template('news/ColloquiaArticle.html', colloquia=colloquia)

@app.route('/retrievePeople', methods=['GET'])
def allPeopleAjax(subpage):
    if request.method == 'GET':
        faculties = Faculty.query.all()

        people_result = []
        for faculty in faculties:
            img_name = faculty.user.image.image_name
            img_ext = faculty.user.image.image_extension
            img_url = '/static/images/faculty/' + img_name + "." + img_ext
            ptype = faculty.faculty_type
            ptype = ptype.title()
            json = {'user_id': faculty.user_id,
                    'name': faculty.user.fname + ' ' + faculty.user.lname,
                    'lname': faculty.user.lname,
                    'person_type': ptype,
                    'job_title': faculty.faculty_rank,
                    'status': faculty.status,
                    'image_url': img_url,
                    'profile_url': '/faculty/' + str(faculty.id)}
            people_result.append(json)

        staffs = Staff.query.all()
        for staff in staffs:
            img_url = '/static/images/staff/' + staff.user.lname + '.jpg'
            json = {'user_id': staff.user_id,
                    'name': staff.user.fname + ' ' + staff.user.lname,
                    'lname': staff.user.lname,
                    'person_type': 'Staff',
                    'job_title': staff.position,
                    'image_url': img_url,
                    'profile_url': '/staff/' + str(staff.id)}
            people_result.append(json)

        people_result = sorted(people_result, key=lambda k: k['lname'])

#        return render_template('about/faculty.html', people=people_result)
        return render_template('about/' + subpage + '.html', people=people_result)

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
    # TODO: still need to implement ldap support
    if username == 'djoyce' and password == 'wordpass':
        print(username)
        user = User.query.get(int(1))
        login_user(user, False)
        return redirect(request.args.get('next') or url_for('loggedInPage'))
    if username == 'alerts' and password == 'strela':
        print(username)
        user = User.query.get(int(2))
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

def uploadImage(type, imgfile, loc):
    filename = secure_filename(imgfile.filename)
    imgfile.save(os.path.join(loc, filename))
    filenameList = filename.split('.')
    image = Image(image_type=type, image_name=filenameList[0], image_extension=filenameList[1])
    db.session.add(image)
    db.session.commit()
    image = Image.query.order_by(desc(Image.id)).first()
    return image

@app.route('/sidebarEditor')
@login_required
def sidebarEditor():
    sideviews = Sideview.query.order_by(desc(Sideview.id)).all()
    sideimages = Image.query.filter_by(image_type='sidebar').all()
    return render_template('sidebar/sidebarEditor.html', sideviews=sideviews, images=sideimages)

@app.route('/addSidebar', methods=['POST'])
def addSideview():
    imgfile = request.files['img']
    imgId = 3
    if secure_filename(imgfile.filename) == "" and request.form['img-id'] != "":
        imgId = request.form['img-id']
    elif imgfile and allowed_file(imgfile.filename):
        sideImage = uploadImage('sidebar', imgfile, app.config['SIDEBAR_UPLOAD_FOLDER'])
        imgId = sideImage.id
    sideview = Sideview(title = request.form['title'],
                        content = request.form['content'],
                        category = request.form['category'],
                        active = 1 if 'active' in request.form else 0,
                        image_id = imgId)
    db.session.add(sideview)
    db.session.commit()

    newSideview = Sideview.query.order_by(desc(Sideview.id)).first()
    return json.dumps({'status' : 'OK', 'sideview' : newSideview.to_json_format() })

@app.route('/editSidebar/<int:sidebar_id>', methods=['POST'])
def editSideview(sidebar_id):
    sideview = Sideview.query.filter_by(id=sidebar_id).first()
    sideview.title = request.form['title']
    sideview.content = request.form['content']
    sideview.category = request.form['category']
    sideview.active = 1 if 'active' in request.form else 0
    imgfile = request.files['img']
    if secure_filename(imgfile.filename) == "":
        sideview.image_id = request.form['img-id']
    elif imgfile and allowed_file(imgfile.filename):
        sidebarImage = uploadImage('sidebar', imgfile, app.config['SIDEBAR_UPLOAD_FOLDER'])
        sideview.image_id = sidebarImage.id
    else:
        return json.dumps({'status' : 'ERROR'})
    db.session.commit()
    return json.dumps({'status' : 'OK', 'sideview' : sideview.to_json_format()})

@app.route('/admin')
@login_required
def loggedInPage():
    return render_template('user_options.html')

@app.route('/newsEditor')
@login_required
def newsEditor():
    news = News.query.order_by(desc(News.id)).all()
    newsimages = Image.query.filter_by(image_type='news').all()
    return render_template('news/newsEditor.html', news=news, images=newsimages)

@app.route('/addNews', methods=['POST'])
def addNews():
    imgfile = request.files['img']
    imgId = 4
    if secure_filename(imgfile.filename) == "" and request.form['img-id'] != "":
        imgId = request.form['img-id']
    elif imgfile and allowed_file(imgfile.filename):
        nImage = uploadImage('news', imgfile, app.config['NEWS_UPLOAD_FOLDER'])
        imgId = nImage.id
    news = News(headline = request.form['headline'],
                intro = request.form['intro'],
                article = request.form['article'],
                start_date = request.form['start_date'],
                end_date = request.form['end_date'],
                image_id = imgId)
    db.session.add(news)
    db.session.commit()

    newNews = News.query.order_by(desc(News.id)).first()
    return json.dumps({'status':'OK', 'news':newNews.to_json_format() })
    # TODO: Put error handling in a try catch statement or something
    #return json.dumps({'status' : 'ERROR'})

@app.route('/editNews/<int:news_id>', methods=['POST'])
def editNews(news_id):
    news = News.query.filter_by(id=news_id).first()
    news.headline = request.form['headline']
    news.intro = request.form['intro']
    news.article = request.form['article']
    news.start_date = request.form['start_date']
    news.end_date = request.form['end_date']
    # Saves image to static/image folder
    imgfile = request.files['img']
    if secure_filename(imgfile.filename) == "":
        news.image_id = request.form['img-id']
        db.session.commit()
        return json.dumps({'status' : 'OK', 'news':news.to_json_format() })
    elif imgfile and allowed_file(imgfile.filename):
        newsImage = uploadImage('news', imgfile, app.config['NEWS_UPLOAD_FOLDER'])
        news.image_id = newsImage.id
        db.session.commit()
        return json.dumps({'status' : 'OK', 'news':news.to_json_format() })
    return json.dumps({'status' : 'ERROR'})

@app.route('/colloquiaEditor')
@login_required
def colloquiaEditor():
    colloquia = Colloquia.query.order_by(desc(Colloquia.id)).all()
    return render_template('news/colloquiaEditor.html', colloquia=colloquia)

@app.route('/addColloquia', methods=['POST'])
def addColloquia():
    title = request.form['title']
    speaker = request.form['speaker']
    speaker_bio = request.form['speaker_bio']
    prelude = request.form['prelude']
    content = request.form['content']
    postlude = request.form['postlude']
    event_date = request.form['event_date']
    location = request.form['location']
    author = request.form['author']
    colloquia = Colloquia(title=title, speaker=speaker, speaker_bio=speaker_bio, prelude=prelude, content=content, postlude=postlude, event_date=event_date, location=location, author=author)
    try:
	db.session.add(colloquia)
        db.session.commit()
        newColloquia = Colloquia.query.order_by(desc(Colloquia.id)).first()
        return json.dumps({'status':'OK', 'colloquia':newColloquia.to_json_format() })
    except:
        # TODO: Put error handling in a try catch statement or something
        return json.dumps({'status' : 'ERROR'})

@app.route('/editColloquia/<int:colloquia_id>', methods=['POST'])
def editColloquia(colloquia_id):
    colloquia = Colloquia.query.filter_by(id=colloquia_id).first()
    colloquia.title = request.form['title']
    colloquia.speaker = request.form['speaker']
    colloquia.speaker_bio = request.form['speaker_bio']
    colloquia.prelude = request.form['prelude']
    colloquia.content = request.form['content']
    colloquia.postlude = request.form['postlude']
    colloquia.event_date = request.form['event_date']
    colloquia.location = request.form['location']
    colloquia.author = request.form['author']
    try:
        db.session.commit()
        return json.dumps({'status' : 'OK', 'colloquia':colloquia.to_json_format() })
    except:
	return json.dumps({'status' : 'ERROR'})

@app.route('/alertEditor')
@login_required
def alertEditor():
    alerts = Alert.query.order_by(desc(Alert.id)).all()
    return render_template('alerts/alertEditor.html', alerts=alerts)

@app.route('/addAlert', methods=['POST'])
def addAlert():
    content = request.json['content']
    start_date = request.json['start_date']
    end_date = request.json['end_date']
    author = request.json['author']
    alert = Alert(content=content, start_date=start_date, end_date=end_date, user_id=1, author=author)
    db.session.add(alert)
    db.session.commit()
    newAlert = Alert.query.order_by(desc(Alert.id)).first()
    user = User.query.filter_by(id=newAlert.user_id).first()
    alertUser = user.lname + ', ' + user.fname
    return json.dumps({'status' : 'OK', 'alertID' : newAlert.id, 'alertUser' : alertUser })


@app.route('/editAlert/<int:alert_id>', methods=['POST'])
def submitAlertEdits(alert_id):
    alert = Alert.query.filter_by(id=alert_id).first()
    alert.content = request.json['content']
    alert.start_date = request.json['start_date']
    alert.end_date = request.json['end_date']
    alert.author = request.json['author']
    db.session.commit()
    return json.dumps({'status' : 'OK'})

@app.route('/carousel')
def carousel():
    return render_template('carousel.html')

# next 3 routes are for compatibility with previous version of site and sites linking to us
@app.route('/about')
def about():
   return render_template('about/index.html')

@app.route('/prospective')
def prospective():
   return render_template('about/prospective.html')

@app.route('/faculty')
def faculty():
   return render_template('about/facStaff.html')

@app.route('/aboutUs', defaults={'subpage':None})
@app.route('/aboutUs/', defaults={'subpage':None})
@app.route('/aboutUs/<subpage>')
def aboutUs(subpage):
    if subpage is not None:
        uri = 'about/%s' % subpage + '.html'
        try:
            if subpage == 'faculty' or subpage == 'adjunct' or subpage == 'staff':
                return allPeopleAjax(subpage)
            elif subpage == 'committees':
                return allCommitteeInfo()
            else:
                return render_template(uri)
        except TemplateNotFound:
            abort(404)
    
    return render_template('/about/index.html')


@app.route('/academics', defaults={'subpage': None})
@app.route('/academics/<subpage>')
def academics(subpage):
    if subpage is not None:
        uri = 'academics/%s' % (subpage + '.html')
        try:
            if subpage == 'courses':
                return courseInfo()
            else:
                return render_template(uri)
        except TemplateNotFound:
            abort(404)
    
    return render_template('academics/index.html')

@app.route('/research', defaults={'subpage': None})
@app.route('/research/<subpage>')
def research(subpage):
    if subpage is not None:
        uri = 'research/%s' % (subpage + '.html')
        try:
            return render_template(uri)
        except TemplateNotFound:
            abort(404)

    return render_template('research/index.html')

@app.route('/gradGC', defaults={'subpage': None})
@app.route('/gradGC/<subpage>')
def gradGC(subpage):
    if subpage is not None:
        uri = 'academics/gradGC/%s' % (subpage + '.html')
        try:
            return render_template(uri)
        except TemplateNotFound:
            abort(404)

    return render_template('academics/gradGC/index.html')

@app.route('/opportunities', defaults={'subpage': None})
@app.route('/opportunities/<subpage>')
def opportunites(subpage):
    if subpage is not None:
        uri = 'opportunities/%s' % (subpage + '.html')
        try:
            return render_template(uri)
        except TemplateNotFound:
            abort(404)

    return render_template('opportunities/index.html')

@app.route('/news', defaults={'subpage': None})
@app.route('/news/<subpage>')
def news(subpage):
    if subpage is not None:
        uri = 'news/%s' % (subpage + '.html')
        try:
	    if subpage == 'colloquia' or subpage == 'Colloquia':
		colloquia = Colloquia.query.order_by(desc(Colloquia.id)).all()
	        return render_template(uri, colloquia=colloquia)
            else:
		return render_template(uri)
        except TemplateNotFound:
            abort(404)

    news = News.query.order_by(desc(News.id)).all()
    newsimages = Image.query.filter_by(image_type='news').all()
    return render_template('news/index.html', news=news, images=newsimages)


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

@app.route('/faculty/<int:faculty_id>', methods=['GET'])
def faculty_profile(faculty_id):
    if request.method == 'GET':
        faculty = Faculty.query.filter_by(id=faculty_id).first()

        if faculty.user.minit is None:
            faculty.user.minit = ''

        faculty_result = []
        faculty_dict = faculty.to_json_format()
        user_dict = faculty.user.to_json_format()
        json = util._merge_two_dicts(user_dict, faculty_dict)

        img_name = faculty.user.image.image_name
        img_ext = faculty.user.image.image_extension
        image_source = "/static/images/faculty/" + img_name + "." + img_ext
        json = util._append_to_dict(json, image_source, 'img_src')

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
        json = util._append_to_dict(json, department_committee, 'department_committee')
        json = util._append_to_dict(json, college_committee, 'college_committee')
        json = util._append_to_dict(json, university_committee, 'university_committee')
        json = util._append_to_dict(json, inter_department_committee, 'inter_department_committee')
        json = util._append_to_dict(json, professional_committee, 'professional_committee')

        officeHours = OfficeHours.query.filter_by(user_id=faculty.user_id)
        hours = [util._get_time(h.start_time) + "-" + util._get_time(h.start_time) + " " + h.days for h in officeHours]
        json = util._append_to_dict(json, hours, 'office_hours')

        json = util._append_to_dict(json, True, "isFaculty")

        faculty_result.append(json)
        return render_template("about/profile.html", data=faculty_result[0])

@app.route('/staff/<int:staff_id>', methods=['GET'])
def staff_profile(staff_id):
    if request.method == 'GET':
        staff = Staff.query.filter_by(id=staff_id).first()

        if staff.user.minit is None:
            staff.user.minit = ''

        staff_result = []
        staff_dict = staff.to_json_format()
        user_dict = staff.user.to_json_format()
        json = util._merge_two_dicts(user_dict, staff_dict)

        img_name = staff.user.image.image_name
        img_ext = staff.user.image.image_extension
        image_source = "/static/images/staff/" + img_name + "." + img_ext
        json = util._append_to_dict(json, image_source, 'img_src')

 #       staff_phones = staff.user.phone_numbers
 #       phone_list = []
 #       for p in staff_phones:
 #           phone_list = [p.area_code + p.number + (", Ext. " + p.extension if p.extension else "") for p in staff_phones]
 #       json = util._append_to_dict(json, phone_list, 'phone_number')

        staff_result.append(json)
        return render_template("about/profile.html", data=staff_result[0])



@app.route('/courses/<int:course_id>', methods=['GET'])
def course_info(course_id):
    if request.method == 'GET':
        course = Course.query.filter_by(id=course_id).first()

        course_result = []
        course_dict = course.to_json_format()
        json = course_dict

        objectives = course.objectives
        obj_list = [o.to_json_format() for o in objectives]
        obj_list = sorted(obj_list, key=lambda k: k['sequence'])
        json = util._append_to_dict(json, obj_list, 'objectives')

        course_result.append(json)

        return render_template("academics/courseInfo.html", data=course_result[0])


def courseInfo():
    if request.method == 'GET':
        courses = Course.query.all()

        cou_result = []
        for c in courses:
            json = {'couid': c.id,
                    'course': c.course,
                    'department': c.department,
                    'title': c.title,
                    'credits': c.credits,
                    'level': c.level,
                    'description': c.description,
                    'prerequisites': c.prerequisites}
            cou_result.append(json)

        cou_result = sorted(cou_result, key=lambda k: k['course'])

        return render_template('academics/courses.html', courses=cou_result)

@app.route('/retreiveCommitteeInfo', methods=['GET'])
def allCommitteeInfo():
    if request.method == 'GET':
        committees = Committee.query.all()

        com_result = []
        for c in committees:
            json = {'comid': c.id,
                    'name': c.name,
                    'category': c.category,
                    'description': c.description}
            com_result.append(json)

        com_result = sorted(com_result, key=lambda k: k['name'])


        members = CommitteeMembers.query.all()

        mem_result = []
        for m in members:
            json = {'facid': m.faculty_id,
                    'name': m.faculty.user.fname + ' ' + m.faculty.user.lname,
                    'committee': m.committee.name,
                    'role': m.role}
            mem_result.append(json)

        mem_result = sorted(mem_result, key=lambda k: k['role'])

        return render_template('about/committees.html', committees=com_result, members=mem_result)
