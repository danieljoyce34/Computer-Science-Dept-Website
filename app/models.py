from app import db
import datetime
import util


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_type = db.Column(db.String(64))
    alt_text = db.Column(db.Text)
    image_extension = db.Column(db.String(64))
    image_name = db.Column(db.Text)
    sideviews = db.relationship('Sideview',
                                backref=db.backref('image'),
                                uselist=False)
    news = db.relationship('News',
                           backref=db.backref('image'),
                           uselist=False)
    users = db.relationship('User',
                            backref=db.backref('image'),
                            uselist=False)

    def to_json_format(self):
        json = {'id': self.id,
                'image_type': self.image_type,
                'alt_text': self.alt_text,
                'image_extension': self.image_extension,
                'image_name': self.image_name}
        return json

    def __repr__(self):
        return ('<Image id %i, image_type %s, alt_text %s, image_extension %s>'
                % (self.id, self.image_type, self.alt_text, self.image_extension))


class Sideview(db.Model):
    __tablename__ = 'sideviews'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    title = db.Column(db.String(64))
    category = db.Column(db.String(64))
    active = db.Column(db.Integer)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'content': self.content,
                'title': self.title,
                'category': self.category,
                'active': self.active,
                'image_id': self.image_id}
        return json

    def __repr__(self):
        return ('<Sideview id %i, content %s, title %s, active %i, image_id %i>'
                % (self.id, self.content, self.title, self.active, self.image_id))


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, default=datetime.date.today())
    end_date = db.Column(db.DateTime, default=util._next_month())
    headline = db.Column(db.String(64))
    intro = db.Column(db.Text)
    article = db.Column(db.Text)
    post_date = db.Column(db.DateTime, default=datetime.date.today())
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'headline': self.headline,
                'intro': self.intro,
                'article': self.article,
                'post_date': self.post_date, 
                'image_id': self.image_id}
        return json

    def __repr__(self):
        return ('<News id %i, start_date %s, end_date %s, headline %s, intro %s,'
                ' article %s, post_date %s, image_id %i>'
                % (self.id, str(self.start_date), str(self.end_date), self.headline,
                    self.intro, self.article, str(self.post_date), self.image_id))


class Colloquia(db.Model):
    __tablename__ = 'colloquia'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    speaker = db.Column(db.Text)
    speaker_bio = db.Column(db.Text)
    prelude = db.Column(db.Text)
    content = db.Column(db.Text)
    postlude = db.Column(db.Text)
    event_date = db.Column(db.DateTime, default=datetime.date.today())
    location = db.Column(db.Text)
    author = db.Column(db.Text)

    def to_json_format(self):
        json = {'id': self.id,
                'title': self.title,
		'speaker': self.speaker,
		'speaker_bio': self.speaker_bio,
		'prelude': self.prelude,
                'content': self.content,
		'postlude': self.postlude,
		'event_date': self.event_date,
		'location': self.location,
		'author': self.author}
        return json

    def __repr__(self):
        return ('<Colloquia id %i, title %s, speaker %s, speaker_bio %s,'
        	' prelude %s, content %s, postlude %s, event_date %s, location %s,'
        	' author %s>'
                % (self.id, self.title, self.speaker, self.speaker_bio, self.prelude,
                    self.content, self.postlude, str(self.event_date), self.location, 
                    self.author))


