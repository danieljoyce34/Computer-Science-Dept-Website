from app import db, models
import datetime

### USER ROLES ###
user_role_prof = models.UserRole(role='Faculty')
user_role_staff = models.UserRole(role='Staff')
user_role_grad = models.UserRole(role='Graduate')
user_role_ugrad = models.UserRole(role='Undergrad')
user_role_web = models.UserRole(role='Webteam')


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

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Goelman",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Mrs. Helwig",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Japaridze",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Kim",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Klassner",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Levitin",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Papalaskari",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Soong",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Dr. Way",
                          image_extension='png'))

fac_images.append(models.Image(image_type='icon',
                          alt_text="Ms. Zimmerman",
                          image_extension='png'))

### STAFF IMAGES ###

staff_images = []

staff_images.append(models.Image(image_type='icon',
                          alt_text="Adele Ballard",
                          image_extension='png'))

staff_images.append(models.Image(image_type='icon',
                          alt_text="Joe Dalbo",
                          image_extension='png'))

staff_images.append(models.Image(image_type='icon',
                          alt_text="Anne Hischar",
                          image_extension='png'))

staff_images.append(models.Image(image_type='icon',
                          alt_text="Najib Nadi",
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

staff = []

### FACULTY ### 

# Dr. Joyce (User 0)

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

# Dr. Beck (User 1)

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

# Dr. Cassel (User 2)

users.append(models.User(fname='Lillian', 
                   lname='Cassel',
                   email='lillian.cassel@villanova.edu',
                   vu_ldap='lcassel',
                   image=fac_images[2],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-7341',
                             #extension='1234',
                             user=users[2]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[2]))
'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://what.csc.villanova.edu/~cassel',
                         faculty_type='full time',
                         faculty_rank='Professor and Chair',
                         status='Active',
                         office_loc='MSC 161-A',
                         user=users[2]))

edu_cassel = []

edu_cassel.append(models.Education(degree='Ph.D.',
                             discipline='Computer Science',
                             school='University of Delaware',
                             faculty=faculty[2]))

edu_cassel.append(models.Education(degree='M.S.',
                             discipline='Computer Science',
                             school='University of Delaware',
                             faculty=faculty[2]))

fac_edu.append(edu_cassel)

fac_int_cassel = []

fac_int_cassel.append(models.FacultyInterests(interest='Networks',
                                             faculty=faculty[2]))

fac_int_cassel.append(models.FacultyInterests(interest='Information Retrieval',
                                             faculty=faculty[2]))

fac_int_cassel.append(models.FacultyInterests(interest='Digital Libraries',
                                             faculty=faculty[2]))

fac_int_cassel.append(models.FacultyInterests(interest='Image Management',
                                             faculty=faculty[2]))

fac_int.append(fac_int_cassel)

com_mem_cassel = []

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com16))

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com32))

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com41))

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com3))

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com7))

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com19))

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com42))

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com29))

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com6))

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com9))

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com31))

com_mem_cassel.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[2],
                                             committee=com24))

fac_com_mem.append(com_mem_cassel)

fac_serv_cassel = []

fac_serv_cassel.append(models.FacultyServices(name='ABET CAC Team Chair',
                                         category='professional',
                                         faculty=faculty[2]))

fac_serv_cassel.append(models.FacultyServices(name='Advising: Internships',
                                         category='department',
                                         faculty=faculty[2]))

fac_serv_cassel.append(models.FacultyServices(name='Department Chair',
                                         category='department',
                                         faculty=faculty[2]))

fac_serv_cassel.append(models.FacultyServices(name='Digital Library Lab Coordinator',
                                         category='department',
                                         faculty=faculty[2]))

fac_serv.append(fac_serv_cassel)

# Dr. Damian (User 3)

users.append(models.User(fname='Mirela',
                   lname='Damian',
                   email='mirela.damian@villanova.edu',
                   vu_ldap='mdamiani',
                   image=fac_images[3],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-7414',
                             #extension='1234',
                             user=users[3]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[3]))
'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://www.csc.villanova.edu/~mdamian',
                         faculty_type='full time',
                         faculty_rank='Professor',
                         status='Active',
                         office_loc='MSC 167-A',
                         user=users[3]))

edu_damian = []

edu_damian.append(models.Education(degree='Ph.D.',
                             discipline='Computer Science',
                             school='University of Iowa',
                             faculty=faculty[3]))

