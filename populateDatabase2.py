from app import db, models
import datetime

### USER ROLES ###
user_role_prof = models.UserRole(role='Faculty')
user_role_staff = models.UserRole(role='Staff')
user_role_grad = models.UserRole(role='Graduate')


### Committees ###
com1 = models.Committee(name='Academic Policy',
                               category='university',
                               description='Oversees the academic policies for the university')

com2 = models.Committee(name='Academic Standing',
                               category='college')

com3 = models.Committee(name='ACM Education Board',
                               category='professional',
                               description='Addresses educational concerns within the '
                               'Association for Computing Machinery.')

com4 = models.Committee(name='Annual Evaluation',
                               category='department',
                               description='Participates in the peer evaluation process '
                               'as defined by the College of Liberal Arts and Sciences.')

com5 = models.Committee(name='Assessment',
                               category='department',
                               description='Oversees the processes involved to assess '
                               'our effectiveness at accomplishing our departmental objectives.')

com6 = models.Committee(name='Bioinformatics Working Group',
                               category='college')

com7 = models.Committee(name='BIS IS Steering',
                               category='department',
                               description='Supports the program leading to the Bachelor '
                               'of Interdisciplinary Studies (BIS) degree with a concentration '
                               'in Information Systems (IS).')

com8 = models.Committee(name='Board of Academic Integrity',
                               category='university',
                               description='Adjudicates academic integrity cases.')

com9 = models.Committee(name='Board of Trustees Academic Affairs',
                               category='university')

com10 = models.Committee(name='BS in Comprehensive Science',
                               category='college',
                               description='Oversees the B.S. Comprehensive interdisciplinary program.')

com11 = models.Committee(name='BSCS Curriculum',
                               category='department',
                               description='Oversees the curriculum for the undergraduate program '
                               'leading to the Bachelor of Science degree in Computer Science.')

com12 = models.Committee(name='CEET Governance Board',
                               category='university')

com13 = models.Committee(name='Cognitive Science Program',
                               category='inter-department')

com14 = models.Committee(name='Committee on Faculty',
                               category='university')

com15 = models.Committee(name='Complaint',
                               category='department',
                               description='Addresses issues raised under the University '
                               'policy on complaints about faculty.')

com16 = models.Committee(name='Core Sub-Committee on Mathematics and Computing',
                               category='college',
                               description='A sub-committee of the college\'s Core '
                               'Curriculum committee, focused on how Math and CS are '
                               'incorporated into the core curriculum.')

com17 = models.Committee(name='CPE Curriculum',
                               category='inter-department',
                               description='Oversees the curriculum of the Computer '
                               'Engineering majors in the ECE department.')

com18 = models.Committee(name='Diversity',
                               category='department',
                               description='Explores issues related to ethnic diversity.')

com19 = models.Committee(name='Faculty Congress',
                               category='university')

com20 = models.Committee(name='Faculty Search',
                               category='department',
                               description='Oversees the process of finding suitable '
                                'candidates for new faculty positions.')

com21 = models.Committee(name='Information Competencies',
                               category='college')

com22 = models.Committee(name='Institutional Review Board',
                               category='university')

com23 = models.Committee(name='Majors and Concentrations',
                               category='college')

com24 = models.Committee(name='Mathematics for Computing',
                               category='department',
                               description='Investigates the role of mathematics in '
                               'computing, with the goal of tailoring the math requirements '
                               'of our students.')

com25 = models.Committee(name='Mendel Building',
                               category='college',
                               description='Addresses physical plant issues related to '
                               'Mendel Science Center.')

com26 = models.Committee(name='MSCS Curriculum',
                               category='department',
                               description='Oversees the curriculum for the graduate '
                               'program leading to the Master of Science degree in Computer Science.')

com27 = models.Committee(name='MSSE Curriculum',
                               category='department',
                               description='Oversees the curriculum for the graduate '
                               'program leading to a Masters of Science degree in Software Engineering.')

com28 = models.Committee(name='Non-Major Courses',
                               category='department',
                               description='Oversees the department\'s courses that '
                               'are designed for non-technical majors.')

com29 = models.Committee(name='Outcomes Assessment',
                               category='university')

com30 = models.Committee(name='Outreach',
                               category='department',
                               description='Investigates opportunities for the department '
                               'to increase its contributions and impact within the '
                               'Villanova community and the computing discipline at large.')

com31 = models.Committee(name='Policy Committee, National Science Digital Library',
                               category='professional')