class Alert(db.Model):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    start_date = db.Column(db.DateTime, default=datetime.date.today())
    end_date = db.Column(db.DateTime, default=util._next_month())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.Column(db.String(32))

    def to_json_format(self):
        json = {'id': self.id,
                'content': self.content,
                'user_id': self.user_id,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'author': self.author}
        return json

    def __repr__(self):
        return ('<Alert id %i, content %s, user_id %i,'
                ' start_date %s, end_date %s, author %s>'
                % (self.id, self.content, self.user_id, str(self.start_date),
                    str(self.end_date), self.author))



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(32))
    minit = db.Column(db.String(2))
    lname = db.Column(db.String(32))
    email = db.Column(db.String(64))
    vu_ldap = db.Column(db.String(64))
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    user_role_id = db.Column(db.Integer, db.ForeignKey('user_role.id'))
    staffs = db.relationship('Staff',
                             backref=db.backref('user'),
                             uselist=False)
    administrations = db.relationship('Administration',
                                      backref=db.backref('user'),
                                      uselist=False)
    phone_numbers = db.relationship('PhoneNumber',
                                    backref=db.backref('user'))
    addresses = db.relationship('Address',
                                backref=db.backref('user'))
    office_hours = db.relationship('OfficeHours',
                                   backref=db.backref('user'))
    faculties = db.relationship('Faculty',
                                backref=db.backref('user'),
                                uselist=False)
    alerts = db.relationship('Alert',
                             backref=db.backref('user'))
    exit_interview = db.relationship('ExitInterview',
                                     backref=db.backref('user'),
                                     uselist=False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def to_json_format(self):
        json = {'id': self.id,
                'fname': self.fname,
                'minit': self.minit,
                'lname': self.lname,
                'email': self.email,
                'vu_ldap': self.vu_ldap,
                'image_id': self.image_id,
                'user_role_id': self.user_role_id}
        return json

    def __repr__(self):
        return ('<User id %i, fname %s, minit %s, lname %s, email %s, vu_ldap %s,'
                'image_id %i, user_role_id %i>'
                % (self.id, self.fname, self.minit, self.lname, self.email,
                   self.vu_ldap, self.image_id, self.user_role_id))


class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(32))
    users = db.relationship('User', backref=db.backref('user_role',),
                            uselist=False)

    def to_json_format(self):
        json = {'id': self.id,
                'role': self.role}
        return json

    def __repr__(self):
        return ('<UserRole id %i, role %s>' % (self.id, self.role))


class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(64))
    office_loc = db.Column(db.String(64))
    phone_num = db.Column(db.String(32))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'position': self.position,
                'office_loc': self.office_loc,
                'phone_num': self.phone_num,
                'user_id': self.user_id}
        return json

    def __repr__(self):
        return ('<Staff id %i, position %s, office_loc %s, phone_num %s, user_id %i>'
                % (self.id, self.position, self.office_loc, self.phone_num, self.user_id))


class Administration(db.Model):
    __tablename__ = 'administration'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128))
    priority = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'description': self.description,
                'priority': self.priority,
                'user_id': self.user_id}
        return json

    def __repr__(self):
        return ('<Administration id %i, description %s, priority %s, user_id %i>'
                % (self.id, self.description, self.priority, self.user_id))


class PhoneNumber(db.Model):
    __tablename__ = 'phone_number'
    id = db.Column(db.Integer, primary_key=True)
    area_code = db.Column(db.String(8))
    number = db.Column(db.String(8))
    extension = db.Column(db.String(8))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'area_code': self.area_code,
                'number': self.number,
                'extension': self.extension,
                'user_id': self.user_id}
        return json

    def __repr__(self):
        return ('<PhoneNumber id %i, area_code %s, number %s, extension %s,'
                ' user_id %i>'
                % (self.id, self.area_code, self.number, self.extension))


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    line1 = db.Column(db.String(32))
    line2 = db.Column(db.String(32))
    city = db.Column(db.String(32))
    state = db.Column(db.String(32))
    zip = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'line1': self.line1,
                'line2': self.line2,
                'city': self.city,
                'state': self.state,
                'zip': self.zip,
                'user_id': self.user_id}
        return json

    def __repr__(self):
        return ('<Address id %i, line1 %s, line2 %s, city %s, state %s, zip %i'
                ' user_id %i>'
                % (self.id, self.line1, self.line2, self.city, self.state, self.zip,
                    self.user_id))