edu_damian.append(models.Education(degree='M.S.',
                             discipline='Computer Science',
                             school='University of Iowa',
                             faculty=faculty[3]))

edu_damian.append(models.Education(degree='M.S.',
                             discipline='Electrical and Computer Engineering',
                             school='University Politechnica of Bucharest',
                             faculty=faculty[3]))

fac_edu.append(edu_damian)

fac_int_damian = []

fac_int_damian.append(models.FacultyInterests(interest='Computational Geometry',
                                             faculty=faculty[3]))

fac_int_damian.append(models.FacultyInterests(interest='Graph Theory',
                                             faculty=faculty[3]))

fac_int_damian.append(models.FacultyInterests(interest='Wireless Networks',
                                             faculty=faculty[3]))

fac_int.append(fac_int_damian)

com_mem_damian = []

com_mem_damian.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[3],
                                             committee=com5))

com_mem_damian.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[3],
                                             committee=com11))

com_mem_damian.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[3],
                                             committee=com18))

com_mem_damian.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[3],
                                             committee=com20))

com_mem_damian.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[3],
                                             committee=com34))

fac_com_mem.append(com_mem_damian)

fac_serv_damian = []

fac_serv_damian.append(models.FacultyServices(name='Advising: Class of 2016',
                                         category='department',
                                         faculty=faculty[3]))

fac_serv_damian.append(models.FacultyServices(name='UPE Student Chapter Advisor',
                                         category='department',
                                         faculty=faculty[3]))

fac_serv_damian.append(models.FacultyServices(name='Networks Lab Coordinator',
                                         category='department',
                                         faculty=faculty[3]))

fac_serv.append(fac_serv_damian)

# Dr. Fleischman (User 4)

users.append(models.User(fname='William',
                   minit='M.',
                   lname='Fleischman',
                   email='william.fleischman@villanova.edu',
                   vu_ldap='wfleisch',
                   image=fac_images[4],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-4819',
                             #extension='1234',
                             user=users[4]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[4]))

'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://www.csc.villanova.edu/~fleischm',
                         faculty_type='full time',
                         faculty_rank='Professor',
                         status='Active',
                         office_loc='MSC 167-B',
                         user=users[4]))


edu_fleischman = []

edu_fleischman.append(models.Education(degree='Ph.D.',
                             discipline='Mathematics',
                             school='Lehigh University',
                             faculty=faculty[4]))

fac_edu.append(edu_fleischman)


fac_int_fleischman = []

fac_int_fleischman.append(models.FacultyInterests(interest='Biological Systems Modeling',
                                             faculty=faculty[4]))

fac_int_fleischman.append(models.FacultyInterests(interest='Parallel Computing',
                                             faculty=faculty[4]))

fac_int.append(fac_int_fleischman)


com_mem_fleischman = []

com_mem_fleischman.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[4],
                                             committee=com18))

com_mem_fleischman.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[4],
                                             committee=com24))

com_mem_fleischman.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[4],
                                             committee=com27))

com_mem_fleischman.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[4],
                                             committee=com30))

com_mem_fleischman.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[4],
                                             committee=com10))

com_mem_fleischman.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[4],
                                             committee=com22))

fac_com_mem.append(com_mem_fleischman)


fac_serv_fleischman = []

fac_serv_fleischman.append(models.FacultyServices(name='Advising: Class of 2017',
                                         category='department',
                                         faculty=faculty[4]))

fac_serv.append(fac_serv_fleischman)

# Dr. Gehlot (User 5)

users.append(models.User(fname='Vijay',
                   lname='Gehlot',
                   email='vijay.gehlot@villanova.edu',
                   vu_ldap='vgehlot',
                   image=fac_images[5],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-5843',
                             #extension='1234',
                             user=users[5]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[5]))

'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://www.csc.villanova.edu/~gehlot',
                         faculty_type='full time',
                         faculty_rank='Associate Professor',
                         status='Active',
                         office_loc='MSC 161-B',
                         user=users[5]))


edu_gehlot = []

edu_gehlot.append(models.Education(degree='Ph.D.',
                             discipline='Computer and Information Science',
                             school='University of Pennsylvania',
                             faculty=faculty[5]))

edu_gehlot.append(models.Education(degree='M.E.',
                             discipline='Automation',
                             school='Indian Institute of Science',
                             faculty=faculty[5]))

