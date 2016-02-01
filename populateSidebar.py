from app import db, models
import datetime

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

sideview.append(models.Sideview(
    content='Have you ever been frustrated in the grocery store when having to double back to previously visited aisles just to get '
    'one item that you forgot while going through your grocery list? Have you ever missed out on saving money when you didn\'t '
    'check for what items were on sale or print out online coupons? The GrocerEZ Program seeks to eliminate these annoyances with '
    'the ability to craft a grocery list organized by the aisles of the local store selected by the user. On print out, the program '
    'would print out the user\'s list with associated aisles along with any coupons online that were selected. With a database '
    'maintaining the information behind the scenes, the user is also given the ability to easily customize the information about '
    'their local stores if the store reorganizes its inventory. Eventually, this program will be ported to Android and iOS to '
    'further user convenience even further.',
    title='The GrocerEZ Program (Christopher Chestnut)',
    category='Senior Project',
    active=0,
    image=sb_images[18]))

sideview.append(models.Sideview(
    content='For our senior project we will be releasing four new iPhone games. These will be based on classic arcade games, '
    'but with unique twists and themes. Also, we are going to improve our company, Kitri Software LLC. We have plans to redesign '
    'our website and create a social media presence. We will also be converting one of our most popular iPhone applications '
    '"Swimming Converter" to the Android platform.<br>Kitri Software, LLC is continuing to grow and expand. In the near future, '
    'we will be releasing even more advanced iPhone and Android applications. Current plans also include launches of several '
    'full-length games before 2013. In the future, Kitri Software, LLC will be building a portfolio of applications related to '
    'specific companies.<br>Please find our apps in the store under Ben Smith Apps. Also, please check out (and rate!!) our first '
    'game released as part of this project (Avalanche Dodge), It\'s FREE!<br>http://itunes.apple.com/us/app/avalanche-dodge/id545016614?mt=8',
    title='Benjamin Smith & Philip Williams',
    category='Senior Project',
    active=0,
    image=sb_images[19]))

sideview.append(models.Sideview(
    content='SagaScribe is a chat-based game engine designed to give creative control to the users. We take form of traditional '
    'table-top gaming, where one player is a GameMaster who creates the rules and story for other players to follow, and where '
    'dice are rolled to determine outcomes of events, and make it online. Each player is given a profile, with a name, stats, '
    'class, etc. and allowed to connect to a game where one player (the host or in this case GameMaster) chooses the background '
    'images, and sounds to play, etc. Each player is also given a "dice" button which randomly generates a number from 1-20 to '
    'simulate a real world 20-sided dice. With all of these things in place, we can effectively simulate a table-top game through '
    'our computers and across long distances.<br> The goal of this is to make an immersive chat based game, that follows the '
    'traditional set-up of table-top games like dungeons and dragons. Simply put, we create a framework for others to use to create '
    'their own unique games.',
    title='Tom English, Travis Klein, Peter Rowkowski & Matt Sher',
    category='Senior Project',
    active=0,
    image=sb_images[20]))

sideview.append(models.Sideview(
    content='For this project, we are looking to help the realtors of the Critelli Realtors company. In the past, the realtors '
    'had to enter the same listing information in multiple social media. They might have had to enter such information in places '
    'like Facebook, Twitter, Realtor.com, Trulia as well as other various sites. We would like to make their job a little bit '
    'easier by creating a "Universal  Updater Form." This form would be a portal that would send the listing information to these '
    'sites for the realtor. This way, instead of entering the same information multiple times in multiple locations, the realtors '
    'would simply have to enter it once and all of the necessary sites will be updated.  We are doing all of our work through a test '
    'site as to not interfere with their working site CritelliandKilbride.com. Once we have achieved all of the necessary connections '
    'with the social media, the Critelli Realtors will be able to implement our work into their own site.',
    title='Alyssa Critelli & Amy Zuerndorfer',
    category='Senior Project',
    active=0,
    image=sb_images[21]))

sideview.append(models.Sideview(
    content='Team Tre Amici is creating an Android application which will be ideal for runners. The app will recognize how quickly '
    'a person is running or moving and based on that data, will select an appropriate song from a playlist based on the BPM of each '
    'song. In other words, a person running quickly will hear fast songs while a person walking slowly will hear slower ones. Along '
    'with this, the app will track the runner\'s movement and display the path via Google Maps. After the runner is finished, the app '
    'will display the distance ran, along with other statistics. This app is written in Java and XML. The goal of this project is to '
    'make a more enjoyable experience for a runner and allow him or her to focus more on his or her exercise routine rather than the '
    'hassle of switching songs. It will also provide a runner with useful analytics that will allow the user to see his or her '
    'progress over time.',
    title='James Bradley, Mauro Mescia & Kristen O\'Leary',
    category='Senior Project',
    active=0,
    image=sb_images[22]))