class OfficeHours(db.Model):
    __tablename__ = 'office_hours'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    days = db.Column(db.String(5))
    apntmnt_msg = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'start_time': self.start_time,
                'end_time': self.end_time,
                'days': self.days,
                'apntmnt_msg': self.apntmnt_msg,
                'user_id': self.user_id}
        return json

    def __repr__(self):
        return ('<OfficeHours id %i, start_time %s, end_time %s, days %s,'
                ' apntmnt_msg %s, user_id %i, term_id %i>'
                % (self.id, str(self.start_time), str(self.end_time), self.days,
                    self.apntmnt_msg, self.user_id, self.term_id))


class Term(db.Model):
    __tablename__ = 'term'
    id = db.Column(db.Integer, primary_key=True)
    semester = db.Column(db.String(16))
    year = db.Column(db.Integer)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    courses = db.relationship('Course',
                              backref=db.backref('term'))

    def to_json_format(self):
        json = {'id': self.id,
                'semester': self.semester,
                'year': self.year,
                'start_date': self.start_date,
                'end_date': self.end_date}
        return json

    def __repr__(self):
        return ('<Term id %i, semester %s, year %i, start_date %s, end_date %s>'
                % (self.id, self.semester, self.year, str(self.start_date),
                   str(self.end_date)))


class Faculty(db.Model):
    __tablename__ = 'faculty'
    id = db.Column(db.Integer, primary_key=True)
    salutation = db.Column(db.String(32))
    secondary_email = db.Column(db.String(64))
    website_url = db.Column(db.String(128))
    faculty_type = db.Column(db.String(32))
    faculty_rank = db.Column(db.String(32))
    status = db.Column(db.String(32))
    office_loc = db.Column(db.String(64))
    phone_num = db.Column(db.String(32))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    educations = db.relationship('Education',
                                 backref=db.backref('faculty'))
    faculty_services = db.relationship('FacultyServices',
                                       backref=db.backref('faculty'))
    faculty_interests = db.relationship('FacultyInterests',
                                        backref=db.backref('faculty'))
    committee_members = db.relationship('CommitteeMembers',
                                        backref=db.backref('faculty'))

    def to_json_format(self):
        json = {'id': self.id,
                'salutation': self.salutation,
                'secondary_email': self.secondary_email,
                'website_url': self.website_url,
                'faculty_type': self.faculty_type,
                'faculty_rank': self.faculty_rank,
                'status': self.status,
                'office_loc': self.office_loc,
                'phone_num': self.phone_num,
                'user_id': self.user_id}
        return json

    def __repr__(self):
        return ('<Faculty id %i, salutation %s, secondary_email %s, website_url %s,'
                ' faculty_type %s, faculty_rank %s, status %s, office_loc %s,'
                ' phone_num %s, user_id %s>'
                % (self.id, self.salutation, self.secondary_email, self.website_url,
                    self.faculty_type, self.faculty_rank, self.status,
                    self.office_loc, self.phone_num, self.user_id))


class Education(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(64))
    discipline = db.Column(db.String(128))
    school = db.Column(db.String(128))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'degree': self.degree,
                'discipline': self.discipline,
                'school': self.school,
                'faculty_id': self.faculty_id}
        return json

    def __repr__(self):
        return ('<Education id %i, degree %s, discipline %s, school %s,'
                ' faculty_id %s>'
                % (self.id, self.degree, self.discipline, self.school,
                    self.faculty_id))


class FacultyServices(db.Model):
    __tablename__ = 'faculty_services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    category = db.Column(db.String(64))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'service_name': self.service_name,
                'category': self.category,
                'faculty_id': self.faculty_id}
        return json

    def __repr__(self):
        return ('<FacultyServices %i, service_name %s, category %s, faculty_id %i>'
                % (self.id, self.service_name, self.category, self.faculty_id))