edu_gehlot.append(models.Education(degree='B.E.',
                             discipline='Electrical and Electronics Engineering',
                             school='Birla Institute of Technology and Science',
                             faculty=faculty[5]))

fac_edu.append(edu_gehlot)


fac_int_gehlot = []

fac_int_gehlot.append(models.FacultyInterests(interest='Programming Languages',
                                             faculty=faculty[5]))

fac_int_gehlot.append(models.FacultyInterests(interest='Compilation Techniques',
                                             faculty=faculty[5]))

fac_int_gehlot.append(models.FacultyInterests(interest='Systems Modeling and Analysis',
                                             faculty=faculty[5]))

fac_int_gehlot.append(models.FacultyInterests(interest='Petri Nets',
                                             faculty=faculty[5]))

fac_int_gehlot.append(models.FacultyInterests(interest='Formal Methods',
                                             faculty=faculty[5]))

fac_int.append(fac_int_gehlot)


com_mem_gehlot = []

com_mem_gehlot.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[5],
                                             committee=com26))

com_mem_gehlot.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[5],
                                             committee=com5))

com_mem_gehlot.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[5],
                                             committee=com17))

com_mem_gehlot.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[5],
                                             committee=com27))

fac_com_mem.append(com_mem_gehlot)


fac_serv_gehlot = []

fac_serv_gehlot.append(models.FacultyServices(name='Advising: Graduate Students',
                                         category='department',
                                         faculty=faculty[5]))

fac_serv_gehlot.append(models.FacultyServices(name='Graduate Program Director',
                                         category='department',
                                         faculty=faculty[5]))

fac_serv.append(fac_serv_gehlot)

# Dr. Goelman (User 6)

users.append(models.User(fname='Don',
                   lname='Goelman',
                   email='don.goelman@villanova.edu',
                   vu_ldap='dgoelman',
                   image=fac_images[6],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-7346',
                             #extension='1234',
                             user=users[6]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[6]))

'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://www.csc.villanova.edu/~goelman',
                         faculty_type='full time',
                         faculty_rank='Associate Professor',
                         status='Active',
                         office_loc='MSC 162-A',
                         user=users[6]))


edu_goelman = []

edu_goelman.append(models.Education(degree='Ph.D.',
                             discipline='Mathematics',
                             school='University of Pennsylvania',
                             faculty=faculty[6]))

edu_goelman.append(models.Education(degree='B.A.',
                             discipline='Mathematics',
                             school='University of Pennsylvania',
                             faculty=faculty[6]))

fac_edu.append(edu_goelman)


fac_int_goelman = []

fac_int_goelman.append(models.FacultyInterests(interest='Database Systems',
                                             faculty=faculty[6]))

fac_int_goelman.append(models.FacultyInterests(interest='Algorithms',
                                             faculty=faculty[6]))

fac_int_goelman.append(models.FacultyInterests(interest='Data Modeling',
                                             faculty=faculty[6]))

fac_int.append(fac_int_goelman)


com_mem_goelman = []

com_mem_goelman.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[6],
                                             committee=com26))

com_mem_goelman.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[6],
                                             committee=com33))

fac_com_mem.append(com_mem_goelman)


fac_serv_goelman = []

fac_serv_goelman.append(models.FacultyServices(name='Advising: Class of 2015',
                                         category='department',
                                         faculty=faculty[6]))

fac_serv_goelman.append(models.FacultyServices(name='Colloquia Coordinator',
                                         category='department',
                                         faculty=faculty[6]))

fac_serv_goelman.append(models.FacultyServices(name='Integrated BS/MS Program Coordinator',
                                         category='department',
                                         faculty=faculty[6]))

fac_serv_goelman.append(models.FacultyServices(name='CCSC-NE 2009 Co-Chair',
                                         category='professional',
                                         faculty=faculty[6]))

fac_serv.append(fac_serv_goelman)

# Mrs. Helwig (User 7)

users.append(models.User(fname='Catherine',
                   minit='L.',
                   lname='Helwig',
                   email='catherine.helwig@villanova.edu',
                   vu_ldap='chelwig',
                   image=fac_images[7],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-5412',
                             #extension='1234',
                             user=users[7]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[7]))

