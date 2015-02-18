from app import db


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_type = db.Column(db.String(45))
    alt_text = db.Column(db.Text)
    image_extension = db.Column(db.String(45))

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
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    image = db.relationship('Image', backref=db.backref('image', lazy='dynamic'),
                            uselist=False)

    def __repr__(self):
        return ('<Sideview id %i, content %s, title %s, active %i, image_id %i>'
                % (self.id, self.content, self.title, self.active, self.image_id))


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    headline = db.Column(db.String(45))
    intro = db.Column(db.Text)
    article = db.Column(db.Text)
    post_date = db.Column(db.DateTime)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    #image = db.relationship('Image', backref=db.backref('image', lazy='dynamic'), uselist=False) #can't fix this error

    def __repr__(self):
        return ('<News id %i, start_date %f, end_date %f, headline %s, intro %s, article %s, post_date %f, image_id %i>'
                % (self.id, self.start_date, self.end_date, self.headline, self.intro, self.article, self.post_date, self.image_id))

class Alert(db.Model):
	__tablename__ = 'alerts'
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer)
	category = db.Column(db.String(45))
	post_date = db.Column(db.DateTime)
	location = db.Column(db.String(45))
	start_date = db.Column(db.DateTime)
	end_date = db.Column(db.DateTime)


	def __repr__(self):
		return ('<Alert id %i, content %s, user_id %i, category %s, post_date %f, location %s, start_date %f, end_date %f>'
				% (self.id, self.content, self.user_id, self.category, self.post_date, self.location, self.start_date, self.end_date))