class FacultyInterests(db.Model):
    __tablename__ = 'faculty_interests'
    id = db.Column(db.Integer, primary_key=True)
    interest = db.Column(db.String(64))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'interest': self.interest,
                'faculty_id': self.faculty_id}
        return json

    def __repr__(self):
        return ('<FacultyInterests id %i, interest %s, faculty_id %i>'
                % (self.id, self.interest, self.faculty_id))


class CommitteeMembers(db.Model):
    __tablename__ = 'committee_members'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(64))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    committee_id = db.Column(db.Integer, db.ForeignKey('committees.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'role': self.role,
                'faculty_id': self.faculty_id,
                'committee_id': self.committee_id}
        return json

    def __repr__(self):
        return ('<CommitteeMembers id %i, role %s, faculty_id %i, committee_id %i>'
                % (self.id, self.role, self.faculty_id, self.committee_id))


class Committee(db.Model):
    __tablename__ = 'committees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    category = db.Column(db.String(64))
    description = db.Column(db.Text)
    committee_members = db.relationship('CommitteeMembers',
                                        backref=db.backref('committee'))

    def to_json_format(self):
        json = {'id': self.id,
                'name': self.name,
                'category': self.category,
                'description': self.description}
        return json

    def __repr__(self):
        return ('<Committee id %i, name %s, category %s, description %s>'
                % (self.id, self.name, self.category, self.description))


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(16))
    department = db.Column(db.String(64))
    title = db.Column(db.String(64))
    credits = db.Column(db.Integer)
    level = db.Column(db.String(16))
    description = db.Column(db.Text)
    prerequisites = db.Column(db.String(64))
    term_id = db.Column(db.Integer, db.ForeignKey('term.id'))
    objectives = db.relationship('Objective',
                                 backref=db.backref('courses'))

    def to_json_format(self):
        json = {'id': self.id,
                'course': self.course,
                'department': self.department,
                'title': self.title,
                'credits': self.credits,
                'level': self.level,
                'description': self.description,
                'prerequisites': self.prerequisites,
                'term_id': self.term_id}
        return json

    def __repr__(self):
        return ('<Course id %i, course %s, department %s, title %s, credits %i, level %s,'
                ' description %s, prerequisites %s, term_id %i>'
                % (self.id, self.course, self.department, self.title, self.credits,
                    self.level, self.description, self.prerequisites, self.term_id))


class Objective(db.Model):
    __tablename__ = 'objectives'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    objective = db.Column(db.Text)
    sequence = db.Column(db.Integer)

    def to_json_format(self):
        json = {'id': self.id,
                'course_id': self.course_id,
                'objective': self.objective,
                'sequence': self.sequence}
        return json

    def __repr__(self):
        return ('<Objective id %i, course_id %i, objective %s, sequence %i>'
                % (self.id, self.course_id, self.objective, self.sequence))


class ExitInterview(db.Model):
    __tablename__ = 'exit_interview'
    id = db.Column(db.Integer, primary_key=True)
    face_interview = db.Column(db.Integer)  # should be a tinyint
    cs_improvement_suggestions = db.Column(db.Text)
    sufficient_info_for_future = db.Column(db.Text)
    valueable_aspects = db.Column(db.Text)
    language_proficiency = db.Column(db.Text)
    curriculum_comment = db.Column(db.Text)
    general_course_comment = db.Column(db.Text)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('exit_interview_job.id'))
    grad_school_id = db.Column(
        db.Integer, db.ForeignKey('exit_interview_grad_school.id'))
    exit_interview_course_evaluation = db.relationship('ExitInterviewCourseEvaluation',
                                                       backref=db.backref('exit_interview_course_evaluation'))

    def to_json_format(self):
        json = {'id': self.id,
                'user_id': self.user_id,
                'job_id': self.job_id,
                'grad_school_id': self.grad_school_id,
                'face_interview': self.face_interview,
                'cs_improvement_suggestions': self.cs_improvement_suggestions,
                'sufficient_info_for_future': self.sufficient_info_for_future,
                'valueable_aspects': self.valueable_aspects,
                'language_proficiency': self.language_proficiency,
                'curriculum_comment': self.curriculum_comment,
                'general_course_comment': self.general_course_comment,
                'creation_date': self.creation_date}
        return json

    def __repr__(self):
        return ('<id %i, user_id %i, job_id %s, grad_school_id %f,'
                ' face_interview %f, cs_improvement_suggestions %s,'
                ' sufficient_info_for_future %s, valueable_aspects %s,'
                ' language_proficiency %s, curriculum_comment %s,'
                ' general_course_comment %s creation_date %f>'
                % (self.id, self.user_id, self.job_id, self.grad_school_id,
                    self.face_interview, self.cs_improvement_suggestions,
                    self.sufficient_info_for_future, self.valueable_aspects,
                    self.language_proficiency, self.curriculum_comment,
                    self.general_course_comment, str(self.creation_date)))


