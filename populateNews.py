from app import db, models
import datetime

### NEWS IMAGES ###
news_images = []

news_images.append(models.Image(image_type='news',
                          alt_text="UPE Logo",
                          image_extension='png'))

news_images.append(models.Image(image_type='news',
                          alt_text="Programming Team",
                          image_extension='png'))

news_images.append(models.Image(image_type='news',
                          alt_text="VWCS",
                          image_extension='png'))


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



### SIDEBAR IMAGES ###
sb_images = []
'''
sb_images.append(models.Image(image_type='sidebar',
							alt_text='',
							image_extension='',
							image_name=''))
'''
sb_images.append(models.Image(image_type='sidebar',
							alt_text='',
							image_extension='',
							image_name=''))



### SIDEBAR ###

sideview = []

sideview.append(models.Sideview(
    content='A team of students (Jasmine Serano, David Siah, Will Makabenta, Zachary '
    'Zaccaro ...  with a nod to former team members Peter Rokowski and Sahithi Yalamanchi) '
	'led by Xiaojie Jiang are creating a new version of our department website. Technologies '
	'involved include Python, Flask, JQuery, Git, MySQL, HTML5, and CSS3. Follow their progress '
	'<a href="http://cscvillanova.pythonanywhere.com/">HERE</a> but keep in mind that we still '
	'need to populate the underlying database. Stay tuned.',
    title='New Web Site Coming',
    category='Check This Out',
    active=1,
    image=sb_images[0]))

sideview.append(models.Sideview(
    content="For our Senior Project, "
    "we will be creating an interactive paint program using the Xbox 360 Kinect to "
    "control the various commands.  Primarily, we will focus on working with GIMP, a "
    "freely distributed piece of software for such tasks as photo retouching, image "
    "composition and image authoring, and/or Green Foot, an interactive Java development "
    "environment designed primarily for educational purposes at the high school and "
    "undergraduate level that allows for easy development of two-dimensional graphical "
    "applications, such as simulations and interactive games, to utilize the motion "
    "detection from the Xbox 360 Kinect to apply abstract paint functions such as splash.  "
    "This will ultimately be a proof of concept and more showing how body motion can be "
    "detected to apply visual effects on a photo editing program such as GIMP.  One of "
    "the main effects we would like to see is the paint splash effect on a photo with the "
    "effect intensity dependent on arm motion intensity.  We would also like to further "
    "investigate other possibilities of free body motion that can be applied to our photo "
    "editing program which we believe may promote creativity.",
    title='GIMP Kinect Plugin (Anthony DiValerio & Sang Cheon)',
    category='Senior Project',
    active=0,
    image=sb_images[1]))

sideview.append(models.Sideview(
    content="Our senior project deals with the advent of "
    "virtual reality (VR). The two main VR devices at the moment are the Google Cardboard "
    "and the Oculus Rift (now owned by Facebook). The Google Cardboard is quite literally "
    "made of cardboard and uses certain Android based phones to create a 3d headset. The "
    "phone slides into the cardboard horizontally, the screen displays two separate images "
    "on the screen, and the special lenses act as 3d glasses and the images become a single "
    "3d image. The Oculus Rift is a specially made headset with its own screen to recreate a "
    "three dimensional space. The Oculus headset in combination with a camera, track your head "
    "movements and adjust the picture on the headset's screen to match your real time motions. "
    "Our goal is to create a 3d environment using both technologies and then compare the two "
    "technologies. A few of the questions we hope to answer at the end of this project are: a) "
	"Does the cost between the two devices affect the quality of the device? (Do you get what "
	"you pay for?) b) Is this technology ready for mass consumption and what would its uses be "
	"to your average citizen and society in general? c) What are the current capabilities of VR technology?",
    title='CodeWarriors',
    category='Senior Project',
    active=0,
    image=sb_images[2]))

sideview.append(models.Sideview(
    content="NeuroSoccer is the name of my project, and its goal is "
    "to implement the Q-Learning Algorithm, modified for a Neural Network, in a basic soccer game. "
    "Q-Learning works by exploring the state space of the game, and determining potential reward "
    "for each action. My plan is to train an individual player to kick the ball, and score a goal "
    "in the net. Then, multiple players will be grouped and will train together as a team. Once "
    "multiple teams are trained, I will have a round robin style tournament to determine the best "
    "team. Each team will have slightly different attributes such as amount of information relayed "
    "to the neural network, training time, number of neurons etc.The hope is to determine which "
    "attributes contribute most significantly to training time, and overall team performance. "
    "Technologies used will be Python. Graphics rendering will be done using the PyGame Library. "
    "Neural Networks will leverage a library called PyBrain, which is a general purpose machine "
    "learning library with a focus on neural networks. The game logic will all be hand coded, using "
    "PyGame simply for graphics rendering.",
    title='NeuroSoccer',
    category='Senior Project',
    active=0,
    image=sb_images[3]))

