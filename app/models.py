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
	__tablename = 'sideviews'
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