class ExitInterviewJob(db.Model):
    __tablename__ = 'exit_interview_job'
    id = db.Column(db.Integer, primary_key=True)
    job_found = db.Column(db.Integer)
    company_name = db.Column(db.String(128))
    job_location = db.Column(db.String(128))
    job_title = db.Column(db.String(128))
    salary = db.Column(db.String(8))
    reasons_joined = db.Column(db.Text)
    other_offers = db.Column(db.Text)
    comments = db.Column(db.Text)
    exit_interview = db.relationship('ExitInterview',
                                     backref=db.backref('exit_interview_job'),
                                     uselist=False)

    def to_json_format(self):
        json = {'id': self.id,
                'job_found': self.job_found,
                'company_name': self.company_name,
                'job_location': self.job_location,
                'job_title': self.job_title,
                'salary': self.salary,
                'reasons_joined': self.reasons_joined,
                'other_offers': self.other_offers,
                'comments': self.comments}
        return json

    def __repr__(self):
        return ('<id %i, job_found %i, company_name %s, job_location %s, job_title %s,'
                ' salary %s, reasons_joined %s, other_offers %s, comments %s>'
                % (self.id, self.job_found, self.company_name, self.job_location,
                    self.job_title, self.salary, self.reasons_joined, other_offers,
                    self.comments))


class ExitInterviewCourseEvaluation(db.Model):
    __tablename__ = 'exit_interview_course_evaluation'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer)
    course_rating = db.Column(db.String(32))
    course_comment = db.Column(db.Text)
    exit_interview_id = db.Column(
        db.Integer, db.ForeignKey('exit_interview.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'exit_interview_id': self.exit_interview_id,
                'course_id': self.course_id,
                'course_rating': self.course_rating,
                'course_comment': self.course_comment}
        return json

    def __repr__(self):
        return ('<id %i, exit_interview_id %i, course_id %i, course_rating %s,'
                ' course_comment %s>'
                % (self.id, self.exit_interview_id,  self.course_id,
                    self.course_rating, self.course_comment))


class ExitInterviewGradSchool(db.Model):
    __tablename__ = 'exit_interview_grad_school'
    id = db.Column(db.Integer, primary_key=True)
    grad_school_name = db.Column(db.String(256))
    field_of_study = db.Column(db.String(128))
    acceptance = db.Column(db.Integer)
    aid = db.Column(db.String(128))
    exit_interview = db.relationship('ExitInterview',
                                     backref=db.backref(
                                         'exit_interview_grad_school'),
                                     uselist=False)

    def to_json_format(self):
        json = {'id': self.id,
                'grad_school_name': self.grad_school_name,
                'field_of_study': self.field_of_study,
                'acceptance': self.acceptance,
                'aid': self.aid}
        return json

    def __repr__(self):
        return ('<id %i, grad_school_name %s, field_of_study %s, acceptance %i aid %s>'
                % (self.id, self.grad_school_name, self.field_of_study,
                    self.acceptance, self.aid))