sideview.append(models.Sideview(
    content='Team Muisdro is creating an application in collaboration with Villanova\'s volleyball team. The application will use '
    'a URL provided by the user to locate a page with play by play information about a volleyball match. It will then scan that '
    'page and create pertinent information, such as the percentage of service points won for each server and provide it for the user. '
    'The user will have the ability to indicate more than one match and if they like to indicate that they want the entire season\'s '
    'data to be accumulated and turned into information. If all goes well, there is an opportunity for this program to be used by '
    'other teams or clubs with minimal changes to the code due to the modularized approach that we will take.',
    title='Karen Mui & Bianca Isidro',
    category='Senior Project',
    active=0,
    image=sb_images[23]))

sideview.append(models.Sideview(
    content='<ul>'
	'<li><b>Jill Kramer</b> worked for an REU program at University of Rhode Island. She added to a program that was originally '
	'created to find remnants of cloud computing applications on a computer.</li>'
	'<li><b>Kristin Arcurio</b> interned at Lilly Pulitzer in the E-Commerce department as a web developer. She worked on '
	'programming for the website and Facebook applications.</li>'
	'<li><b>Matthew Sher</b> worked at Epsilen with the User Experience team to make the prohibitively complex web application '
	'more accessible to everyday users. </li>'
	'<li><b>Jeffrey Linahan</b> interned at the Jet Propulsion Laboratory, working on DARTS, moving them off the Bullet '
	'collision detection library and onto PQP. </li>'
	'<li><b>Tom English</b> worked at Wingspan LLC, writing scripts to stress-test Wingspan\'s cloud application. He used '
	'Jmeter to simulate users connecting to the service and performing tasks. </li>'
	'<li><b>Travis Klein</b> interned at Automated Financial Systems, working a lot with Cisco systems.</li>'
	'</ul>',
    title='Here are some of the jobs and internships CS majors have participated in over this past summer.',
    category='Summer Internships',
    active=0,
    image=sb_images[24]))

sideview.append(models.Sideview(
    content='<ul>'
	'<li><b>Stephen Garvin</b> worked at Barclays with a trade validation and enrichment application. He applied the tool '
	'Maven to the international version.</li>'
	'<li><b>Roberra Akilu</b> interned at the Vanguard Group and worked on restructuring how the company acquires and '
	'stores financial data.</li>'
	'<li><b>Benjamin Woodrum</b> worked at thismoment, creating and developing their testing process on their whole '
	'system. He implemented an open source software project called \'Jenkins\' to utilize its continuous integration '
	'functionality.</li>'
	'<li><b>Peter Rokowski</b> worked at Disruptive Apps doing Web programming, using PHP, Ajax, JQuery among other '
	'things. He also built a channel for the Roku Box. </li>'
	'<li><b>Erica Hagman</b> worked at F.W. Davison & Company, Inc. and wrote their new Employee Self Service web application '
	'that employees will use for their payroll service.</li>'
	'</ul>',
    title='Here are some of the jobs and internships CS majors have participated in over this past summer.',
    category='Summer Internships',
    active=0,
    image=sb_images[25]))

sideview.append(models.Sideview(
    content='<ul>'
	'<li><b>Kristen O\'Leary</b> interned at Goldman Sachs, working on GS Collections, which is an open source Java '
	'Collections Framework.</li>'
	'<li><b>Bianca Isidro</b> worked at QVC in the IT Department for the Applications Development team. She worked '
	'on testing and debugging applications that the producers, editors, sales teams, etc all work with in order to '
	'keep track of products that are to be shown on the shows throughout the day.</li>'
	'<li><b>Alyssa Critelli</b> interned at Market Street Advisors as a junior software engineer. She wrote Perl '
	'scripts, and was responsible for the implementation of a ticketing system for their support team.</li>'
	'<li><b>Kristin Palazzolo</b> worked at Customs & Border Protection - Office of Information Technology, fixing '
	'old and broken computers as well as printers in order for them to be donated to local schools and charities.</li>'
	'<li><b>Christopher Backofen</b> worked at Villanova University\'s Information Technology Department (UNIT) '
	'as a Web Developer.</li>'
	'</ul>',
    title='Here are some of the jobs and internships CS majors have participated in over this past summer.',
    category='Summer Internships',
    active=0,
    image=sb_images[26]))