com32 = models.Committee(name='Rank and Tenure',
                               category='college',
                               description='Evaluates rank and tenure cases at the college level.')

com33 = models.Committee(name='Sabbaticals and Reduced Loads in the Sciences',
                               category='college')

com34 = models.Committee(name='Scholarship',
                               category='department',
                               description='Promotes scholarship opportunities and '
                               'assesses candidates for local scholarship awards.')

com35 = models.Committee(name='Strategic Planning',
                               category='college',
                               description='Formulates and maintains the college\'s '
                               'strategic plan.')

com36 = models.Committee(name='Strategic Planning Focus Group',
                               category='college')

com37 = models.Committee(name='Task Force on Diversity and Recruitment',
                               category='college',
                               description='Formulates plans for college-wide recruitment, '
                               'with an emphasis on creating a diverse student body.')

com38 = models.Committee(name='Task Force on International Studies',
                               category='college')

com39 = models.Committee(name='Task Force on Science Education',
                               category='college')

com40 = models.Committee(name='Technology',
                               category='college',
                               description='Addresses any college-level technology issues.')

com41 = models.Committee(name='University Library',
                               category='university',
                               description='Addresses issues related to Falvey Library.')

com42 = models.Committee(name='University Senate',
                               category='university')

com43 = models.Committee(name='VICS Program Evaluation',
                               category='university',
                               description='Evaluates the success of the Villanova '
                               'Computing Scholars program.')

com44 = models.Committee(name='VICS Program Management',
                               category='department',
                               description='Oversees the Villanova Computing Scholars '
                               'program, including applicant evaluation.')



### FACULTY IMAGES ###
fac_images = []

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Joyce",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Beck",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Cassel",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Damian",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Fleischman",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Gehlot",
                          image_extension='png'))


### INSTANTIATE LISTS ###
users = []

user_phone = []

user_offhour = []

faculty = []

fac_edu = []

fac_com_mem = []

fac_int = []

fac_serv = []


### FACULTY ### 

# Dr. Joyce
users.append(models.User(fname='Daniel',
                   minit='T.',
                   lname='Joyce',
                   email='daniel.joyce@villanova.edu',
                   vu_ldap='djoyce',
                   image=fac_images[0],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-7344',
                             #extension='1234',
                             user=users[0]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[0]))

'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://webster.csc.villanova.edu:18088/~joyce/',
                         faculty_type='full time',
                         faculty_rank='Associate Professor',
                         status='Active',
                         office_loc='MSC 167-C',
                         user=users[0]))


edu_joyce = []

edu_joyce.append(models.Education(degree='Ph.D.',
                             discipline='Computer Science',
                             school='Temple University',
                             faculty=faculty[0]))

edu_joyce.append(models.Education(degree='M.A.',
                             discipline='Mathematics',
                             school='Villanova University',
                             faculty=faculty[0]))

edu_joyce.append(models.Education(degree='B.S.',
                             discipline='Mathematics',
                             school='University of Notre Dame',
                             faculty=faculty[0]))

fac_edu.append(edu_joyce)


fac_int_joyce = []

fac_int_joyce.append(models.FacultyInterests(interest='Software Engineering',
                                             faculty=faculty[0]))

fac_int_joyce.append(models.FacultyInterests(interest='Computer Security',
                                             faculty=faculty[0]))

fac_int_joyce.append(models.FacultyInterests(interest='Computer Science Education',
                                             faculty=faculty[0]))

fac_int.append(fac_int_joyce)


com_mem_joyce = []

com_mem_joyce.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[0],
                                             committee=com26))

com_mem_joyce.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[0],
                                             committee=com20))

com_mem_joyce.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[0],
                                             committee=com34))

fac_com_mem.append(com_mem_joyce)


fac_serv_joyce = []

fac_serv_joyce.append(models.FacultyServices(name='SIGCSE Vice Chair',
                                         category='professional',
                                         faculty=faculty[0]))

fac_serv_joyce.append(models.FacultyServices(name='Graduate Independent Study Coordinator',
                                         category='department',
                                         faculty=faculty[0]))

fac_serv_joyce.append(models.FacultyServices(name='Software Engineering Lab Coordinator',
                                         category='department',
                                         faculty=faculty[0]))

fac_serv_joyce.append(models.FacultyServices(name='Department Web Site Coordinator',
                                         category='department',
                                         faculty=faculty[0]))

fac_serv_joyce.append(models.FacultyServices(name='AP Computer Science Exam Reader',
                                         category='professional',
                                         faculty=faculty[0]))