'''

faculty.append(models.Faculty(salutation='Mrs.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://www.csc.villanova.edu/~helwig',
                         faculty_type='full time',
                         faculty_rank='Instructor',
                         status='Active',
                         office_loc='MSC 292-B',
                         user=users[7]))


edu_helwig = []

edu_helwig.append(models.Education(degree='M.S.',
                             discipline='Computer Science',
                             school='Villanova University',
                             faculty=faculty[7]))

edu_helwig.append(models.Education(degree='B.A.',
                             discipline='History, Philosophy',
                             school='Chestnut Hill College',
                             faculty=faculty[7]))

fac_edu.append(edu_helwig)


fac_int_helwig = []

fac_int_helwig.append(models.FacultyInterests(interest='Algorithms',
                                             faculty=faculty[7]))

fac_int_helwig.append(models.FacultyInterests(interest='Object-Oriented Software',
                                             faculty=faculty[7]))

fac_int_helwig.append(models.FacultyInterests(interest='Data Structures',
                                             faculty=faculty[7]))

fac_int.append(fac_int_helwig)


com_mem_helwig = []

com_mem_helwig.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[7],
                                             committee=com11))

com_mem_helwig.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[7],
                                             committee=com28))

com_mem_helwig.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[7],
                                             committee=com30))

fac_com_mem.append(com_mem_helwig)


fac_serv_helwig = []

fac_serv_helwig.append(models.FacultyServices(name='Advising: Class of 2015',
                                         category='department',
                                         faculty=faculty[7]))

fac_serv.append(fac_serv_helwig)

# Dr. Japaridze (User 8)

users.append(models.User(fname='Giorgi',
                   lname='Japaridze',
                   email='giorgi.japaridze@villanova.edu',
                   vu_ldap='gjaparid',
                   image=fac_images[8],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-7332',
                             #extension='1234',
                             user=users[8]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[8]))

'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://www.csc.villanova.edu/~japaridz',
                         faculty_type='full time',
                         faculty_rank='Professor',
                         status='Active',
                         office_loc='MSC 165-A',
                         user=users[8]))


edu_japaridze = []

edu_japaridze.append(models.Education(degree='Ph.D.',
                             discipline='Computer Science',
                             school='University of Pennsylvania',
                             faculty=faculty[8]))

edu_japaridze.append(models.Education(degree='Ph.D.',
                             discipline='Mathematical Logic',
                             school='Moscow State University',
                             faculty=faculty[8]))

edu_japaridze.append(models.Education(degree='M.S.',
                             discipline='Philosophy',
                             school='Tbilisi State University',
                             faculty=faculty[8]))

fac_edu.append(edu_japaridze)


fac_int_japaridze = []

fac_int_japaridze.append(models.FacultyInterests(interest='Computational Theory',
                                             faculty=faculty[8]))

fac_int_japaridze.append(models.FacultyInterests(interest='Artificial Intelligence',
                                             faculty=faculty[8]))

fac_int_japaridze.append(models.FacultyInterests(interest='Logic',
                                             faculty=faculty[8]))

fac_int.append(fac_int_japaridze)


com_mem_japaridze = []

com_mem_japaridze.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[8],
                                             committee=com15))

com_mem_japaridze.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[8],
                                             committee=com18))

com_mem_japaridze.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[8],
                                             committee=com26))

fac_com_mem.append(com_mem_japaridze)


fac_serv_japaridze = []

fac_serv_japaridze.append(models.FacultyServices(name='Advising: Part Time Students',
                                         category='department',
                                         faculty=faculty[8]))

fac_serv_japaridze.append(models.FacultyServices(name='Library Acquisitions',
                                         category='department',
                                         faculty=faculty[8]))

fac_serv.append(fac_serv_japaridze)

# Dr. Kim (User 9)

users.append(models.User(fname='Edward',
                   lname='Kim',
                   email='edward.kim@villanova.edu',
                   vu_ldap='ekim07',
                   image=fac_images[9],
                   user_role=user_role_prof))

faculty.append(models.Faculty(salutation='Dr.',
                         faculty_type='full time',
                         faculty_rank='Assistant Professor',
                         status='Active',
                         office_loc='MSC 165-B',
                         user=users[9]))

'''
***Dr. Kim's information is missing***

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-7344',
                             #extension='1234',
                             user=users[9]))


user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[9]))

edu_kim = []

fac_edu.append(edu_kim)


fac_int_kim = []

fac_int.append(fac_int_kim)


com_mem_kim = []

fac_com_mem.append(com_mem_kim)


fac_serv_kim = []