sideview.append(models.Sideview(
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
    active=0,
    image=sb_images[4]))

sideview.append(models.Sideview(
    content="Mojo Rank is an (anti)social network for college students - in particular "
    "Villanova - that facilitates positive freedom of expression. We allow users to post "
    "as themselves or postanonymously, and we encourage people to post photos, text, or "
    "other pieces of content relevant to them. The purpose of this site is twofold: 1. "
    "To give college students an incredible social networking platform, specifically for "
    "people who only go to their college/university, and 2. To provide a friendly outlet "
    "for people to express themselves and their views. People are far less likely to say "
    "what they actually think on social networks, and it would be great to have a platform "
    "which doesn't trap users into varying forms of technological groupthink.",
    title='Mojo Rank',
    category='Senior Project',
    active=0,
    image=sb_images[5]))

sideview.append(models.Sideview(
    content="Luke and Nick will be creating a website for the Blue Key Society, the "
    "organization on campus that is responsible for giving tours to prospective students "
    "and their families. The website's purpose is twofold: to provide information about "
    "the society and its members to prospective students and tour guides and to be a tool "
    "that the current members of the society can use as well. The website will include "
    "information about the society's current executive board; a directory of all current "
    "members that will list their names, majors, hometowns, and expected dates of graduation; "
    "a calendar of Blue Key events; a page where members can request a substitute as well as "
    "volunteer for a special tour; and a list of the Blue Key family standings that will be "
    "updated weekly.",
    title='Blue Key Site',
    category='Senior Project',
    active=0,
    image=sb_images[6]))

sideview.append(models.Sideview(
    content="Algorithmic trading goes by many different names including: automated trading, "
    "black-box trading, or algo trading. The basis of algorithmic trading is exactly as it "
    "sounds, it is the process of trading through the execution of an algorithm that is constantly "
    "analyzing the market and its indicators. Who uses algorithmic trading? Algorithmic trading "
    "is used by investment banks, pension funds, mutual funds, and other buy-side (investor-driven) "
    "institutional traders. How is algorithmic trading used? Algorithmic trading is used for many "
    "different purposes varying based on how the algorithm is implemented and what types of "
    "indicators/variables are used. We have developed a system that allows the users to take advantage "
    "of basic stock analysis algorithms. With this system, users are able to produce trend lines and "
    "tunnels based on historical data, which will allow them to make decisions for the future.",
    title='Algorithmic Trading',
    category='Senior Project',
    active=0,
    image=sb_images[7]))

sideview.append(models.Sideview(
    content="As graphics scenes continue to grow in importance and complexity, it becomes increasingly "
    "challenging to efficiently select a three-dimensional object from a graphics scene.  There is "
    "currently a lack of readily available information about algorithms which will allow responsiveness "
    "in graphics scenes to keep up with its intricacy.  From a gaming perspective, complexity in computer "
    "graphics has increased so drastically because thousands of users can participate together in games "
    "which involve a high frequency of selecting objects from a graphics scene - situations which used to "
    "just involve one individual.  Selecting three-dimensional objects from a graphics scene poses a challenge "
    "because each object exists in a native, local coordinate system which needs to eventually be realistically "
    "seen on a two-dimensional screen in order to be selected by users.  We intend to begin by evaluating the "
    "theory and mathematics behind these operations.  Following this analysis, our goal is to properly document "
    "an efficient picking algorithm, the type of algorithms used for selection, which will retain appropriate "
    "performance as graphical complexity continues to grow.  To do this, we will evaluate the ray casting and "
    "color picking algorithms in terms of speed and accuracy and compare our results throughout different "
    "complexities.  We hope to conclude that under certain conditions, regardless of user, one algorithm "
    "significantly outperforms the other.",
    title='3D Graphics Environments',
    category='Senior Project',
    active=0,
    image=sb_images[8]))

