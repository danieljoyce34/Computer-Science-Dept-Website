from app import db


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_type = db.Column(db.String(45), nullable=False)
    alt_text = db.Column(db.Text)
    image_extension = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return ('<Image id %i, image_type %s, alt_text %s, image_extension %s>'
                % (self.id, self.image_type, self.alt_text, self.image_extension))


class Sideview(db.Model):
    __tablename__ = 'sideviews'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(45), nullable=False)
    category = db.Column(db.String(45), nullable=False)
    active = db.Column(db.Integer, nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    image = db.relationship('Image', backref=db.backref('image', lazy='dynamic'),
                            uselist=False)

    def __repr__(self):
        return ('<Sideview id %i, content %s, title %s, active %i, image_id %i>'
                % (self.id, self.content, self.title, self.active, self.image_id))

class Alert(db.Model):
	__tablename__ = 'alerts'
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	content = db.Column(db.Text, nullable=True)
	user_id = db.Column(db.Integer, nullable=False)
	category = db.Column(db.String(45), nullable=True)
	post_date = db.Column(db.DateTime,nullable=False )
	location = db.Column(db.String(45), nullable=False)
	start_date = db.Column(db.DateTime, nullable=False)
	end_date = db.Column(db.DateTime, nullable=False)


	def __repr__(self):
		return ('<Alert id %i, content %s, user_id %i, category %s, post_date %f, location %s, start_date %f, end_date %f>'
				% (self.id, self.content, self.user_id, self.category, self.post_date, self.location, self.start_date, self.end_date))