fac_serv.append(fac_serv_kim)
'''

# Dr. Klassner (User 10)

users.append(models.User(fname='Frank',
                   minit='I.',
                   lname='Klassner',
                   email='frank.klassner@villanova.edu',
                   vu_ldap='fklassne',
                   image=fac_images[10],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-5671',
                             #extension='1234',
                             user=users[10]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[10]))

'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://www.csc.villanova.edu/~klassner',
                         faculty_type='full time',
                         faculty_rank='Associate Professor',
                         status='Active',
                         office_loc='MSC 160-C',
                         user=users[10]))


edu_klassner = []

edu_klassner.append(models.Education(degree='Ph.D.',
                             discipline='Computer Science',
                             school='University of Massachusetts',
                             faculty=faculty[10]))

edu_klassner.append(models.Education(degree='M.S.',
                             discipline='Computer Science',
                             school='University of Massachusetts',
                             faculty=faculty[10]))

edu_klassner.append(models.Education(degree='B.S.',
                             discipline='Computer Science',
                             school='University of Scranton',
                             faculty=faculty[10]))

edu_klassner.append(models.Education(degree='B.S.',
                             discipline='Electronics Engineering',
                             school='University of Scranton',
                             faculty=faculty[10]))

fac_edu.append(edu_klassner)


fac_int_klassner = []

fac_int_klassner.append(models.FacultyInterests(interest='Web-Based Software Systems',
                                             faculty=faculty[10]))

fac_int_klassner.append(models.FacultyInterests(interest='Artificial Intelligence',
                                             faculty=faculty[10]))

fac_int_klassner.append(models.FacultyInterests(interest='Signal Processing',
                                             faculty=faculty[10]))

fac_int.append(fac_int_klassner)


com_mem_klassner = []

com_mem_klassner.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[10],
                                             committee=com12))

com_mem_klassner.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[10],
                                             committee=com20))

com_mem_klassner.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[10],
                                             committee=com44))

com_mem_klassner.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[10],
                                             committee=com30))

com_mem_klassner.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[10],
                                             committee=com34))

fac_com_mem.append(com_mem_klassner)


fac_serv_klassner = []

fac_serv_klassner.append(models.FacultyServices(name='Advising: Class of 2016',
                                         category='department',
                                         faculty=faculty[10]))

fac_serv_klassner.append(models.FacultyServices(name='Programming Team Coach',
                                         category='department',
                                         faculty=faculty[10]))

fac_serv_klassner.append(models.FacultyServices(name='Intelligent Systems Lab Coordinator',
                                         category='department',
                                         faculty=faculty[10]))

fac_serv_klassner.append(models.FacultyServices(name='Director, Center of Excellence in Enterprise Technology',
                                         category='department',
                                         faculty=faculty[10]))

fac_serv_klassner.append(models.FacultyServices(name='Virtual Reality Lab Coordinator',
                                         category='department',
                                         faculty=faculty[10]))

fac_serv.append(fac_serv_klassner)

# Dr. Levitin (User 11)

users.append(models.User(fname='Anany',
                   lname='Levitin',
                   email='anany.levitin@villanova.edu',
                   vu_ldap='alevitin',
                   image=fac_images[11],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-7349',
                             #extension='1234',
                             user=users[11]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[11]))

'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://www.csc.villanova.edu/~levitin',
                         faculty_type='full time',
                         faculty_rank='Professor',
                         status='Active',
                         office_loc='MSC 162-B',
                         user=users[11]))


edu_levitin = []

edu_levitin.append(models.Education(degree='Ph.D.',
                             discipline='Mathematics',
                             school='Hebrew University of Jerusalem',
                             faculty=faculty[11]))

fac_edu.append(edu_levitin)


fac_int_levitin = []

fac_int_levitin.append(models.FacultyInterests(interest='Algorithms',
                                             faculty=faculty[11]))

fac_int_levitin.append(models.FacultyInterests(interest='Data and Information',
                                             faculty=faculty[11]))

fac_int.append(fac_int_levitin)


com_mem_levitin = []

com_mem_levitin.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[11],
                                             committee=com11))

com_mem_levitin.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[11],
                                             committee=com26))

com_mem_levitin.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[11],
                                             committee=com4))

com_mem_levitin.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[11],
                                             committee=com15))

com_mem_levitin.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[11],
                                             committee=com24))

fac_com_mem.append(com_mem_levitin)


fac_serv_levitin = []

fac_serv_levitin.append(models.FacultyServices(name='Advising: Class of 2018',
                                         category='department',
                                         faculty=faculty[11]))

fac_serv.append(fac_serv_levitin)

# Dr. Papalaskari (User 12)

users.append(models.User(fname='Mary',
                   minit='A.',
                   lname='Papalaskari',
                   email='mary.papalaskari@villanova.edu',
                   vu_ldap='mpapalas',
                   image=fac_images[12],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-7333',
                             #extension='1234',
                             user=users[12]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[12]))

'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://www.csc.villanova.edu/~map',
                         faculty_type='full time',
                         faculty_rank='Assistant Professor',
                         status='Active',
                         office_loc='MSC 162-C',
                         user=users[12]))


edu_papa = []

edu_papa.append(models.Education(degree='Ph.D.',
                             discipline='Artificial Intelligence',
                             school='Edinburgh University',
                             faculty=faculty[12]))

edu_papa.append(models.Education(degree='M.S.',
                             discipline='Computer Science',
                             school='University of Alberta',
                             faculty=faculty[12]))

edu_papa.append(models.Education(degree='B.S.',
                             discipline='Mathematics and Computer Science',
                             school='Lakehead University',
                             faculty=faculty[12]))

fac_edu.append(edu_papa)


fac_int_papa = []

fac_int_papa.append(models.FacultyInterests(interest='Computational Theory',
                                             faculty=faculty[12]))

fac_int_papa.append(models.FacultyInterests(interest='Artificial Intelligence',
                                             faculty=faculty[12]))

fac_int.append(fac_int_papa)


com_mem_papa = []

com_mem_papa.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[12],
                                             committee=com4))

com_mem_papa.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[12],
                                             committee=com10))

com_mem_papa.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[12],
                                             committee=com9))

com_mem_papa.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[12],
                                             committee=com28))

com_mem_papa.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[12],
                                             committee=com30))

fac_com_mem.append(com_mem_papa)


fac_serv_papa = []

fac_serv_papa.append(models.FacultyServices(name='Advising: Class of 2017',
                                         category='department',
                                         faculty=faculty[12]))

fac_serv.append(fac_serv_papa)

# Dr. Soong (User 13)

users.append(models.User(fname='Norman',
                   minit='L.',
                   lname='Soong',
                   email='norman.soong@villanova.edu',
                   vu_ldap='nsoong',
                   image=fac_images[13],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-6462',
                             #extension='1234',
                             user=users[13]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[13]))

'''