sideview.append(models.Sideview(
    content='<ul>'
	'<li><b>William Solomito</b> worked at Lutron Electronics Co., Inc creating automated testing for one of their '
	'commercial systems.</li>'
	'<li><b>Osagie Ighodaro</b> worked at Deloitte & Touche, analyzing IT systems, those primarily used for reporting '
	'financial statements, and testing for competency and risks.</li>'
	'<li><b>Philip Williams</b> worked at BarclayCard US, building a Service Governance Registry, as well as working '
	'on mobile app and web development.</li>'
	'<li><b>Christopher Chestnut</b> worked at Dow Jones Inc. with the Mobile Unit team on the Wall Street Journal app '
	'for the iPad.</li>'
	'<li><b>Benjamin Smith</b> worked at IBM as part of the managed services group installing IBM\'s Watson onto '
	'different computing clusters. </li>'
	'</ul>',
    title='Here are some of the jobs and internships CS majors have participated in over this past summer.',
    category='Summer Internships',
    active=0,
    image=sb_images[27]))

sideview.append(models.Sideview(
    content='<ul>'
	'<li><b>Kyle Dunn</b> worked at Rosemont School of the Holy Child as an IT administrator. </li>'
	'<li><b>Kristy Majetich</b> worked at NetApp working on a proxy application for their vCenter and vSphere '
	'Client.</li>'
	'<li><b>Taylor Clifton</b> worked at Google Inc. on the Gmail team designing a major test/mock application '
	'from the ground up, as well as designing and implementing the new search query parser.</li>'
	'<li><b>Karen Mui</b> worked at Heavy Inc. and her responsibilities included migrating email from Exchange to '
	'Gmail, auditing WordPress plugins, purchasing an SSL Certificate and working on the VPN setup.</li>'
	'<li><b>Mauro Mescia</b> worked at The Vanguard Group in the Information Systems department. He automated '
	'System Testing using Quicktest Professional Scripting and worked with SharePoint and InfoPath.</li>'
	'</ul>',
    title='Here are some of the jobs and internships CS majors have participated in over this past summer.',
    category='Summer Internships',
    active=0,
    image=sb_images[28]))

sideview.append(models.Sideview(
    content='Steve Castellotti graduated from Villanova University with a BSCS in 2000. Steve is the owner of '
    'Puzzlebox Productions LLC in San Francisco and the Technical Director at Eyemagnet Limited, also in San '
    'Francisco. His activities include advising or consulting on serious, innovative projects in his areas of '
    'interest (brain-computer interface, rapid prototyping, mobile applications, education, disruptive '
    'technologies), and working with nonprofits using innovation, particularly technology, to improve society. '
	'His previous experiences includes positions as a Principal Support Consultant at Rocom Wireless and Bulletin '
	'Wireless and a Systems Programmer at the University of Pennsylvania.',
    title='Steve Castellotti',
    category='Department Entreprenuers',
    active=0,
    image=sb_images[29]))

sideview.append(models.Sideview(
    content='Ben LeDonni graduated from Villanova University with a BSCS in 2002 and an MSCS in 2003. After '
    'graduating, Ben worked for Lockheed Martin in King of Prussia, where he was the lead developer on a team '
    'that developed and supported a Windows Application for a customer. He then began working for BrickSimple, '
    'a software development company, where he worked with Java, XML, Tomcat, MySQL and other technologies to '
    'develop web applications using cutting edge technology. Ben has also been conceptualizing, designing, '
    'developing and supporting websites on his own for the past three years. He decided to start his own LLC, '
    'Creative Multimedia Solutions, which focuses on developing web presences for companies that don\'t have a '
    'website or need one that is more up to date. It also provides network and PC support in and around the '
    'Northeast Philadelphia area.',
    title='Ben LeDonni, BSCS ’02, MSCS ’03, Owner at Creative Multimedia Solutions',
    category='Department Entreprenuers',
    active=0,
    image=sb_images[30]))

sideview.append(models.Sideview(
    content='John Keleher received his BS in Computer Science from Villanova University in 2002.  He went on '
    'to receive his MS in Computer Science from American University, where he achieved a perfect academic '
    'record focusing his research on the Web and Internet technologies.  Before finishing graduate school, '
    'he co-founded Benton Consulting, a software services firm.<br>John has been professionally and academically '
    'involved in the World Wide Web and consulting since 2000.  He has worked on strategy for high-tech companies '
    'in Silicon Valley with R.B.Webber & Co., developed web applications for one of the top 5 software service '
    'firms in the world, Accenture, and independently led Web initiatives for several small organizations both '
    'domestically and internationally.<br>After a few years of consulting, he found that he wanted to specialize '
    'in a particular Web technology.  In 2008, along with a few other colleagues, John became familiar with the '
    'lack of technology in the world of college athletics. It was then that he found his passion for solving the '
    'problem of coaches, athletic directors, and compliance officers.  He is driven to uncovering the challenges '
    'of each client, develop an understanding of what they need, and deliver the industry leading features of ARMS, '
    'Athletic Relationship Management Software.',
    title='John Keleher, BSCS ’02, Managing Director at ARMS College Athletics Software',
    category='Department Entreprenuers',
    active=0,
    image=sb_images[31]))

