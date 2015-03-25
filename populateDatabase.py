from app import db, models
import datetime

image_icon = models.Image(image_type='icon',
                          alt_text="XJ's_awesome_selfie",
                          image_extension='png')

sideview = models.Sideview(
    content="There are many frameworks available for iOS 2D game development such"
    " as Unity, Corona, SpriteKit, Cocos2D etc... Many people are turned off from"
    " learning these frameworks because they seem really complicated. The purpose"
    " of my project to create a couple iOS 2D games using Cocos2D and SpriteKit"
    " and perform a comparison of these two frameworks. The reason for a comparison"
    " between Cocos2D and SpriteKit is that most game on the App Store are created"
    " using Cocos2D, and on the other hand, SpriteKit is Apple's 2D game development"
    " framework that was based off Cocos2D. It would be interesting to see the pros"
    " and cons of each framework side by side. For my first iOS game - Drop Blocks!"
    " visit this link: https://bitly.com/a/bitlinks - I used Cocos2D, it is a very"
    " simple game where blocks will move back and forth on the top of the screen"
    " and the user will tap the screen to drop the blocks. The user will be able"
    " to gain points and erase blocks if the blocks are matched with 3 or more same"
    " color blocks horizontally or vertically.",
    title='2D Game Development',
    category='Senior Project',
    active=1,
    image=image_icon)

news = models.News(headline='Congratulations 2014 UPE Inductees!',
                   intro='On Friday, April 4 2014, eleven graduate students and'
                   ' four undergraduate students have been inducted into Upsilon'
                   ' Pi Epsilon, the International Honor Society for Computing'
                   ' and Information Sciences.',
                   article='On Friday, April 4 2014, eleven graduate students and'
                   ' four undergraduate students have been inducted into Upsilon'
                   ' Pi Epsilon, the International Honor Society for Computing'
                   ' and Information Sciences.',
                   image=image_icon)

user_role_prof = models.UserRole(role='Faculty')
user_role_staff = models.UserRole(role='Staff')
user_role_grad = models.UserRole(role='Graduate')

prof = models.User(fname='Daniel',
                   minit='T.',
                   lname='Joyce',
                   email='daniel.joyce@villanova.edu',
                   vu_ldap='djoyce',
                   image=image_icon,
                   user_role=user_role_prof)

user_staff = models.User(fname='Daniel_Staff',
                         minit='T.',
                         lname='Joyce',
                         email='daniel.joyce@villanova.edu',
                         vu_ldap='djoyce',
                         image=image_icon,
                         user_role=user_role_staff)

user_graduate = models.User(fname='Peter',
                            minit='T.',
                            lname='R',
                            email='peter.r@villanova.edu',
                            vu_ldap='pr',
                            image=image_icon,
                            user_role=user_role_grad)

alert_1 = models.Alert(content='Software Engineering cancelled this week',
                       category='Class',
                       location='MSC-168',
                       user=prof)

alert_2 = models.Alert(content='Colloquium this Monday',
                       category='Colloquium',
                       location='MSC-168',
                       user=prof)

alert_3 = models.Alert(content='Senior Project cancelled this week',
                       category='Class',
                       location='MSC-168',
                       user=prof)

alert_4 = models.Alert(content='Colloquium this Tuesday',
                       category='Colloquium',
                       location='MSC-168',
                       user=prof)

alert_5 = models.Alert(content='Programming team meeting cancelled this week',
                       category='Class',
                       location='MSC-168',
                       user=prof)

alert_6 = models.Alert(content='Colloquium this Thursday',
                       category='Colloquium',
                       location='MSC-168',
                       user=prof)

staff = models.Staff(position='PC LAND Administrator',
                     office_loc='MSC-161',
                     user=user_staff)

administration = models.Administration(description='Webmaster of the CS Dept',
                                       priority='None',
                                       user=prof)

phone_1 = models.PhoneNumber(area_code='(215)',
                             number='777-7777',
                             extension='1234',
                             user=prof)

phone_2 = models.PhoneNumber(area_code='(215)',
                             number='777-7777',
                             extension='1234',
                             user=user_staff)

phone_3 = models.PhoneNumber(area_code='(215)',
                             number='777-7777',
                             extension='1234',
                             user=user_graduate)

address_1 = models.Address(line1='123 Sesame St.',
                           city='Villanova',
                           state='PA',
                           zip=11111,
                           user=prof)

address_2 = models.Address(line1='123 North St.',
                           city='Villanova',
                           state='PA',
                           zip=11111,
                           user=user_staff)

address_3 = models.Address(line1='123 North St.',
                           city='Villanova',
                           state='PA',
                           zip=11111,
                           user=user_graduate)

term_fall = models.Term(semester='Fall',
                        year=2014,
                        start_date=datetime.date(2014, 8, 23),
                        end_date=datetime.date(2020, 12, 21))

office_hour = models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                end_time=datetime.datetime(2014, 9, 1, 14),
                                apntmnt_msg='email beforehand',
                                days='MWF',
                                user=prof,
                                term=term_fall)

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

committee_1 = models.Committee(name='Technology',
                               category='department',
                               description='Address many department level '
                               'technology issues')

committee_2 = models.Committee(name='Technology',
                               category='university',
                               description='Address many university level '
                               'technology issues')

committee_member_1 = models.CommitteeMembers(role='Chair',
                                             faculty=faculty,
                                             committee=committee_1)

committee_member_2 = models.CommitteeMembers(faculty=faculty,
                                             committee=committee_2)

dept = models.Department(name='Computing Sciences')

course_1 = models.Course(title='Software Engineering',
                         credits=3,
                         level='UG',
                         description='See website',
                         prerequisites='None',
                         term=term_fall,
                         department=dept)

course_sect_1 = models.CourseSection(course_time_id='1',
                                     room='MSC-168',
                                     section_type='Lecture',
                                     course=course_1,
                                     faculty=faculty)

course_sect_2 = models.CourseSection(course_time_id='2',
                                     room='MSC-168',
                                     section_type='Lecture',
                                     course=course_1,
                                     faculty=faculty)

course_time_1 = models.CourseTimes(days='MWF',
                                   start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                   end_time=datetime.datetime(2014, 9, 1, 14))

course_time_2 = models.CourseTimes(days='TTR',
                                   start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                   end_time=datetime.datetime(2014, 9, 1, 14))

#db.create_all()
db.session.add(image_icon)
db.session.add(sideview)
db.session.add(news)
db.session.add(user_role_prof)
db.session.add(user_role_grad)
db.session.add(user_role_staff)
db.session.add(prof)
db.session.add(user_staff)
db.session.add(user_graduate)
db.session.add(alert_1)
db.session.add(alert_2)
db.session.add(alert_3)
db.session.add(alert_4)
db.session.add(alert_5)
db.session.add(alert_6)
db.session.add(staff)
db.session.add(administration)
db.session.add(phone_3)
db.session.add(phone_2)
db.session.add(phone_1)
db.session.add(address_3)
db.session.add(address_2)
db.session.add(address_1)
db.session.add(term_fall)
db.session.add(office_hour)
db.session.add(faculty)
db.session.add(education)
db.session.add(faculty_service)
db.session.add(faculty_interest_1)
db.session.add(faculty_interest_2)
db.session.add(committee_1)
db.session.add(committee_2)
db.session.add(committee_member_1)
db.session.add(committee_member_2)
db.session.add(dept)
db.session.add(course_1)
db.session.add(course_sect_1)
db.session.add(course_sect_2)
db.session.add(course_time_1)
db.session.add(course_time_2)
db.session.commit()