faculty.append(models.Faculty(salutation='Dr.',
                         website_url='http://www.csc.villanova.edu/~soong',
                         faculty_type='full time',
                         faculty_rank='Professor Emeritus',
                         status='Active',
                         user=users[13]))


edu_soong = []

edu_soong.append(models.Education(degree='Ph.D.',
                             discipline='Aerospace Engineering',
                             school='University of Florida',
                             faculty=faculty[13]))

edu_soong.append(models.Education(degree='M.S.',
                             discipline='Systems Engineering',
                             school='University of Pennsylvania',
                             faculty=faculty[13]))

edu_soong.append(models.Education(degree='M.S.',
                             discipline='Aerospace Engineering',
                             school='University of Florida',
                             faculty=faculty[13]))

edu_soong.append(models.Education(degree='B.S.',
                             discipline='Mechanical Engineering',
                             school='National Taiwan University',
                             faculty=faculty[13]))

fac_edu.append(edu_soong)


fac_int_soong = []

fac_int_soong.append(models.FacultyInterests(interest='Graphics',
                                             faculty=faculty[13]))

fac_int_soong.append(models.FacultyInterests(interest='Information Visualization',
                                             faculty=faculty[13]))

fac_int_soong.append(models.FacultyInterests(interest='Audible User Interfaces',
                                             faculty=faculty[13]))

fac_int.append(fac_int_soong)

'''
com_mem_soong = []

fac_com_mem.append(com_mem_soong)


fac_serv_soong = []

fac_serv.append(fac_serv_soong)
'''

# Dr. Way (User 14)

users.append(models.User(fname='Tom',
                   minit='P.',
                   lname='Way',
                   email='thomas.way@villanova.edu',
                   vu_ldap='tway',
                   image=fac_images[14],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-5033',
                             #extension='1234',
                             user=users[14]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[14]))