fac_serv.append(fac_serv_joyce)

# Dr. Beck

users.append(models.User(fname='Robert',
                   minit='E.',
                   lname='Beck',
                   email='robert.beck@villanova.edu',
                   vu_ldap='rbeck',
                   image=fac_images[1],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-7352',
                             #extension='1234',
                             user=users[1]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[1]))
'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://www.csc.villanova.edu/~beck',
                         faculty_type='full time',
                         faculty_rank='Professor',
                         status='Active',
                         office_loc='MSC 292-A',
                         user=users[1]))

edu_beck = []

edu_beck.append(models.Education(degree='Ph.D.',
                             discipline='Mathematics',
                             school='University of Pennsylvania',
                             faculty=faculty[1]))

edu_beck.append(models.Education(degree='B.S.',
                             discipline='Mathematics',
                             school='Harvey Mudd College',
                             faculty=faculty[1]))

fac_edu.append(edu_beck)

fac_int_beck = []

fac_int_beck.append(models.FacultyInterests(interest='Human-Computer Interaction',
                                             faculty=faculty[1]))

fac_int_beck.append(models.FacultyInterests(interest='Biological Systems Modeling',
                                             faculty=faculty[1]))

fac_int_beck.append(models.FacultyInterests(interest='Computational Algebra',
                                             faculty=faculty[1]))

fac_int.append(fac_int_beck)

com_mem_beck = []

com_mem_beck.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[1],
                                             committee=com4))

com_mem_beck.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[1],
                                             committee=com20))

com_mem_beck.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[1],
                                             committee=com35))

com_mem_beck.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[1],
                                             committee=com40))

com_mem_beck.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[1],
                                             committee=com28))

com_mem_beck.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[1],
                                             committee=com7))

com_mem_beck.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[1],
                                             committee=com6))

com_mem_beck.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[1],
                                             committee=com13))

com_mem_beck.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[1],
                                             committee=com2))

com_mem_beck.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[1],
                                             committee=com12))

com_mem_beck.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[1],
                                             committee=com44))

com_mem_beck.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[1],
                                             committee=com43))

com_mem_beck.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[1],
                                             committee=com24))

com_mem_beck.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[1],
                                             committee=com34))

fac_com_mem.append(com_mem_beck)

fac_serv_beck = []

fac_serv_beck.append(models.FacultyServices(name='ABET CAC Team Chair',
                                         category='professional',
                                         faculty=faculty[1]))

fac_serv_beck.append(models.FacultyServices(name='SIGCSE Symposium Site Coordinator',
                                         category='professional',
                                         faculty=faculty[1]))

fac_serv_beck.append(models.FacultyServices(name='SIGCSE Disciplinary Societies Representative',
                                         category='professional',
                                         faculty=faculty[1]))

fac_serv_beck.append(models.FacultyServices(name='Undergraduate Independent Study Coordinator',
                                         category='department',
                                         faculty=faculty[1]))

fac_serv.append(fac_serv_beck)

# Dr. Cassel

# Dr. Damian

# Dr. Fleischman

# Dr. Gehlot




#### ADD TO DATABASE ####

#db.create_all()

### ADD USER ROLES ###
'''
db.session.add(user_role_prof)
db.session.add(user_role_grad)
db.session.add(user_role_staff)
'''

### ADD COMMITTEES ###
'''
for i in range(1,45):
  db.session.add(eval("com" + str(i)))
'''

### ADD FACULTY IMAGES ###
'''
for i in fac_images:
  db.session.add(i)
'''

### ADD USERS ###
'''
for i in users:
  db.session.add(i)
'''

### ADD USER PHONE NUMBERS ###
'''
for i in user_phone:
  db.session.add(i)
'''

### ADD USER OFFICE HOURS ###
'''
for i in user_offhour:
  db.session.add(i)
'''

### ADD FACULTY ###
'''
for i in faculty:
  db.session.add(i)
'''

### ADD FACULTY EDUCATIONS ###
'''
for i in fac_edu:
  for j in i:
    db.session.add(j)
'''

### ADD FACULTY INTERESTS ###
'''
for i in fac_int:
  for j in i:
    db.session.add(j)
'''

### ADD FACULTY COMMITTEE MEMBERSHIPS ###
'''
for i in fac_com_mem:
  for j in i:
    db.session.add(j)
'''

### ADD FACULTY SERVICES ###
'''
for i in fac_serv:
  for j in i:
    db.session.add(j)
'''


db.session.commit()