from flask import render_template, request, jsonify, make_response, request, current_app
from app import app
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


@app.route('/retrieveSideviews', methods=['GET'])
@crossdomain(origin='*')
def sideviewsAjax():
    if request.method == 'GET':
        sideviews = Sideview.query.all()

        sideview_result = []
        for sideview in sideviews:
            json = sideview.to_json_format()
            sideview_result.append(json)
        return jsonify(sideviews=sideview_result)

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


@app.route('/carousel')
def carousel():
    return render_template('carousel.html')

@app.route('/professors')
def professorsPages():
    return render_template('professors.html')


@app.route('/article', methods=['POST', 'GET'])
def article():

    # QUERY DATABASE HERE
    results = {}
    results['articleImage'] = '120003'
    results['articleHeader'] = 'There is some data'
    results['articleContent'] = 'We have contempt for our content'
    return render_template('article.html', data=results)


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