'''

faculty.append(models.Faculty(salutation='Dr.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://www.csc.villanova.edu/~tway',
                         faculty_type='full time',
                         faculty_rank='Associate Professor',
                         status='Active',
                         office_loc='MSC 160-A',
                         user=users[14]))


edu_way = []

edu_way.append(models.Education(degree='Ph.D.',
                             discipline='Computer Science',
                             school='University of Delaware',
                             faculty=faculty[14]))

edu_way.append(models.Education(degree='M.S.',
                             discipline='Computer Science',
                             school='University of Delaware',
                             faculty=faculty[14]))

edu_way.append(models.Education(degree='B.A.',
                             discipline='Film',
                             school='University of Maryland',
                             faculty=faculty[14]))

fac_edu.append(edu_way)


fac_int_way = []

fac_int_way.append(models.FacultyInterests(interest='Software Engineering',
                                             faculty=faculty[14]))

fac_int_way.append(models.FacultyInterests(interest='Compiler Optimization',
                                             faculty=faculty[14]))

fac_int_way.append(models.FacultyInterests(interest='Applied Computer Science',
                                             faculty=faculty[14]))

fac_int_way.append(models.FacultyInterests(interest='Nanocompilers',
                                             faculty=faculty[14]))

fac_int_way.append(models.FacultyInterests(interest='High Performance Computing',
                                             faculty=faculty[14]))

fac_int_way.append(models.FacultyInterests(interest='Modeling and Simulation',
                                             faculty=faculty[14]))

fac_int.append(fac_int_way)


com_mem_way = []

com_mem_way.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[14],
                                             committee=com5))

com_mem_way.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[14],
                                             committee=com11))

com_mem_way.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[14],
                                             committee=com4))

com_mem_way.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[14],
                                             committee=com20))

com_mem_way.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[14],
                                             committee=com19))

com_mem_way.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[14],
                                             committee=com42))

com_mem_way.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[14],
                                             committee=com23))

com_mem_way.append(models.CommitteeMembers(role='Chair',
                                             faculty=faculty[14],
                                             committee=com30))

com_mem_way.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[14],
                                             committee=com27))

com_mem_way.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[14],
                                             committee=com14))

com_mem_way.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[14],
                                             committee=com39))

fac_com_mem.append(com_mem_way)


fac_serv_way = []

fac_serv_way.append(models.FacultyServices(name='Advising: Class of 2018',
                                         category='department',
                                         faculty=faculty[14]))

fac_serv_way.append(models.FacultyServices(name='Villanova ACM Faculty Advisor',
                                         category='department',
                                         faculty=faculty[14]))

fac_serv_way.append(models.FacultyServices(name='Applied Computing Technology Lab Coordinator',
                                         category='department',
                                         faculty=faculty[14]))

fac_serv.append(fac_serv_way)

# Ms. Zimmerman (User 15)

users.append(models.User(fname='Barbara',
                   minit='H.',
                   lname='Zimmerman',
                   email='barbara.zimmerman@villanova.edu',
                   vu_ldap='bzimmerm',
                   image=fac_images[15],
                   user_role=user_role_prof))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-5354',
                             #extension='1234',
                             user=users[15]))

'''
user_offhour.append(models.OfficeHours(start_time=datetime.datetime(2014, 9, 1, 11, 30),
                                 end_time=datetime.datetime(2014, 9, 1, 14),
                                 apntmnt_msg='email beforehand',
                                 days='MWF',
                                 user=users[15]))

