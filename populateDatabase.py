from app import db, models
import datetime

i = models.Image(image_type='Colloquium', alt_text='This is an image',
				image_extension='png',)
s = models.Sideview(content='Hello world! This is a content', title='Hello World!',
					category='Colloquium', active=1, image=i)
n = models.News(headline='this is some news', intro='here is some content', image=i)

a = models.Alert(content='this is some content', user_id=1, location='villanova', category='alertCat', end_date=datetime.date(2016, 1, 1))

c = models.Course(course_id='CSC 2405', department_id=100, title='Computing Systems')

d = models.Department(dept_id=100, dept_name='Computer Science')

db.create_all()
#db.session.add(a)
#db.session.add(i)
#db.session.add(s)
#db.session.add(n)
#db.session.add(c)
#db.session.add(d)
db.session.commit()