sideview.append(models.Sideview(
    content='William Loftus received his BSCS from Villanova University in 1985. He has worked twenty-seven years '
    'in the executive management and operations of advanced software solution providers, building three Inc. 500 '
    'companies; eventually selling two and helping lead a third company public. Mr. Loftus is now a Senior '
    'Executive and Managing Director of Accenture\'s Mission Services and all Army Programs but prior to Accenture, '
    'he was the President, CEO and Co-Founder of Gestalt, LLC, a leading provider of collaborative technology for '
    'governments and Fortune 500 customers acquired by Accenture in 2007.  Other positions he held include being the '
    'CEO of Breakaway Solutions, a publicly traded company which included Professional Services, Application Services, '
    'and Strategy Services and founder/CEO of WPL Laboratories, which was sold it to Breakaway Solutions in 1999.  '
    'Even before these two ventures, Mr. Loftus was a Manager of R&D at Unisys, where he managed DARPA-sponsored projects.'
    '<br>In addition to being a nationally recognized entrepreneur, he is also recognized as an accomplished author and '
    'technologist.  Besides playing a major role in the previously mentioned companies\' growth, Mr. Loftus has also '
    'consulted to numerous Fortune 500 and emerging companies as well as a number of investment bankers and venture '
    'capitalists.  He has coauthored numerous papers, IEEE standard P1430, and the best-selling textbook, '
    '"Java Software Solutions," which is currently used in over 400 universities world-wide to teach computer science '
    'using Java. He has also contributed to research in various areas.  Some of his numerous awards including a '
    'Special Achievement Award from DARPA, Philadelphia\'s 40 under 40 in 1999, and E&Y Entrepreneur of the Year award '
    'in 2004.',
    title='Bill Loftus, BSCS ’85, Senior Executive Managing Director at Accenture',
    category='Department Entreprenuers',
    active=0,
    image=sb_images[32]))

sideview.append(models.Sideview(
    content='When I graduated Villanova in 2005, I never knew the path that lay before me. I had a job with Lockheed '
    'Martin as a computer analyst as soon as I graduated. It is such a great company that I am with them still today. '
    'I am doing the things that I love. I work with computers every day and interact with so many great people. Who '
    'knew I would also go on to receive 2 Master degrees from Villanova, one in Technology Management and one in Computer '
    'Science. Even better, I am now teaching the night class for Data Structures and Algorithms, CSC 1051, the very '
    'class I took my own freshman year. I have moved past the mortgage stage and own a home in Glenside, PA with my '
    'husband. I look back on my years at Villanova with pride and happiness. Those years really helped me to prepare '
    'myself for the future.',
    title='Katie Richardson',
    category='Where Are They Now?',
    active=0,
    image=sb_images[33]))

sideview.append(models.Sideview(
    content='John Lamb graduated from Villanova in 1992, and received his masters in Computer Science in 2003.  Some '
    'words of advice he would offer to current students is, "Opportunity is always there, you just have to first be '
    'able to recognize it and then be able to seize it.  Remember that you can accomplish anything; you just have to '
    'want it bad enough. You need two things: capability and resolve, and if you have enough resolve you can get the '
    'capability." John Lamb is currently working on the Autonomous Aerial Refueling (AAR) project which is integrated '
    'with the Navy-Unmanned Combat Air System (N-UCAS).  Previously, Mr. Lamb has been a systems engineer on the Joint '
    'Precision Approach Landing System\'s Test and Evaluation System.  He has also worked for the US Government as a '
    'civil servant.  He was the Operation Systems Integration Team Lead at the Naval Air Warfare Center, Identification '
    'Systems Division, Processing and Displays Branch.  His team developed the AN/TPX-42 system which is the air traffic '
    'control system for the US Navy\'s aircraft carriers and amphibious carriers. In addition, he has recently started '
    'his own company, Lambda Technologies, LLC, writing video games.  Mr. Lamb says, "We at L-3 are trying to gain work '
    'assisting the US Government in architecting SOA systems to accommodate communications across multiple levels of '
    'security and varying levels of bandwidth.  We hope to leverage our relationship with Villanova in these efforts." '
    'In his free time, John Lamb enjoys sailing and has raced in the Governor\'s Cup a couple of times.  He is also '
	'currently the Emergency Services Officer for his local Civil Air Patrol squadron, and is a SCUBA diver.',
    title='John Lamb',
    category='Where Are They Now?',
    active=0,
    image=sb_images[34]))