'''

faculty.append(models.Faculty(salutation='Ms.',
                         #secondary_email='person@fakemail.com',
                         website_url='http://homepage.villanova.edu/barbara.zimmerman',
                         faculty_type='full time',
                         faculty_rank='Instructor',
                         status='Active',
                         office_loc='MSC 160-B',
                         user=users[15]))


edu_zimmerman = []

edu_zimmerman.append(models.Education(degree='M.S.',
                             discipline='Computer Science',
                             school='University of Maryland',
                             faculty=faculty[15]))

edu_zimmerman.append(models.Education(degree='B.A.',
                             discipline='Mathematics',
                             school='University of Pennsylvania',
                             faculty=faculty[15]))

fac_edu.append(edu_zimmerman)


fac_int_zimmerman = []

fac_int_zimmerman.append(models.FacultyInterests(interest='Human-Computer Interaction',
                                             faculty=faculty[15]))

fac_int_zimmerman.append(models.FacultyInterests(interest='Software Project Management',
                                             faculty=faculty[15]))

fac_int_zimmerman.append(models.FacultyInterests(interest='Web Design',
                                             faculty=faculty[15]))

fac_int_zimmerman.append(models.FacultyInterests(interest='Computer Education for Non-Majors',
                                             faculty=faculty[15]))

fac_int.append(fac_int_zimmerman)


com_mem_zimmerman = []

com_mem_zimmerman.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[15],
                                             committee=com7))

com_mem_zimmerman.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[15],
                                             committee=com28))

com_mem_zimmerman.append(models.CommitteeMembers(role='Member',
                                             faculty=faculty[15],
                                             committee=com30))

fac_com_mem.append(com_mem_zimmerman)


fac_serv_zimmerman = []

fac_serv_zimmerman.append(models.FacultyServices(name='Advising: Class of 2018',
                                         category='department',
                                         faculty=faculty[15]))

fac_serv_zimmerman.append(models.FacultyServices(name='President, Phi Beta Kappa Delaware Valley Association',
                                         category='department',
                                         faculty=faculty[15]))

fac_serv.append(fac_serv_zimmerman)


### STAFF ###

# Adele Ballard (User 16)

users.append(models.User(fname='Adele',
                   minit='E.',
                   lname='Ballard',
                   email='adele.ballard@villanova.edu',
                   vu_ldap='aballard',
                   image=staff_images[0],
                   user_role=user_role_staff))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-7310',
                             #extension='1234',
                             user=users[16]))

staff.append(models.Staff(position='Administrative Assistant',
                       office_loc='MSC 161',
                       user=users[16]))

# Joe Dalbo (User 17)

users.append(models.User(fname='Joe',
                   lname='Dalbo',
                   email='joseph.dalbo@villanova.edu',
                   vu_ldap='jdalbo',
                   image=staff_images[1],
                   user_role=user_role_staff))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-5334',
                             #extension='1234',
                             user=users[17]))

staff.append(models.Staff(position='PC LAN Administrator',
                       office_loc='MSC G55',
                       user=users[17]))

# Anne Hischar (User 18)

users.append(models.User(fname='Anne',
                   minit='L.',
                   lname='Hischar',
                   email='anne.hischar@villanova.edu',
                   vu_ldap='ahischar',
                   image=staff_images[2],
                   user_role=user_role_staff))

staff.append(models.Staff(user_id=users[18],
                       position='Administrative Assistant II',
                       office_loc='MSC 161',
                       user=users[18]))

# Najib Nadi (User 19)

users.append(models.User(fname='Najib',
                   lname='Nadi',
                   email='najib.nadi@villanova.edu',
                   vu_ldap='nnadi',
                   image=staff_images[3],
                   user_role=user_role_staff))

user_phone.append(models.PhoneNumber(area_code='(610)',
                             number='519-4852',
                             #extension='1234',
                             user=users[19]))

staff.append(models.Staff(position='Systems Administrator', 
                        office_loc='MSC 165-C',
                        user=users[19]))




#### ADD TO DATABASE ####

#db.create_all()

### ADD USER ROLES ###
db.session.add(user_role_prof)
db.session.add(user_role_grad)
db.session.add(user_role_staff)
db.session.add(user_role_ugrad)
db.session.add(user_role_web)

### ADD COMMITTEES ###
for i in range(1,45):
  db.session.add(eval("com" + str(i)))

### ADD FACULTY IMAGES ###
for i in fac_images:
  db.session.add(i)

### ADD STAFF IMAGES ###
for i in staff_images:
  db.session.add(i)

### ADD USERS ###
for i in users:
  db.session.add(i)

### ADD USER PHONE NUMBERS ###
for i in user_phone:
  db.session.add(i)

### ADD USER OFFICE HOURS ###
'''
for i in user_offhour:
  db.session.add(i)
'''

### ADD FACULTY ###
for i in faculty:
  db.session.add(i)

### ADD FACULTY EDUCATIONS ###
for i in fac_edu:
  for j in i:
    db.session.add(j)

### ADD FACULTY INTERESTS ###
for i in fac_int:
  for j in i:
    db.session.add(j)

### ADD FACULTY COMMITTEE MEMBERSHIPS ###
for i in fac_com_mem:
  for j in i:
    db.session.add(j)

### ADD FACULTY SERVICES ###
for i in fac_serv:
  for j in i:
    db.session.add(j)

### ADD STAFF ###
for i in staff:
  db.session.add(i)

db.session.commit()




