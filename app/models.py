from app import db

class Action(db.Model):
	__tablename__ = 'actions'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), index=True)
	controller_id = db.Column(db.Integer, index=True)

	def __repr__(self):
		return '<Action id %i, name %s, controller_id %i>' % (self.id, self.name, self.controller_id)