sideview.append(models.Sideview(
    content='We aim to create a web application that utilizes the data on Twitter in order to allow users to stay '
    'informed and up-to-date with the most popular and current events taking place around the world. Fundamentally '
    'speaking, the application will search and collect data from tweets on Twitter that contain trending hashtags. '
    'Since trending hashtags are dependent on physical location, we will allow users to specify which location they '
    'are interested in obtaining information about. The web application will then analyze the aggregated tweets and '
    'search for any sub-trends or patterns that could provide more insight and information into the current event. '
    'For example, a few weeks ago, "#VMAs" was a trending hashtag around the United States. The hashtag "VMAs", which '
    'refers to the famous Video Music Awards, does not really provide much information about the award ceremony. The '
    'real information lies within the millions of tweets posted during the event about people\'s favorite performances, '
    'their opinions on things that took place at this renowned ceremony and all forms of celebrity gossip. One can manually '
    'read through these tweets to learn this information but that would be both tedious and deadly. Not only that, '
    'reading tweets manually would not provide a user with an accurate and complete depiction of all of the tweets in '
    'circulation. Our web application aims to solve this issue.<br>Fundamentally, our application reads through the '
    'millions of tweets and keeps track of reoccurring words and phrases. Our application only focuses on important nouns '
    'and phrases, omitting words such as "the," "is," "they," "he" and "because". The information is also presented in an '
    'aesthetically pleasing and easy to read manner. Staying up-to-date and informed has never been easier! All in all, we '
    'hope our project proves that Twitter can be used as a more reliable, authentic and quick alternative to mainstream news '
    'stations such as CNN and Fox News.',
    title='Data Gurus Application',
    category='Senior Project',
    active=0,
    image=sb_images[9]))

sideview.append(models.Sideview(
    content='Last year, the Block-It Scientists were hired to create a Villanova Volleyball Summer Camp Registration website, '
    'which allows aspiring volleyball players to sign up for a 4 day summer camp with Villanova\'s Head Volleyball Coach, Josh '
    'Steinbach. We initially built the site using WordPress but we have now decided to restructure the site from the ground up '
    'using some tools that are new to us such as JavaScript, HTML, CSS, PHP and Twitter Boostrap. Using WordPress and some of '
    'its free plug-ins was effective, but we had to sacrifice some functionality and control in order to get our site up and '
    'running as quickly as possible. While WordPress was an outstanding tool to use for the first time around, we would like '
    'to experiment with rebuilding and redesigning the site from our own code, which in the long run, will give us more control '
    'of our site and hopefully better usability, functionality and visibility for users, administrators and developers. Along '
    'the way, we will be drawing comparisons between the two different implementations to see which version is more applicable '
    'and efficient.',
    title='Villanova Volleyball Registration Website',
    category='Senior Project',
    active=0,
    image=sb_images[10]))

sideview.append(models.Sideview(
    content='Edward J. McLaughlin III originally enrolled at Villanova University within the college of Commerce and Finance.  '
    'Halfway through his freshman year, he discovered that he had a strong interest in Computer Science.  After speaking briefly '
    'over the phone with Dr. Beck, he immediately decided to enroll within the program.  Throughout his tenure within the '
    'department of Computer Science, he took several courses that not only exposed him to the many facets of computing, but they '
    'also gave him the opportunity to choose his direction professionally.  Originally, he was a consultant working with Oracle '
    'Database systems, but after having the opportunity to build custom web based applications, he focused on complete web based '
    'application solutions.  Throughout the past 14 years, he has worked as a software engineer designing applications from the '
    'database level up through to the client level.  He has worked for private corporations and Fortune 50 companies such as '
    'Walgreens.  Today, after developing applications for so many years, he is now a Principal Solution Architect for Comcast in '
    'Center City, Philadelphia.  He is responsible for not only designing responsive client facing applications (web and mobile '
    'based), but for guiding development teams as a mentor and guide to ensure efficient and robust applications.',
    title='Edward J. McLaughlin III',
    category='Where Are They Now?',
    active=0,
    image=sb_images[11]))

sideview.append(models.Sideview(
    content='For my senior project I am building a web site for a band called Future Games. The page can be found here: '
    'www.futuregamesband.com. In addition I am creating a site editor for the band members to make updates to their web '
    'site whenever they would like. The band will have a user name and password to access this editor, and once logged in, '
    'will be presented with a user-friendly interface to change information like biography, show information, music, photos, '
    'and videos. Since I am connecting the site to a MySQL database, the editor is basically a front end way to edit database '
    'content, allowing changes to be immediately viewable on the band homepage.  Also for this project, I will be researching '
    'SEO, good web design practices, in terms of site content and UX, specifically for band websites, as well as new social '
    'media ideas to incorporate. I hope to create an optimal way for fans to interact with a band via web site, as well as a '
    'fully customizable site which band members can easily edit.',
    title='Kristin Arcurio',
    category='Senior Project',
    active=0,
    image=sb_images[12]))