sideview.append(models.Sideview(
    content='Edward J. McLaughlin III graduated from Villanova with a Computer Science degree in 1999. He recently '
    'told us "After graduating Villanova in 1999 I remained in the Philadelphia area.  I live with my wife and unborn '
    'child in Worcester, Pa located next to Valley Forge National Park.  For the past two and a half years, I have '
    'been working for the Health and Wellness division of Walgreens known as Take Care Health Systems.  Our division '
    'focuses on providing healthcare solutions to the public and private corporations in a cost efficient and convenient '
    'manner.  My role as a Senior Applications Developer is to architect, design, and implement web based software '
    'solutions.  The one thing I truly enjoy about my position is that I work with many facets of database and web '
    'based technologies.  This keeps my work interesting, and I wouldn\'t be where I am if it wasn\'t for the CSC '
    'program at Villanova which exposed me to the many areas of the industry.  I recently completed an online '
    'scheduling system for our patients where I was responsible for the database design of tables and stored procedures '
    'and a calendar interface built with .NET 4.0 and Silverlight 4.0 technologies.  At the same time, I also finished '
    'working on a project for the Walgreens store of tomorrow located within the Chicago area.  These stores were '
    'designed with multiple technologies including but not limited to the use of iPad and iTouch devices for mobile '
    'availability, new system kiosks for refilling prescriptions and registering for a visit with a Nurse Practitioner, '
    'and greater accessibility and availability of the Pharmacists."',
    title='Edward J. McLaughlin III',
    category='Where Are They Now?',
    active=0,
    image=sb_images[35]))

sideview.append(models.Sideview(
    content='John Fiedler received his BSCS from Villanova in 2005.<br>He says, "Since graduating from Villanova in '
    'the Spring of 2005, I moved to midtown Manhattan and began working at FOXNews.com.  I began as a Front End Web '
    'Developer and am currently a Senior Developer at the company.  My current role requires me to lead the '
    'development effort as we move from an outdated Vignette content management system to one built entirely '
    'in-house.  Our in-house solution is being constructed entirely with open-source, Java-based technologies.  '
    'The experience I gained at Villanova gave me an incredible advantage in order to lead the effort I am currently '
    'undertaking.  It has required not only a knowledge of programming, but also of system architecture, system '
    'administration, database structure, and networking.  In addition to this current role, other roles have allowed '
    'me to gain experience with some of the most cutting-edge tools and technologies.  It has been a very fulfilling '
    'ride thus far and I am thrilled to have had the opportunities to work on thrilling and engaging projects every '
    'single day."',
    title='John Fiedler',
    category='Where Are They Now?',
    active=0,
    image=sb_images[36]))

sideview.append(models.Sideview(
    content='James Ballow received his BSCS from Villanova in 2004.<br>He says, "After a paid internship as a junior '
    'web developer with SportingNews.com, I became a full-time front-end producer there. However, in May, 2007, '
    'rather than relocate to Charlotte, NC, I decided to search for a new job in the New York City area. Soon after, '
    'I became a PHP developer ( a web development language ) at CSTV.com, where I worked primarily on special projects. '
    'About a year later, though, CSTV became part of CBS Sports. Once again I found myself in a new role, and once '
    'again I preferred to seek a new job in sports media. I interviewed for two positions within ESPN and shortly '
    'thereafter received offers from both. I picked the one with ESPN Mobile and am now one of two lead developers for '
    'the mobile phone website. In the future I will potentially be working with both the iPhone and Google Android '
    'platforms.  I also plan on utilizing ESPN\'s mentoring program to help me plan out my career and assist me in my '
    'goal of receiving an MBA with a specialization in entertainment and media."',
    title='James Ballow',
    category='Where Are They Now?',
    active=0,
    image=sb_images[37]))

