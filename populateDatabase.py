from app import db, models
i = models.Image(image_type='Colloquium', alt_text='This is an image',
				image_extension='png',)
s = models.Sideview(content='Hello world! This is a content', title='Hello World!',
					category='Colloquium', active=1, image=i)
db.session.add(i)
db.session.add(s)
db.session.commit()