sideview.append(models.Sideview(
    content='Villanova\'s voice is a web application being developed for student use. It lets students anonymously post their '
    'thoughts and rate them in various ways. There is also a way to comment on thoughts and report them. The website contains '
    'various filters which can show such things as which posts are most popular or controversial. Comments can also be agreed '
    'or disagreed with but only appear within a post. This anonymous thought board would be a good way to know what the '
    'student body is thinking and how they feel about certain things at the university or surrounding area. The main focus of '
    'this application is anonymity. The anonymous quality is something which would be valued when compared to a social network '
    'such as Facebook. Villanova\'s Voice\'s anonymous social platform will enable student discussion and a more communal '
    'Villanovan perspective. All of Villanova should have a place to communicate and share personal thoughts.',
    title='Joseph Quadrino',
    category='Senior Project',
    active=0,
    image=sb_images[13]))

sideview.append(models.Sideview(
    content='Yapl (Yet another Programming Language) is a superset of the ECMA 262 programming language specification, '
    'specifically the JavaScript implementation.  Yapl aims to simplify JavaScript by stripping out tedious semantic and syntactic '
    'boilerplate, while also providing higher levels of expressiveness with far less code.  Yapl adds both original features and '
    'elements borrowed from other modern programming languages such as Ruby.   Its design focuses on providing a syntax that is clean, '
    'unobtrusive, the overall goal being to maximize the expressiveness of the language and minimize the size of the source code.'
    '<br>Yapl removes much of JavaScript\'s unnecessary boilerplate syntax and semantics in favor of more concise, terse, and cleaner '
    'code.  Its syntax ends up very closely resembling that of Ruby\'s.  Aside from syntax, Yapl still aims to preserve all of '
    'JavaScript\'s features, and also adds both original features and features inspired by other languages, such as Ruby and '
    'Python.<br>Yapl\'s primary execution environment is client-side web applications.  All major browsers in use today support '
    'JavaScript as their primary client-side scripting language, which means that Yapl will first and foremost compile to JavaScript.  '
    'Compiling to JavaScript means developers can use Yapl to write client-side web applications, with the resulting compiled code '
    'being served to the browser.  There are also projects that allow JavaScript to be run out of the context of a browser, such as '
    'Rhino and Node.js, meaning Yapl does not necessarily run exclusively in the browser context.',
    title='Taylor Clifton',
    category='Senior Project',
    active=0,
    image=sb_images[14]))

sideview.append(models.Sideview(
    content='A web application that provides an interface for students to take assignments (exams, homeworks) and provides data about '
    'their performance. Each assigned problem has a set of data points that enables tutors and parents to pin down individual skills '
    'or concepts that the student is missing. The students can log into the application through a browser and see their current and '
    'past assignments plus data for each and aggregated data. Tutor can see data for each student and create assignments tailored to '
    'each individual student. The system also recommends problems to assign based on individual user perfomance and collaborative '
    'filtering (users who missed X also missed Y). The application is being developed using an MVC architecture and Ruby on Rails. '
    'It is hosted on Heroku and Amazon S3.<br>The frontend is built mainly on bootstrap, html5 and jquery.',
    title='Ivan Barria',
    category='Senior Project',
    active=0,
    image=sb_images[15]))

sideview.append(models.Sideview(
    content='Our project is taking social networking to another level. While almost everyone can update their facebooks and twitters '
    'on their phones, we are providing another way in which you can express yourself. Using a microcontroller, users will now be able '
    'to update their statuses and tweets using Morse code. Imagine yourself in a situation where you are unable to look at your keyboard '
    'for proper typing, or need to free up one of your hands while tweeting. Morse code is simple and only requires two characters, dots '
    'and dashes, to get your message across. Using Arduino, we will program the microcontroller to accept dots and dashes from two '
    'different buttons. Our software will then convert the dots and dashes into the intended message and post to facebook or twitter. '
    'Our project will make it easier and more fun to update your statuses and tweets.',
    title='Roberra Akillu & Patrick Ringelstein',
    category='Senior Project',
    active=0,
    image=sb_images[16]))

sideview.append(models.Sideview(
    content='Bookshelf is a social media website that allows users to share with each other the book(s) they are currently reading, '
    'have read, and/or wish to read. Each user will have an account and homepage. They will be required to login using their username '
    'and password. In addition to information about books, user homepages will include a short bio and profile picture. Users will be '
    'able to edit and view their own homepage, as well as look at other users homepages. Users will subscribe to other users, similar '
    'to Twitter. There will be a main feed which will display updates from all subscribed users, such as, '
    '"Ben Woodrum started Green Eggs and Ham," or "James Mensch finished The Great Gatsby." Users will be able to comment on these '
    'updates. Email notifications will be sent to users when someone comments on his or her update. Users will also have the option of '
    'writing book reviews. There will be a section on the homepage under which reviews are placed.',
    title='Steve Garvin, James Mensch, Ben Woodrum',
    category='Senior Project',
    active=0,
    image=sb_images[17]))



### POPULATE DATABASE ###

for i in news:
	db.session.add(i)

db.session.commit()