sideview.append(models.Sideview(
    content='Amy Roberge received her BSCS from Villanova in 2008.<br>She says, "I am currently living in Brighton, MA '
    '(right outside of Boston) and am working for Cisco Systems in Boxborough, MA.  When I\'m not at work, I like to '
    'spend time enjoying the great shopping and dining in downtown Boston.  Also, I love to go and cheer on all of the '
    'Boston sports teams - my particular favorite being watching the Red Sox play at Fenway Park! During the working '
    'hours, I spend my time focusing on a product called the Adaptive Security Appliance - a security appliance that '
    'does Firewall, VPN and IPS.  My title at Cisco is "Software Engineer", but my responsibilities mainly revolve '
    'around working with customers.  I do everything from helping customers with configuration issues, to fixing '
    'customer-found bugs, to managing our various beta test programs.  Cisco is a great place to work, and the people '
    'here have really made my transition from the "college world" to the "real world" a pleasant one.  I still can\'t '
    'help but miss Villanova though."',
    title='Amy Roberge',
    category='Where Are They Now?',
    active=0,
    image=sb_images[38]))

sideview.append(models.Sideview(
    content='Colleen McInerney received her BSCS from Villanova in 2008.<br>She says, "After graduating from Villanova '
    'in May 2008, I had planned to move back home and work in the Philadelphia area, but then I was presented with the '
    'opportunity to work in Washington, DC.  Although I was hesitant at first, I thought it would be a great experience. '
    'I started work with CareFirst BlueCross BlueShield in August as an Application Integration Specialist.  In the '
    'beginning I did documentation and became more familiar with the Software Development Lifecycle as well as the business '
    'world. Little by little I was given more responsibility in software development and testing. Within the next year I '
    'plan to be DBA (database administrator) certified. Villanova provided me with a great foundation for a fruitful career '
    'with computers and beyond."',
    title='Colleen McInerney',
    category='Where Are They Now?',
    active=0,
    image=sb_images[39]))

sideview.append(models.Sideview(
    content='Wendy Hillegass received her BSCS from Villanova in 2004.<br>She says, "After graduating from Villanova '
    '2004, I began my career at Vanguard, where I first worked in systems testing and was later happy to be offered a '
    'developer\'s position in a production support group. The downside of my new role was that I was then unable to '
    'matriculate as a master\'s student at the University of Pennsylvania, where I\'d been admitted in Computer and '
    'Information Science. However, I enjoyed improving my skills as a developer in my new role.<br>After three years '
    'at Vanguard, I moved to New York City, where I am currently working for Google as a Software Engineer on Google '
    'Checkout.  Here at Google I\'ve worked on the design and implementation of several projects, including Google '
    'Checkout for Non-Profits, recently launched.  While there are countless reasons why I love working here, it is '
    'projects like this, which have a significant positive impact on many people everywhere, that are most satisfying '
    'to me.  The projects I work on at Google are both challenging and interesting, not to mention that my dog gets to '
    'sit next to me in the office! "',
    title='Wendy Hillegass',
    category='Where Are They Now?',
    active=0,
    image=sb_images[40]))

sideview.append(models.Sideview(
    content='Karla Janet Castro Granja received her BSCS from Villanova in 2005.<br>She says, "I am a systems '
    'programmer at University of the Sciences in Philadelphia. Over the years I have become familiar with the '
    'infrastructures of our main databases: built in Unidata and Uniquery programming, SQL and Oracle Databases. '
    'I am capable of utilizing different reporting tools including Colleague Informer and Benefactor Informer to '
    'create reports and meet our client\'s requirements for information. Throughout the years I have acted as the '
    'lead as well as a team member in the implementation of new pieces of software on campus including Astra '
	'Schedule, Sedona, Maintenance Direct, Share Point, and Informer, which has given me a comprehensive understanding '
	'of these systems. This makes it easy for me to maintain and trouble shut problems when these systems fail to run '
	'effectively. I have gained the background in working with various systems/applications and supporting them from a '
	'technical (IT) perspective and from a user (front end perspective). I have also obtained skills in systems '
	'administration, and OS support, project management and gained strong communication skills. I lead a series of '
	'computer trainings oriented to staff and faculty members on campus. I teach our users how to navigate our '
	'computer systems."',
    title='Karla Ganja',
    category='Where Are They Now?',
    active=0,
    image=sb_images[41]))

