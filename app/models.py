from app import db
import datetime
import util


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_type = db.Column(db.String(64))
    alt_text = db.Column(db.Text)
    image_extension = db.Column(db.String(64))
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
                'image_extension': self.image_extension}
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
        return ('<News id %i, start_date %f, end_date %f, headline %s, intro %s,'
                ' article %s, post_date %f, image_id %i>'
                % (self.id, self.start_date, self.end_date, self.headline,
                    self.intro, self.article, self.post_date, self.image_id))


class Alert(db.Model):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    category = db.Column(db.String(64))
    post_date = db.Column(db.DateTime, default=datetime.date.today())
    location = db.Column(db.String(64))
    start_date = db.Column(db.DateTime, default=datetime.date.today())
    end_date = db.Column(db.DateTime, default=util._next_month())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'content': self.content,
                'user_id': self.user_id,
                'category': self.category,
                'post_date': self.post_date,
                'location': self.location,
                'start_date': self.start_date,
                'end_date': self.end_date}
        return json

    def __repr__(self):
        return ('<Alert id %i, content %s, user_id %i, category %s, post_date %f,'
                ' location %s, start_date %f, end_date %f>'
                % (self.id, self.content, self.user_id, self.category,
                    self.post_date, self.location, self.start_date, self.end_date))


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
                ' image_id %i, user_role_id %i>'
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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'position': self.position,
                'office_loc': self.office_loc,
                'user_id': self.user_id}
        return json

    def __repr__(self):
        return ('<Staff id %i, position %s, office_loc %s, user_id %i>'
                % (self.id, self.position, self.office_loc, self.user_id))


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
    term_id = db.Column(db.Integer, db.ForeignKey('term.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'start_time': self.start_time,
                'end_time': self.end_time,
                'days': self.days,
                'apntmnt_msg': self.apntmnt_msg,
                'user_id': self.user_id,
                'term_id': self.term_id}
        return json

    def __repr__(self):
        return ('<OfficeHours id %i, start_time %f, end_time %f, days %s,'
                ' apntmnt_msg %s, user_id %i, term_id %i>'
                % (self.id, self.start_time, self.end_time, self.days,
                    self.apntmnt_msg, self.user_id, self.term_id))


class Term(db.Model):
    __tablename__ = 'term'
    id = db.Column(db.Integer, primary_key=True)
    semester = db.Column(db.String(16))
    year = db.Column(db.Integer)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    office_hours = db.relationship('OfficeHours',
                                   backref=db.backref('term'))
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
        return ('<Term id %i, semester %s, year %i, start_date %i, end_date %i>'
                % (self.id, self.semester, self.year, self.start_date, self.end_date))


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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    educations = db.relationship('Education',
                                 backref=db.backref('faculty'))
    faculty_services = db.relationship('FacultyServices',
                                       backref=db.backref('faculty'))
    faculty_interests = db.relationship('FacultyInterests',
                                        backref=db.backref('faculty'))
    committee_members = db.relationship('CommitteeMembers',
                                        backref=db.backref('faculty'))
    course_sections = db.relationship('CourseSection',
                                      backref=db.backref('faculty'))
    textbooks = db.relationship('Textbook',
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
                'user_id': self.user_id}
        return json

    def __repr__(self):
        return ('<Faculty id %i, salutation %s, secondary_email %s, website_url %s,'
                ' faculty_type %s, faculty_rank %s, status %s, office_loc %s,'
                ' user_id %s>'
                % (self.id, self.salutation, self.secondary_email, self.website_url,
                    self.faculty_type, self.faculty_rank, self.status,
                    self.office_loc, self.user_id))


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
    title = db.Column(db.String(32))
    credits = db.Column(db.Integer)
    level = db.Column(db.String(16))
    description = db.Column(db.Text)
    prerequisites = db.Column(db.String(16))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    term_id = db.Column(db.Integer, db.ForeignKey('term.id'))
    courses = db.relationship('CourseSection', backref=db.backref('course'))

    def to_json_format(self):
        json = {'id': self.id,
                'department_id': self.department_id,
                'title': self.title,
                'credits': self.credits,
                'level': self.level,
                'description': self.description,
                'prerequisites': self.prerequisites,
                'term_id': self.term_id}
        return json

    def __repr__(self):
        return ('<Course id %i, department_id %i, title %s, credits %i, level %s,'
                ' description %s, prerequisites %s, term_id %i>'
                % (self.id, self.department_id, self.title, self.credits,
                    self.level, self.description, self.prerequisites, self.term_id))


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    courses = db.relationship('Course', backref=db.backref('department'))

    def to_json_format(self):
        json = {'id': self.id,
                'dept_name': self.dept_name}
        return json

    def __repr__(self):
        return ('<id %i, dept_name %s>'
                % (self.id, self.dept_name))


class Textbook(db.Model):
    __tablename__ = 'textbooks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    author = db.Column(db.String(32))
    edition = db.Column(db.String(8))
    publisher_id = db.Column(db.Integer)
    isbn = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    sections = db.relationship('CourseSection', backref=db.backref('textbook'))

    def to_json_format(self):
        json = {'id': self.id,
                'title': self.title,
                'author': self.author,
                'edition': self.edition,
                'publisher_id': self.publisher_id,
                'isbn': self.isbn,
                'author_id': self.author_id}
        return json

    def __repr__(self):
        return ('<id %i, title %s, author %s, edition %s,'
                ' publisher_id %i, isbn %i, author_id %i>'
                % (self.id, self.title, self.author, self.edition,
                    self.publisher_id, self.isbn, self.author_id))


class CourseTimes(db.Model):
    __tablename__ = 'course_times'
    id = db.Column(db.Integer, primary_key=True)
    days = db.Column(db.String(8))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    sections = db.relationship(
        'CourseSection', backref=db.backref('course_time'))

    def to_json_format(self):
        json = {'id': self.id,
                'days': self.days,
                'start_time': self.start_time,
                'end_time': self.end_time}
        return json

    def __repr__(self):
        return ('<id %i, days %s, start_time %f, end_time %f>'
                % (self.id, self.days, self.start_time, self.end_time))


class CourseSection(db.Model):
    __tablename__ = 'course_sections'
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(16))
    section_type = db.Column(db.String(32))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    textbook_id = db.Column(db.Integer, db.ForeignKey('textbooks.id'))
    course_time_id = db.Column(db.Integer, db.ForeignKey('course_times.id'))

    def to_json_format(self):
        json = {'id': self.id,
                'course_id': self.course_id,
                'faculty_id': self.faculty_id,
                'textbook_id': self.textbook_id,
                'course_time_id': self.course_time_id,
                'room': self.room,
                'section_type': self.section_type}
        return json

    def __repr__(self):
        return ('<id %i, course_id %i, faculty_id %i, textbook_id %i,'
                ' course_time_id %i, room %s, section_type %s>'
                % (self.id, self.course_id, self.faculty_id, self.textbook_id,
                    self.course_time_id, self.room, self.section_type))
