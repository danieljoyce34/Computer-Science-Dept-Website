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
    image = db.relationship('Image', backref=db.backref('sideviews', ),
                            uselist=False)

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
    image = db.relationship('Image', backref=db.backref('news',),
                            uselist=False)

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
        return ('<News id %i, start_date %f, end_date %f, headline %s, intro %s,'
                ' article %s, post_date %f, image_id %i>'
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