sideview.append(models.Sideview(
    content='Melissa Corning received her BSCS from Villanova in 2008.<br>She says, "I\'ve been working since '
    'late 2008 at a company called MGame USA, a subsidiary of a Korean company that develops and produces '
    'free-to-play MMOGs (Massively Multiplayer Online Games), is the 5th largest gaming company in Korea, and '
    'has offices all over the world.  I\'ve been working as a project manager for "Scions of Fate" (known in '
    'Korea and Japan as "Yulgang"), a well-known title. As such, I get to do creative development, which '
	'means design events and content, as well as communicate with the player base to better understand its likes and '
	'dislikes.<br>Last year two of my coworkers and I were sent for several months to the main office in Seoul to '
	'work with the programming teams directly. It\'s a great city, and it was a wonderful experience!  The language '
	'barrier wasn\'t too bad, since many of my coworkers spoke English.  I also tried to learn a bit of Korean myself.  '
	'In fact, the biggest difference was the food.  There are only a few American chains, and standard Korean food is '
	'very spicy and tends to have different kinds of noodles, rice, and fish.  It was usually very good though, so it '
	'wasn\'t hard to adjust to. Since then a lot of things have been happening! Besides "Scions of Fate," I\'m now '
	'helping manage a new release, called "Cloud Nine." This includes designing features, planning events and preparing '
	'for an upcoming expansion. Other new MGame releases are planned as well.<br>Of course, there are always the '
	'"less fun" aspects including writing reports, investigating problems and monitoring revenue, but overall I\'m very '
	'happy with everything and excited about this year."',
    title='Melissa Corning',
    category='Where Are They Now?',
    active=0,
    image=sb_images[42]))

sideview.append(models.Sideview(
    content='Caroline Cassigneul received her BSCS from Villanova in 2001.<br>She says, "As I left Villanova, I found '
    'that many career opportunities were open to me.  After graduation, I had the option between two jobs.  I\'ve had '
    'many job offers since then, but I moved back to Pennsylvania to take one of the two original jobs.  I now work for '
    'IKEA as an Information Technology Manager in Training. I\'m a project manager, and am currently managing three '
    'different projects.  I plan, track and coordinate, follow up with team members, and make sure things are done on time."',
    title='Caroline Cassigneul',
    category='Where Are They Now?',
    active=0,
    image=sb_images[43]))

sideview.append(models.Sideview(
    content='Kallie Nordengren received a BSCS from Villanova in 2006, as well as a MSCS from Villanova in 2007. '
    '<br>She says of being a recent graduate, "As a recent graduate from Villanova, I moved back to my hometown '
    'in Massachusetts and began working for the MITRE Corporation.  In the short time since I\'ve been out of '
    'school, I attained the position of Senior Software Systems Engineer.  Each day, I work as a software consultant '
    'on multiple projects at a time with teams of people across the United States.  I constantly learn more in the '
    'field and expand on my knowledge that I gained at Villanova by doing development work through my company."',
    title='Kallie Nordengren',
    category='Where Are They Now?',
    active=0,
    image=sb_images[44]))

sideview.append(models.Sideview(
    content='Alison Lowery received her BSCS from Villanova in 1988 and later went on to receive her MSE from '
    'the University of Pennsylvania and her MMGT from Penn State University.<br>She shares her thoughts, "Computer '
    'science is an opportunity to make a difference in the success of your company at all levels.  Since graduating '
    'Villanova, I\'ve continued my education and received a MSE Computer Science degree (from the University of '
    'Pennsylvania) and a MMGT Management degree (from Penn State).  These days, I\'m working for Platform A, '
	'which is the Behavioral Targeting platform within AOL\'s online business arm, as a Vice President of Engineering.  '
	'I\'m accountable for product development customer service and support.   Computer Science is fun, challenging and '
	'can cause a great impact everywhere in the workplace." You can read more about what I do at http://www.tacoda.com/',
    title='Kallie Nordengren',
    category='Where Are They Now?',
    active=0,
    image=sb_images[45]))

sideview.append(models.Sideview(
    content='Caroline Scales received her BSCS from  Villanova in 1987.<br>She talks about life after college and '
    'says, "Upon graduation of Villanova, I spent a few weeks abroad bicycling through Europe.  After that, however, '
    'I settled down and began working as a contractor doing system test at AT&T. Since then, I\'ve worked for various '
    'parts of the company, always using my degree to its full advantage.  These days, I am responsible for the creation, '
    'launch, results reporting and overall quality for business marking outbound email campaigns at AT&T.  Through my '
    'company, I am able to telecommute, and work out of a virtual office.  In addition to being able to use my degree '
    'everyday in the workplace, I\'m also able to use what I learned at Villanova in my personal life, for I now maintain '
    'the Habitat for Humanity website for our local affiliate as well as help maintain the small marketing database used '
    'to track donations at my children\'s school."',
    title='Caroline Scales',
    category='Where Are They Now?',
    active=0,
    image=sb_images[46]))

sideview.append(models.Sideview(
    content='Candice Goglio received her BSCS from Villanova in 1987 and went on to earn her MBA from Long Island University '
    'in 1996.<br>She says, "Computer science has changed so much from the time I went to Villanova to the current day, and '
    'I only wish I could take it now.  It must be so exciting, challenging and rewarding!  Since attending Villanova, I\'ve '
    'held a career in Finance and then in Client Service Management.  Villanova was a great school when I attended, and it\'s '
    'an even better school now.  Students are really encouraged to \'give it all you\'ve got\', my orientation slogan from '
    'freshman year."',
    title='Candice Goglio',
    category='Where Are They Now?',
    active=0,
    image=sb_images[47]))

