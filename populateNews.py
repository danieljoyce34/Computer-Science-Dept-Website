from app import db, models
import datetime

### NEWS IMAGES ###
news_images = []

news_images.append(models.Image(image_type='news',
                          alt_text="UPE 2015",
                          image_extension='png',
                          image_name='UPE2015'))

news_images.append(models.Image(image_type='news',
                          alt_text="Programming Team",
                          image_extension='png',
                          image_name='programming_team'))

news_images.append(models.Image(image_type='news',
                          alt_text="VWCS",
                          image_extension='png',
                          image_name='VWCS'))


### NEWS ###
news = []

news.append(models.News(headline='Congratulations 2015 UPE Inductees!',
                    intro='On October 23, 2015 nineteen students were recognized for '
                    'their outstanding academic achievements at the 16th induction ceremony '
                    'of the Villanova chapter of Upsilon Pi Epsilon (UPE), the International '
                    'Honor Society for Computing and Information disciplines. These students '
                    'rank in the highest 25 percent of their major and have completed at least half '
                    'of the core credits and at least half of the major credits. In addition, '
                    'the undergraduate students have attained a GPA of 3.5 or higher, and the '
                    'graduate students have attained a GPA of 3.75 or higher. Congratulations '
                    'to ALL! Pictures Of the 2015 UPE Induction can be found at the following '
                    'links: http://tinyurl.com/UPEInduction-15 and http://webster.csc.villanova.edu/~mdamian/photos/upe15/',
                    article='On October 23, 2015 nineteen students were recognized for their outstanding '
                    'academic achievements at the 16th induction ceremony of the Villanova chapter of '
                    'Upsilon Pi Epsilon (UPE), the International Honor Society for Computing and Information '
                    'disciplines. These students rank in the highest 25 percent of their major and have completed at '
                    'least half of the core credits and at least half of the major credits. In addition, the '
                    'undergraduate students have attained a GPA of 3.5 or higher, and the graduate students '
                    'have attained a GPA of 3.75 or higher. Congratulations to ALL! Pictures Of the 2015 UPE '
                    'Induction can be found at the following links: http://tinyurl.com/UPEInduction-15 and '
                    'http://webster.csc.villanova.edu/~mdamian/photos/upe15/ <br><br>'
                    'Undergraduate Inductees: <br>'
                    '1.     Alyson Hopkins <br>'
                    '2.     David Siah <br>'
                    '3.     Jasmine Serano <br>'
                    '4.     Kent Wu <br>'
                    '5.     Nicholas Grupen <br>'
                    '6.     Rachel Malloy <br>'
                    '7.     Zachary Rahn <br>'
                    '8.     Zachary Zaccaro <br>'
                    '9.     Nicholas Vandervoorn <br><br>'
                    'Graduate Inductees: <br>'
                    '1.     Gopi Krishna Chitluri <br>'
                    '2.     Andrew Grace <br>'
                    '3.     Naresh Nelavalli <br>'
                    '4.     Shruthika Vangala <br>'
                    '5.     Raja Harish Vempati <br>'
                    '6.     Sai Ramya Mounika Karri <br>'
                    '7.     Naga Sai Bharadwaj Vadlamannati <br>'
                    '8.     Neha Karing <br>'
                    '9.     Sahithi Yalamanchi <br>'
                    '10.    Kevin Cloutier', 
                    image=news_images[0]))

news.append(models.News(headline='Programming Team Wins!',
                   intro='The department programming club sent a team of three students to the CCSC Eastern '
                   'Conference on Saturday, October 24. (David Siah, Kent Wu, and Alex Damian)',
                   article='The department programming club sent a team of three students to the '
                   'CCSC Eastern Conference on Saturday, October 24. David Siah, Kent Wu, and Alex '
                   'Damian were up early Saturday, leaving Villanova at 6:30 sharp, well let\'s say '
                   '"sharpish". Arriving at Stockton University with 15 minutes to spare they first '
                   'attacked the breakfast buffet and then got busy tackling the contest problems. '
                   'The problem set consisted of six problems ranging in difficulty from "very easy" '
                   'to "almost impossible" The contest lasted three hours during which time the team '
                   'solved three of the problems correctly and in the words of the contest judge were '
                   '"extremely close" to solving a fourth. None of the other 18 teams in the contest '
                   'solved more than two problems so the Villanova "Ain\'t Too Proud To Brute-Force" '
                   'team easily took first place. Congratulations!', 
					         image=news_images[1]))

news.append(models.News(headline='Villanova Women in Computer Science host Resume and Interview Workshop',
                   intro='Presenting yourself in a competitive world is a tough challenge for anyone. '
                   'On Friday, October 2, 2015, the Villanova Women in Computer Science (VWCS) hosted '
                   'a workshop on resume-writing and interview skills facilitated by career expert Beth '
                   'Cahill, Assistant Director of Student Services.  Beth provided important tips on what '
                   'to reveal in a resume that says “Interview me!” and what to keep to yourself, how to '
                   'prepare for successful interviews and how to make the most out of networking opportunities. '
                   'This great workshop helped students get started on their job and internship searches with '
                   'confidence, and built a momentum that will continue throughout the upcoming 2015 Grace '
                   'Hopper experience.',
                   article='Presenting yourself in a competitive world is a tough challenge for anyone. '
                   'On Friday, October 2, 2015, the Villanova Women in Computer Science (VWCS) hosted '
                   'a workshop on resume-writing and interview skills facilitated by career expert Beth '
                   'Cahill, Assistant Director of Student Services.  Beth provided important tips on what '
                   'to reveal in a resume that says “Interview me!” and what to keep to yourself, how to '
                   'prepare for successful interviews and how to make the most out of networking opportunities. '
                   'This great workshop helped students get started on their job and internship searches with '
                   'confidence, and built a momentum that will continue throughout the upcoming 2015 Grace '
                   'Hopper experience.', 
                   image=news_images[2]))


### POPULATE DATABASE ###

for i in news_images:
  db.session.add(i)

for i in news:
  db.session.add(i)

db.session.commit()