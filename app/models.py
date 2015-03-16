from app import db
import datetime
import util


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_type = db.Column(db.String(64))
    alt_text = db.Column(db.Text)
    image_extension = db.Column(db.String(64))
    sideview = db.relationship('Sideview', backref=db.backref('image', ),
                               uselist=False)
    news = db.relationship('News', backref=db.backref('image',),
                           uselist=False)
    # user object here

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
                'image_id': self.image}
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
    user_id = db.Column(db.Integer)
    category = db.Column(db.String(64))
    post_date = db.Column(db.DateTime, default=datetime.date.today())
    location = db.Column(db.String(64))
    start_date = db.Column(db.DateTime, default=datetime.date.today())
    end_date = db.Column(db.DateTime, default=util._next_month())

    def to_json_format(self):
        json = {'id': self.id,
                'content': self.id,
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
    minit = db.Column(db.String(1))
    lname = db.Column(db.String(32))
    email = db.Column(db.String(64))
    vu_ldap = db.Column(db.String(64))
    # image_id foreign key here
    # user_role_id foreign key here
    # staff object here
    # administration object here
    # phoneNumber object here
    # address object here
    # officeHours object here
    # Faculty object here

    # to_json_format
    # repr function


class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(32))
    # user object here

    # to_json_format
    # repr function


class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(64))
    office_loc = db.Column(db.String(64))
    # user_id foreign key here

    # to_json_format
    # repr function


class Administration(db.Model):
    __tablename__ = 'administration'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128))
    priority = db.Column(db.String(64))
    # user_id foreign key here

    # to_json_format
    # repr function


class PhoneNumber(db.Model):
    __tablename__ = 'phone_number'
    id = db.Column(db.Integer, primary_key=True)
    area_code = db.Column(db.String(8))
    number = db.Column(db.String(8))
    extension = db.Column(db.String(8))
    # user_id foreign key here

    # to_json_format
    # repr function


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    line1 = db.Column(db.String(32))
    line2 = db.Column(db.String(32))
    city = db.Column(db.String(32))
    state = db.Column(db.String(32))
    zip = db.Column(db.Integer)
    # user_id foreign key here

    # to_json_format
    # repr function


class OfficeHours(db.Model):
    # TODO: Add util functionality to retrieve time from a DateTime object
    __tablename__ = 'office_hours'
    id = db.Column(db.Integer, primary_key=True)
    # using DateTime object since that's the only Flask SQLAlchemy datatype that
    # deals with time
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    days = db.Column(db.String(5))
    apntmnt_msg = db.Column(db.String(128))
    # user_id foreign key here
    # term_id foreign key here

    # to_json_format
    # repr function


class term(db.Model):
    __tablename__ = 'term'
    id = db.Column(db.Integer, primary_key=True)
    semester = db.Column(db.String(16))
    year = db.Column(db.Integer)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    # officeHours object here

    # to_json_format
    # repr function


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
    # user_id foreign key here
    # education object here
    # facultyServices object here
    # facultyInterests object here
    # committeeMembers object here

    # to_json_format
    # repr function


class Education(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(64))
    discipline = db.Column(db.String(128))
    school = db.Column(db.String(128))
    # faculty_id foreign key here

    # to_json_format
    # repr function


class FacultyServices(db.Model):
    __tablename__ = 'faculty_services'
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(64))
    category = db.Column(db.String(64))
    # faculty_id foreign key here

    # to_json_format
    # repr function


class FacultyInterests(db.Model):
    __tablename__ = 'faculty_interests'
    id = db.Column(db.Integer, primary_key=True)
    interest = db.Column(db.String(64))
    # faculty_id foreign key here

    # to_json_format
    # repr function


class committee_members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(64))
    # faculty_id foreign key here
    # committee_id foreign key here

    # to_json_format
    # repr function


class committee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    category = db.Column(db.String(64))
    description = db.Column(db.Text)
    # committeeMembers object here

    # to_json_format
    # repr function