sideview.append(models.Sideview(
    content='<ul>'
	'<li><b>AJ Palkovic</b> will be working at Fog Creek Software in New York. This company is run by Joel Spolsky, the man '
	'behind the well known blog: joelonsoftware.com. </li>'
	'<li><b>Victoria Suwardiman</b> is participating in the CRA-W program - Distributed Research Experience for Undergraduates. '
	'She will work with Dr. Julie Kientz at the University of Washington. Dr. Kientz has particular interests in technology '
	'and health/education. </li>'
	'<li><b>Kory Kirk</b> and <b>Kevin Berry</b> will both participate in Google\'s <a href="http://code.google.com/soc/">Summer '
	'of Code</a> program. This well known program offers student developers stipends to write code for various open source '
	'software projects.</li>'
	'<li><b>Kurt Lehmer</b> will work on a a robotics research project headed by Dr. Peyton-Jones of the CPE department here '
	'at Villanova. The results of his efforts might be seen in Dr. Klassner\'s robotics class in the fall.</li>'
	'<li><b>Greg Francis</b> will be interning with JPMorgan Chase Wilmington, DE as a Technology Analyst. He will work on '
	'application development related to business analysis, as part of a technology team.</li>'
	'<li><b>Casey Burkhardt</b> will be working as a Software Engineering Intern at Google Headquarters in Mountain View, '
	'California with T.V. Raman\'s accessibility research team and the Android team to improve the accessibility of '
	'Google\'s mobile platform.</li>'
	'<li><b>Taylor Clifton</b> will be interning at the Jet Propulsion Laboratory at Cal Tech.</li>'
	'<li><b>Chris Miller</b> has an internship with Motorola in Horsham, PA this summer. His job is as a Business Analyst '
	'and he will be working with the assimilation of smaller companies purchased by Motorola and assessing their '
	'technological standards.</li>'
	'<li><b>Michael Dokas</b> will be working at Goldman Sach in Operations.</li>'
	'<li><b>Ankit Patel</b> will work with Dr. Cassel this summer at Villanova on the Ensemble web portal project.</li>'
	'<li><b>Zach Horst</b> will be at the New York Stock Exchange as an IT intern analyst, working on a solo project creating '
	'gadgets and apps for the brokers and traders on the floor.</li>'
	'<li><b>Zachary Fanelle</b> plans to work with the IS department at South Jersey Healthcare System.</li>'
	'<li><b>Nicholas Burns</b> will be working for Computer Sciences Corporation at Sikorsky Aircraft.</li>'
	'</ul>',
    title='Here are some of the many interesting jobs and/or internships that CS majors have planned for the upcoming summer.',
    category='Summer Internships',
    active=0,
    image=sb_images[48]))

sideview.append(models.Sideview(
    content='Jason Dobies, known as "Jay" or "General", graduated from Villanova as a Computer Science and Mathematics major '
    'in 2001. During his junior and senior years he interned with Lockheed Martin as a visual basic programmer. After graduating '
    'from Villanova he worked for five different companies within five years. For the past four years however, he has settled '
    'in with Red Hat as a senior software engineer. He enjoys this job because of the freedom it provides as well as the pride '
    'that the company has in its workers. Red Hat makes open source software easier to use for other major corporations. While '
    'working for Red Hat, Jay realized how much he wanted to help other people. He believes that teaching is a great way to '
    'fulfill that ambition. After earning Masters in Software Engineering from Drexel University he applied to teach at Villanova. '
    'In the Spring of 2008 he started teaching Data Structures and Algorithms II. He is able to incorporate real world examples '
    'that he sees day to day in his work at Red Hat into his classroom. He also supplies the students with personal advice on '
    'surviving college and choosing a job or internship. Jay is happily married to his wife (duh), whom he met during his '
    'junior year at Villanova (they were married in the Villanova Church). They are currently living in New Jersey with their '
    'two-year old daughter. If you ever need a good laugh or advice, you can catch him on campus on Tuesdays and Thursdays, '
    'usually sitting in the Connelly Center.',
    title='Jason Dobies',
    category='Where Are They Now?',
    active=0,
    image=sb_images[49]))



### POPULATE DATABASE ###

for i in sb_images:
	db.session.add(i)

for i in sideview:
	db.session.add(i)

db.session.commit()