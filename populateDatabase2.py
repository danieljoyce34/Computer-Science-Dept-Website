from app import db, models
import datetime

xj_image_icon = models.Image(image_type='icon',
                          alt_text="XJ's_awesome_selfie",
                          image_extension='png')

committee_1 = models.Committee(name='Technology',
                               category='department',
                               description='Address many department level '
                               'technology issues')

committee_2 = models.Committee(name='Technology',
                               category='university',
                               description='Address many university level '
                               'technology issues')

user_role_prof = models.UserRole(role='Faculty')
user_role_staff = models.UserRole(role='Staff')
user_role_grad = models.UserRole(role='Graduate')

## FACULTY ## 

# ***NEED IMAGES FOR FACULTY***
image_icon = models.Image(image_type='icon',
                          alt_text="XJ's_awesome_selfie",
                          image_extension='png')

prof = models.User(fname='Daniel',
                   minit='T.',
                   lname='Joyce',
                   email='daniel.joyce@villanova.edu',
                   vu_ldap='djoyce',
                   image=image_icon,
                   user_role=user_role_prof)

phone_1 = models.PhoneNumber(area_code='(215)',
                             number='777-7777',
                             extension='1234',
                             user=prof)

address_1 = models.Address(line1='123 Sesame St.',
                           city='Villanova',
                           state='PA',
                           zip=11111,
                           user=prof)

office_hour = models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=prof)

faculty = models.Faculty(salutation='Dr.',
                         secondary_email='joyce@fakemail.com',
                         website_url='http://webster.csc.villanova.edu:18088/~joyce/',
                         faculty_type='full time',
                         faculty_rank='Professor',
                         status='Active',
                         office_loc='MSC-161C',
                         user=prof)

education = models.Education(degree='Ph.D.',
                             discipline='Mathematics',
                             school='National Taiwan University',
                             faculty=faculty)

faculty_service = models.FacultyServices(name='Programming Team Coach',
                                         category='department',
                                         faculty=faculty)

faculty_interest_1 = models.FacultyInterests(interest='Software Engineering',
                                             faculty=faculty)

faculty_interest_2 = models.FacultyInterests(interest='Algorithm',
                                             faculty=faculty)

committee_member_1 = models.CommitteeMembers(role='Chair',
                                             faculty=faculty,
                                             committee=committee_1)

committee_member_2 = models.CommitteeMembers(faculty=faculty,
                                             committee=committee_2)

#db.create_all()
db.session.add(xj_image_icon)
db.session.add(committee_1)
db.session.add(committee_2)
db.session.add(user_role_prof)
db.session.add(user_role_grad)
db.session.add(user_role_staff)

db.session.add(image_icon)
db.session.add(prof)
db.session.add(phone_1)
db.session.add(address_1)
#db.session.add(office_hour)
db.session.add(faculty)
db.session.add(education)
db.session.add(faculty_service)
db.session.add(faculty_interest_1)
db.session.add(faculty_interest_2)
db.session.add(committee_member_1)
db.session.add(committee_member_2)

db.session.commit()