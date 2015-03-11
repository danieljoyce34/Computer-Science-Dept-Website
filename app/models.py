from app import db
import datetime
import util


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_type = db.Column(db.String(45))
    alt_text = db.Column(db.Text)
    image_extension = db.Column(db.String(45))
    sideviews_id = db.Column(db.Integer, db.ForeignKey('sideviews.id'))
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))

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
    title = db.Column(db.String(45))
    category = db.Column(db.String(45))
    active = db.Column(db.Integer)
    image = db.relationship('Image', backref=db.backref('sideviews', ), uselist=False)

    def to_json_format(self):
        json = {'id': self.id,
                'content': self.content,
                'title': self.title,
                'category': self.category,
                'active': self.active}
        return json

    def __repr__(self):
        return ('<Sideview id %i, content %s, title %s, active %i, image_id %i>'
                % (self.id, self.content, self.title, self.active, self.image_id))


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, default=datetime.date.today())
    end_date = db.Column(db.DateTime, default=util._next_month())
    headline = db.Column(db.String(45))
    intro = db.Column(db.Text)
    article = db.Column(db.Text)
    post_date = db.Column(db.DateTime, default=datetime.date.today())
    image = db.relationship('Image', backref=db.backref('news',), uselist=False)

    def to_json_format(self):
        json = {'id': self.id,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'headline': self.headline,
                'intro': self.intro,
                'article': self.article,
                'post_date': self.post_date}
        return json

    def __repr__(self):
        return ('<News id %i, start_date %f, end_date %f, headline %s, intro %s, article %s, post_date %f, image_id %i>'
                % (self.id, self.start_date, self.end_date, self.headline,
                    self.intro, self.article, self.post_date, self.image_id))


class Alert(db.Model):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer)
    category = db.Column(db.String(45))
    post_date = db.Column(db.DateTime, default=datetime.date.today())
    location = db.Column(db.String(45))
    start_date = db.Column(db.DateTime, default=datetime.date.today())
    end_date = db.Column(db.DateTime, default=util._next_month())


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
        return ('<Alert id %i, content %s, user_id %i, category %s, post_date %f, location %s, start_date %f, end_date %f>'
                % (self.id, self.content, self.user_id, self.category, self.post_date, self.location, self.start_date, self.end_date))

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(255))
    college_id = db.Column(db.Integer)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.dept_id'))
    title = db.Column(db.String(255))
    credits = db.Column(db.Integer)
    level = db.Column(db.String(255))
    description = db.Column(db.Text)
    format = db.Column(db.String(255))
    coordinator_id = db.Column(db.Integer)
    prerequisite_expression = db.Column(db.String(255))
    online_submission = db.Column(db.Boolean)
    note = db.Column(db.String(255))
    course_year = db.Column(db.Integer)

    def to_json_format(self):
        json = {'id': self.id,
                'course_id': self.course_id,
                'college_id': self.college_id,
                'department_id': self.department_id,
                'title': self.title,
                'credits': self.credits,
                'level': self.level,
                'description': self.description,
                'format': self.format,
                'coordinator_id': self.coordinator_id,
                'prerequisite_expression': self.prerequisite_expression,
                'online_submission': self.online_submission,
                'note': self.note,
                'course_year': self.course_year}
        return json

    def __repr__(self):
        return ('<Course id %i, course_id %s, college_id %i, department_id %i, title %s, credits %i, level %s, description %s, format %s, coordinator_id %i, prerequisite_expression %s, online_submission %i, note %s, course_year %i>'
                % (self.id, self.course_id, self.college_id, self.department_id, self.title, self.credits, self.level, self.description, self.format, self.coordinator_id, self.prerequisite_expression, self.online_submission, self.note, self.course_year))


class Department(db.Model):
    __tablename__ = 'departments'
    dept_id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(255))
    college_name = db.Column(db.String(255))


    def to_json_format(self):
        json = {'dept_id': self.dept_id,
                'dept_name': self.dept_name,
                'college_name': self.college_name}
        return json

    def __repr__(self):
        return ('<dept_id %s, dept_name %s, college_name %s>'
                % (self.dept_id, self.dept_name, self.college_name))


class Textbook(db.Model):
    __tablename__ = 'textbooks'
    text_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    edition = db.Column(db.String(255))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'))
    publisher_id = db.Column(db.Integer)
    isbn = db.Column(db.Integer)


    def to_json_format(self):
        json = {'text_id': self.text_id,
                'title': self.title,
                'author': self.author,
                'edition': self.edition, 
                'course_id': self.course_id, 
                'publisher_id': self.publisher_id, 
                'isbn': self.isbn}
        return json

    def __repr__(self):
        return ('<Textbook id %i, title %s, author %s, edition %s, course_id %i, publisher_id %i, isbn %i>'
                % (self.text_id, self.title, self.author, self.edition, self.course_id, self.publisher_id, self.isbn))


class Course_Section(db.Model):
    __tablename__ = 'course_sections'
    section_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'))
    instructor_id = db.Column(db.Integer)
    days = db.Column(db.String(255))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    room = db.Column(db.String(255))
    section_type = db.Column(db.String(255))


    def to_json_format(self):
        json = {'section_id': self.section_id,
                'course_id': self.course_id,
                'instructor_id': self.instructor_id,
                'days': self.days, 
                'start_time': self.start_time, 
                'end_time': self.end_time, 
                'room': self.room, 
                'section_type': self.section_type}
        return json

    def __repr__(self):
        return ('<section_id %i, course_id %i, instructor_id %i, days %s, start_time %f, end_time %f, room %s, section_type %s>'
                % (self.section_type, self.course_id, self.instructor_id, self.days, self.start_time, self.end_time, self.room, self.section_type))