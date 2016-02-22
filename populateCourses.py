from app import db, models
import datetime

courses = []

courses.append(models.Course(course = 'CSC 1010',
							department = 'Computing Sciences',
							title = 'Programming for All',
							credits = 3,
							level = 'nonmajor',
							description = 'A unified view of the powerful tools for '
							'manipulating text and the algorithms they implement; '
							'complexity and security of operations on text; locating '
							'and searching online text databases and bibliographies via '
							'the Internet; alternative text structures: hypertext, '
							'multimedia; alternative input techniques: scanning, voice.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 1020',
							department = 'Computing Sciences',
							title = 'Computing and the Web',
							credits = 3,
							level = 'nonmajor',
							description = 'Information representation and manipulation; '
							'file systems and directories; compatibility and data '
							'exchange; security and privacy; elements of computer '
							'architectures and operating systems; computer networks, '
							'the Internet, and the World Wide Web; web site design '
							'principles and creation; PC based examples and illustrations.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 1024',
							department = 'Computing Sciences',
							title = 'Computing for Scientists',
							credits = 1,
							level = 'nonmajor',
							description = 'Active learning of computing skills necessary '
							'for scientists: datagraphing, regression analysis, animation, '
							'symbolic computing, information search techniques, scientific '
							'report writing, web page construction, fundamentals of programming.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 1051',
							department = 'Computing Sciences',
							title = 'Algorithms and Data Structures I',
							credits = 4,
							level = 'crossover',
							description = 'Algorithm design and programming fundamentals: data, '
							'variables, selection, loops, arrays, input/output; basic graphics '
							'and graphical user interfaces; object-oriented design: objects, '
							'classes, methods, encapsulation;',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 1800',
							department = 'Computing Sciences',
							title = 'Organization of Programming Languages',
							credits = 3,
							level = 'undergraduate',
							description = 'High level language features: data types, control '
							'structures; formal lexical and syntactical analysis; operational '
							'semantics; language translation.',
							prerequisites = 'CSC 1052 and CSC 1300'))

courses.append(models.Course(course = 'CSC 2500',
							department = 'Computing Sciences',
							title = 'Survey of Information Science',
							credits = 3,
							level = 'undergraduate',
							description = 'Brief introductions to several areas in which '
							'problems in information use are important. Examples are business, '
							'law, biology, medicine, electronic commerce, and libraries.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 3400',
							department = 'Computing Sciences',
							title = 'Information Retrieval',
							credits = 3,
							level = 'undergraduate',
							description = 'Theory and practice of location, organization, '
							'and rendering of meaningful content from largely unorganized sources.',
							prerequisites = 'CSC 1052 and CSC 1300'))

courses.append(models.Course(course = 'CSC 4140',
							department = 'Computing Sciences',
							title = 'Theory of Information',
							credits = 3,
							level = 'undergraduate',
							description = 'Information and coding theory, data compression, cryptology.',
							prerequisites = 'CSC 1300'))

courses.append(models.Course(course = 'CSC 4181',
							department = 'Computing Sciences',
							title = 'Compiler Construction',
							credits = 3,
							level = 'undergraduate',
							description = 'Lexical and syntactical analysis; code generation; error '
							'recovery; recursive descent compilation; handling a run time environment.',
							prerequisites = 'CSC 1600 or CSC 2405'))

courses.append(models.Course(course = 'CSC 4300',
							department = 'Computing Sciences',
							title = 'Computer Graphics',
							credits = 3,
							level = 'undergraduate',
							description = 'Hardware and software systems in computer graphics, graphics '
							'programming languages, (PHIGS, VRML), modeling in 3D, development of '
							'interactive software, animation.',
							prerequisites = 'CSC 2405'))

courses.append(models.Course(course = 'CSC 4380',
							department = 'Computing Sciences',
							title = 'Information Visualization',
							credits = 3,
							level = 'undergraduate',
							description = 'The presentation of information; visual cognition, scientific '
							'visualization, illustration presentation, color theory, motion dynamics, '
							'image processing.',
							prerequisites = 'CSC 1052'))

courses.append(models.Course(course = 'CSC 4480',
							department = 'Computing Sciences',
							title = 'Principles of Database Systems',
							credits = 3,
							level = 'undergraduate',
							description = 'Concepts and technology of database management systems and '
							'data modeling with an emphasis on the relational model; database querying '
							'and normalization; physical data organization.',
							prerequisites = 'CSC 1051 and CSC 1300'))

courses.append(models.Course(course = 'CSC 4500',
							department = 'Computing Sciences',
							title = 'Artificial Intelligence',
							credits = 3,
							level = 'undergraduate',
							description = 'The nature of intelligence and the question of its computer '
							'implementation; search algorithms; knowledge representation; automated '
							'deduction; natural language understanding; planning; problem solving.',
							prerequisites = 'CSC 2053'))

courses.append(models.Course(course = 'CSC 4630',
							department = 'Computing Sciences',
							title = 'Software Development and Systems',
							credits = 3,
							level = 'undergraduate',
							description = 'Operating system structures; system calls; system libraries; '
							'interprocess communication; user-interface programming environments; '
							'software utilities; software portability.',
							prerequisites = 'CSC 2405 or CSC 1600'))

courses.append(models.Course(course = 'CSC 4730',
							department = 'Computing Sciences',
							title = 'Human Computer Interaction',
							credits = 3,
							level = 'undergraduate',
							description = 'Design of the user/system interface; measurement of human-computer '
							'interaction; models of the user and user communities; design criteria for the '
							'interface; user interface management systems (UIMS); test and evaluation '
							'strategies and tools.',
							prerequisites = 'CSC 1052 and (MAT 2310 or MAT 4310)'))

courses.append(models.Course(course = 'CSC 4800',
							department = 'Computing Sciences',
							title = 'Web Application Development',
							credits = 3,
							level = 'undergraduate',
							description = 'Theory and design of web-based applications: stylesheets, applets, '
							'HTML, CGI programming, web server design, web site design, security, multimedia '
							'representations, encryption, compression.',
							prerequisites = 'CSC 1052'))

courses.append(models.Course(course = 'CSC 4900',
							department = 'Computing Sciences',
							title = 'Computer Networks',
							credits = 3,
							level = 'undergraduate',
							description = 'Underlying principles of computer networks; OSI and TCP/IP '
							'architecture; LAN technologies; interconnecting devices: hubs, bridges, switches, '
							'routers, gateways; IP addressing and forwarding; routing protocols; transport '
							'protocols: error, flow, and congestion control; client-server communication; '
							'authentication and authorization; security threats and solutions.',
							prerequisites = 'CSC 2400'))

courses.append(models.Course(course = 'CSC 5930',
							department = 'Computing Sciences',
							title = 'Topics in Computer Science',
							credits = 3,
							level = 'crossover',
							description = 'Lecture presentation of selected topics in computer science. '
							'May be repeated for credit if topics are different.',
							prerequisites = 'Varies with the topic'))

courses.append(models.Course(course = 'CSC 3070',
							department = 'Computing Sciences',
							title = 'Emerging Technology Trends',
							credits = 3,
							level = 'crossover',
							description = 'Investigate new technologies and current applications. Explore '
							'when and how to apply new technologies with sensitivity to feasibility, '
							'financial viability, and overall effectiveness. Culminates in team-driven '
							'exploitation of a new technology.',
							prerequisites = 'Junior Standing'))

courses.append(models.Course(course = 'CSC 7000',
							department = 'Computing Sciences',
							title = 'Algorithms and Programming',
							credits = 3,
							level = 'graduate',
							description = 'Algorithm design and refinement; loop and selection control; '
							'recursion; arrays, pointers, records and strings; abstract data types: linked '
							'lists, stacks, queues, binary trees, elementary searching and sorting.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 7100',
							department = 'Computing Sciences',
							title = 'Computer Systems',
							credits = 3,
							level = 'graduate',
							description = 'Fundamental concepts in computer architecture and operating '
							'systems. Information representation, gates and digital logic, ALU and central '
							'processing organization, instruction sets, basics of pipelining, processes, '
							'memory management and file systems.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8301',
							department = 'Computing Sciences',
							title = 'Design and Analysis of Algorithms',
							credits = 3,
							level = 'graduate',
							description = 'Fundamental strategies for algorithm design; mathematical and '
							'empirical techniques for analysis of nonrecursive and recursive algorithms, '
							'with applications such as sorting, searching, string processing and graphs; '
							'NP-complete problems and approximation algorithms.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8310',
							department = 'Computing Sciences',
							title = 'Linguistics of Programming Languages',
							credits = 3,
							level = 'graduate',
							description = 'Organization, characteristics, constructs and design principles '
							'of programming languages; syntax, semantics, and pragmatics; language '
							'implementation issues; different programming paradigms such as imperative, '
							'functional, object-oriented, and logic programming.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8400',
							department = 'Computing Sciences',
							title = 'Computer Systems',
							credits = 3,
							level = 'graduate',
							description = 'Study of computing systems from the point of view of the '
							'programmer.  Topics include information representation, processor '
							'architecture, computer performance, storage management, security and '
							'concurrent programming.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8000',
							department = 'Computing Sciences',
							title = 'Foundations of Algorithms and Data Structures',
							credits = 3,
							level = 'graduate',
							description = 'Programming in Java or another object-oriented language. '
							'Program design with an emphasis on the object paradigm. Classic algorithms '
							'and data structures. Significant programming assignments are required.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8410',
							department = 'Computing Sciences',
							title = 'Operating Systems Concepts',
							credits = 3,
							level = 'graduate',
							description = 'Principles and techniques required for creating and understanding '
							'operating systems, including the areas of: system services, concurrent programming, '
							'process and resource control; deadlock detection, recovery, and prevention; memory '
							'management; file systems; protection and security.',
							prerequisites = 'CSC 8400'))

courses.append(models.Course(course = 'CSC 8470',
							department = 'Computing Sciences',
							title = 'Computer Graphics',
							credits = 3,
							level = 'graduate',
							description = 'Interactive program development in 2D/3D graphics; event handling, '
							'real-time data sampling, and strategies in programming computer games; 2D/3D '
							'modeling; perspective viewing; object transformation; graphical user interface '
							'design.',
							prerequisites = 'CSC 8301'))

courses.append(models.Course(course = 'CSC 8490',
							department = 'Computing Sciences',
							title = 'Database Systems',
							credits = 3,
							level = 'graduate',
							description = 'Architecture of a database system; conceptual and implementation '
							'models; query languages, design theory; integrity, security, and concurrency; '
							'discussion of some commercial systems.',
							prerequisites = 'CSC 8301 and CSC 8410'))

courses.append(models.Course(course = 'CSC 8510',
							department = 'Computing Sciences',
							title = 'Theory of Computability',
							credits = 3,
							level = 'graduate',
							description = 'Automata theory: deterministic and non-deterministic finite '
							'automata, pushdown automata, regular languages, context-free grammars, '
							'pumping lemma. Computability and recursion theory; Turing machines and '
							'their variations, decidability and recursive enumerability, mapping '
							'reducibility and Turing reducibility, undecidability of the halting problem, '
							'logical theories and Godel\'s incompleteness theorem. Complexity theory: time '
							'complexity, space complexity, major open problems on computational complexity.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8530',
							department = 'Computing Sciences',
							title = 'Distributed Systems',
							credits = 3,
							level = 'graduate',
							description = 'An introduction to distributed systems; distributed system '
							'architecture and design goals; networks and distributed protocols; '
							'distributed/network operating systems, including distributed resource '
							'control and management, concurrency and interprocess communication; remote '
							'procedure calling; client/server techniques and issues; reliability of '
							'distributed systems; security and authentication.',
							prerequisites = 'CSC 8301 and CSC 8410'))

courses.append(models.Course(course = 'CSC 8540',
							department = 'Computing Sciences',
							title = 'Software Engineering',
							credits = 3,
							level = 'graduate',
							description = 'An introduction to software engineering covering development '
							'life-cycle models, requirements analysis and specification, design concepts '
							'and methods, testing, maintenance, CASE tools and management concerns. '
							'Additional topics may include reuse, metrics, experimentation, reengineering, '
							'development environments, and standards. The student may be required to write '
							'a research paper and/or give an in-class presentation.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8560',
							department = 'Computing Sciences',
							title = 'Computer Networks',
							credits = 3,
							level = 'graduate',
							description = 'Computer networks as an application development platform; '
							'services required by and provided to distributed applications; electronic '
							'mail systems enhancement; access to remote file systems; integration of '
							'remote resources such as components of the Web into applications; security; '
							'data compression and encryption; transport protocols; network addressing and '
							'routing; LAN and MAN medium access control; bridging; Wireless and mobile '
							'networking; evolution of network technology on the Internet, Multi-media '
							'protocols.',
							prerequisites = 'CSC 8301 and CSC 8410'))

courses.append(models.Course(course = 'CSC 8580',
							department = 'Computing Sciences',
							title = 'Network Management and Performance',
							credits = 3,
							level = 'graduate',
							description = 'Monitoring and management of computer networks and network '
							'services; SNMP, CMIS, CMIP network management protocols and services; '
							'Management Informtion Base (MIB) development; performance analysis including '
							'queuing models; comparison of channel access protocols; other related topics '
							'as selected by the class. This course is frequently run as a seminar requiring '
							'a significant paper or project, consistent class preparation and participation.',
							prerequisites = 'CSC 8530 and CSC 8560'))

courses.append(models.Course(course = 'CSC 8600',
							department = 'Computing Sciences',
							title = 'Object-Oriented Design and Programming',
							credits = 3,
							level = 'graduate',
							description = 'Introduces the theoretical and practical issues underlying the '
							'object-oriented paradigm, including classes, encapsulation, inheritance and '
							'polymorphism. Primary topics also include object-oriented analysis and design, '
							'databases and technology transfer. The use of an object-oriented programming '
							'language, such as Java or C++, is an integral part of the course. Problems '
							'involving program design and implementation will be assigned. The student may '
							'be required to write a research paper and/or give an in-class presentation.',
							prerequisites = 'CSC 8301 and CSC 8410'))

courses.append(models.Course(course = 'CSC 8700',
							department = 'Computing Sciences',
							title = 'System Programming in UNIX and C',
							credits = 3,
							level = 'graduate',
							description = 'The UNIX operating system: command interpreters, shell programming, '
							'process structure, file system, utilities like grep, sed, awk, and perl. C '
							'programming: file processing, libraries, program environment, system calls.',
							prerequisites = 'CSC 8301 and CSC 8410'))

courses.append(models.Course(course = 'CSC 8800',
							department = 'Computing Sciences',
							title = 'Applied Computer Science I',
							credits = 3,
							level = 'graduate',
							description = 'Mathematical analysis, probability, statistics, optimization, '
							'queuing theory, digital signal processing; software engineering; UNIX, C, C++.',
							prerequisites = 'Permission of Instructor'))

courses.append(models.Course(course = 'CSC 8820',
							department = 'Computing Sciences',
							title = 'Applied Computer Science III',
							credits = 3,
							level = 'graduate',
							description = 'Client-user services; computer networking; communications link '
							'dynamics; astrodynamics.',
							prerequisites = 'CSC 8810'))

courses.append(models.Course(course = 'CSC 9010',
							department = 'Computing Sciences',
							title = 'Special Topics',
							credits = 3,
							level = 'graduate',
							description = 'Advanced elective study of topics of current interest and '
							'importance in the computer field. May be repeated for credit if topics '
							'are different.',
							prerequisites = 'Varies with the topic'))

courses.append(models.Course(course = 'CSC 9080',
							department = 'Computing Sciences',
							title = 'Thesis Continuation',
							credits = 0,
							level = 'graduate',
							description = 'Continuation beyond the first semester for students who '
							'have registered for the thesis (CSC 9030).',
							prerequisites = 'CSC 9030'))

courses.append(models.Course(course = 'CSC 1030',
							department = 'Computing Sciences',
							title = 'Problem Solving with Computers',
							credits = 3,
							level = 'nonmajor',
							description = 'Using the microcomputer as a problem solving tool; system '
							'use; general purpose language programming; spreadsheet analysis and '
							'modeling; retrieving information from the Internet; strengths and weaknesses '
							'of computer based problem solutions.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 1040',
							department = 'Computing Sciences',
							title = 'Computing with Images',
							credits = 3,
							level = 'nonmajor',
							description = 'Image processing as an introduction to broader computing concepts; '
							'computational approaches to image processing and representation; multimedia tools.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'PHY 2601',
							department = 'Physics',
							title = 'Computational Phy Lab I',
							credits = 3,
							level = 'crossover',
							description = 'Computational Physics',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 1052',
							department = 'Computing Sciences',
							title = 'Algorithms and Data Structures II',
							credits = 4,
							level = 'undergraduate',
							description = 'Object-oriented design: inheritance, interfaces, polymorphism; problem '
							'analysis; recursion; abstract data types; dynamically linked structures; linear data '
							'structures: stacks, queues, lists, vectors; sorting and searching; event-driven '
							'programming; graphical user interfaces.',
							prerequisites = 'CSC 1051 or ECE 1620'))

courses.append(models.Course(course = 'CSC 9000',
							department = 'Computing Sciences',
							title = 'Guided Study',
							credits = 3,
							level = 'graduate',
							description = 'Faculty directed study for one or a small number of students on a topic '
							'of mutual interest. Requires permission of the faculty sponsor and the director of '
							'the graduate program.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 1300',
							department = 'Computing Sciences',
							title = 'Discrete Structures',
							credits = 3,
							level = 'undergraduate',
							description = 'Mathematical concepts that support computer science: sets, functions, '
							'relations, combinatorics, recurrences, boolean logic, mathematical proofs, matrices, '
							'graphs and trees.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 1600',
							department = 'Computing Sciences',
							title = 'Operating Systems',
							credits = 3,
							level = 'undergraduate',
							description = 'System software design and implementation; process and resource '
							'management; concurrency, scheduling, and deadlock; memory management; file systems '
							'and security.',
							prerequisites = 'CSC 2400 or ECE 2042'))

courses.append(models.Course(course = 'CSC 1700',
							department = 'Computing Sciences',
							title = 'Analysis of Algorithms',
							credits = 3,
							level = 'undergraduate',
							description = 'Efficiency classifications and mathematical analysis of recursive '
							'and nonrecursive algorithms. Major algorithm design techniques: brute force, '
							'divide-and-conquer, decrease-and-conquer, transform-and-conquer, space and time '
							'tradeoffs, greedy approach, dynamic programming, backtracking and branch-and-bound. '
							'Introduction to NP-completeness, approximation algorithms. Applications to a wide '
							'variety of computational problems: sorting, searching, string processing, graphs, '
							'arithmetic, linear algebra.',
							prerequisites = 'CSC 2053'))

courses.append(models.Course(course = 'CSC 2053',
							department = 'Computing Sciences',
							title = 'Platform Based Computing',
							credits = 3,
							level = 'undergraduate',
							description = 'Course is project driven . Topics include identifying platform '
							'facilities and constraints, event driven programming, MVC pattern, client/server '
							'considerations, security-performance-accessibility issues, web/mobile programming, '
							'and application programmer interfaces.',
							prerequisites = 'CSC 1052'))

courses.append(models.Course(course = 'CSC 2993',
							department = 'Computing Sciences',
							title = 'Internship in Computing',
							credits = 3,
							level = 'undergraduate',
							description = 'Internship in computer science open to second semester sophomores '
							'and above. Most likely, intern will participate in computer system development, '
							'maintenance, or evaluation in an environment which supports sound software '
							'engineering techniques.',
							prerequisites = 'Junior standing and 3.0 overall GPA'))

courses.append(models.Course(course = 'ECE 8471',
							department = 'Electrical and Computer Engineering',
							title = 'Software Reliability',
							credits = 3,
							level = 'graduate',
							description = 'Introduction to concepts of software reliability within the context '
							'of software systems development. The course will be useful to managers who require '
							'a broad understanding of the topic as well as to software designers, programmers and '
							'testers who may need to apply these concepts in detail. Topics: a selection of '
							'classical software reliability models. In addition, some of the broader issues '
							'impacting software reliability, such as software design and testing, will be studied.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'ECE 8429',
							department = 'Electrical and Computer Engineering',
							title = 'Topics in Intelligent Systems',
							credits = 3,
							level = 'graduate',
							description = ' ',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 4170',
							department = 'Computing Sciences',
							title = 'Theory of Computation',
							credits = 3,
							level = 'undergraduate',
							description = 'Finite automata and regular expressions; push down automata and '
							'context-free grammars; Turing machines; Church\'s thesis; computability; '
							'NP-completeness.',
							prerequisites = 'CSC 1700'))

courses.append(models.Course(course = 'CSC 4200',
							department = 'Computing Sciences',
							title = 'Advanced Algorithms and Complexity',
							credits = 3,
							level = 'undergraduate',
							description = 'Greedy algorithms, divide-and-conquer; dynamic programming; '
							'backtracking; branch-and-bound; linear and integer programming; Fast Fourier '
							'Transforms; probabilistic algorithms; NP-complete problems and approximation '
							'methods.',
							prerequisites = 'CSC 1700'))

courses.append(models.Course(course = 'CSC 4280',
							department = 'Computing Sciences',
							title = 'Parallel Algorithms and Architecture',
							credits = 3,
							level = 'undergraduate',
							description = 'Design and analysis of parallel algorithms for arithmetic, matrix '
							'operations, sorting, simulation, combinatorial and graph problems, and Fast Fourier '
							'Transforms; taxonomies of parallel architectures; interconnection networks, meshes, '
							'trees, and hypercubes; scalability and speed-up.',
							prerequisites = 'CSC 1700 and CSC 2405'))

courses.append(models.Course(course = 'CSC 4490',
							department = 'Computing Sciences',
							title = 'Data Warehousing and Mining',
							credits = 3,
							level = 'undergraduate',
							description = 'Tools and techniques, theory and practice for storage and effective '
							'use of massive data sets.',
							prerequisites = 'CSC 4480 and (CSC 2300 or MAT 2310 or MAT 4310)'))

courses.append(models.Course(course = 'CSC 4550',
							department = 'Computing Sciences',
							title = 'Expert and Knowledge Systems',
							credits = 3,
							level = 'undergraduate',
							description = 'Knowledge representation, uncertainty, automated knowledge acquisition, '
							'practical aspects of implementing expert systems.',
							prerequisites = 'CSC 1051'))

courses.append(models.Course(course = 'CSC 4600',
							department = 'Computing Sciences',
							title = 'Distributed Processing Systems',
							credits = 3,
							level = 'undergraduate',
							description = 'Data concurrency; distributed file systems and databases; distributed '
							'operating systems; security; interprocess communication; directory services; process '
							'migration; process vulnerability to partial failure.',
							prerequisites = 'CSC 2405'))

courses.append(models.Course(course = 'CSC 4700',
							department = 'Computing Sciences',
							title = 'Software Engineering',
							credits = 3,
							level = 'undergraduate',
							description = 'Management and production of software systems; the software life cycle; '
							'software design techniques and methodologies; participation in a team software '
							'development project.',
							prerequisites = 'CSC 1052'))

courses.append(models.Course(course = 'CSC 4790',
							department = 'Computing Sciences',
							title = 'Senior Projects',
							credits = 3,
							level = 'undergraduate',
							description = 'Capstone course centered around a semester long software development '
							'or research project; project planning; requirements elicitation and specification; '
							'teamwork; oral presentations required of all students.',
							prerequisites = 'CSC 4700'))

courses.append(models.Course(course = 'CSC 5900',
							department = 'Computing Sciences',
							title = 'Seminar in Computing',
							credits = 3,
							level = 'undergraduate',
							description = 'Study and discussion of selected topics in computing with presentations '
							'by individual students. May be repeated for credit if topics are different.',
							prerequisites = 'Varies with the topic'))

courses.append(models.Course(course = 'CSC 5940',
							department = 'Computing Sciences',
							title = 'Topics in Information Science',
							credits = 3,
							level = 'undergraduate',
							description = 'Lecture presentation of selected topics in information science. May be '
							'repeated for credit if topics are different.',
							prerequisites = 'Varies with the topic'))

courses.append(models.Course(course = 'CSC 5993',
							department = 'Computing Sciences',
							title = 'Independent Study',
							credits = 3,
							level = 'undergraduate',
							description = 'Reading, research and/or projects in a selected area of computer '
							'science under the direction of a member of the staff. May be repeated for credit.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8810',
							department = 'Computing Sciences',
							title = 'Applied Computer Science II',
							credits = 3,
							level = 'graduate',
							description = 'Software engineering: object-oriented analysis and design, database '
							'management, graphical user interfaces, system engineering.',
							prerequisites = 'CSC 8800'))

courses.append(models.Course(course = 'CSC 8100',
							department = 'Computing Sciences',
							title = 'Technology for Human Organizations',
							credits = 3,
							level = 'graduate',
							description = 'Leading-edge technologies and their applications in a variety of '
							'organzational settings. Presumes literacy in basic computer applications: word '
							'processing, desktop publishing, spreadsheets and communications.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8500',
							department = 'Computing Sciences',
							title = 'Formal Grammars and Programming Language Theory',
							credits = 3,
							level = 'graduate',
							description = 'Machines; nondeterminism; simulation; finite machines and regular '
							'languages; grammars; stack, counter, and tape machines; computability.',
							prerequisites = 'CSC 8301 and CSC 8310'))

courses.append(models.Course(course = 'CSC 8505',
							department = 'Computing Sciences',
							title = 'Compiler Construction',
							credits = 3,
							level = 'graduate',
							description = 'Finite state methods for lexical and syntactical analysis; '
							'symbol-table construction, run-time code organization for block-structured '
							'languages, intermediate code generation, and pseudo-object machines; LR(k) and '
							'LL(k) parsers. Programming assignments and exercises are given.',
							prerequisites = 'CSC 8301 and CSC 8310'))

courses.append(models.Course(course = 'CSC 8520',
							department = 'Computing Sciences',
							title = 'Artificial Intelligence',
							credits = 3,
							level = 'graduate',
							description = 'Problem-solving methods; knowledge representation; search; '
							'predicate calculus; automated theorem proving; natural language processing.',
							prerequisites = 'CSC 8301'))

courses.append(models.Course(course = 'CSC 8550',
							department = 'Computing Sciences',
							title = 'Concepts of Data Communications',
							credits = 3,
							level = 'graduate',
							description = 'Analog and digital transmission; media; communication channels; '
							'digital IDN carriers: T1, T3, SONET. Asynchronous and synchronous transmission; '
							'link protocols; multiplexing; switching: circuit and packet; voice and data '
							'PBXs; X.25, frame relay, ATM, ISDN; local area networks; OSI model; routing '
							'and transport; management.',
							prerequisites = 'CSC 8400'))

courses.append(models.Course(course = 'CSC 8570',
							department = 'Computing Sciences',
							title = 'User/System Interface Design',
							credits = 3,
							level = 'graduate',
							description = 'The design and measurement of human-computer interfaces, with '
							'the objectives of developing models of user communities, summarizing current '
							'research in user-oriented design, defining design criteria for the user/system '
							'interface, and constructing test strategies for interactive software systems.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8590',
							department = 'Computing Sciences',
							title = 'Advanced Software Engineering',
							credits = 3,
							level = 'graduate',
							description = 'In-depth coverage of software engineering topics such as: resue, '
							'metrics, CASE tools, design methodologies, reengineering, experimentation, '
							'automatic programming, software safety, development environments, reliability '
							'theory, risk management, and standards. The student may be required to write a '
							'research paper and/or give an in-class presentation.',
							prerequisites = 'CSC 8540'))

courses.append(models.Course(course = 'CSC 8610',
							department = 'Computing Sciences',
							title = 'Multimedia Technology',
							credits = 3,
							level = 'graduate',
							description = 'Theory and practice of multimedia content, representation, '
							'compression, storage, and delivery. Content types include text, audio, images, '
							'graphics, animations, and video. Student projects and presentations are generally '
							'an integral part of the course.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8710',
							department = 'Computing Sciences',
							title = 'Advanced System Programming',
							credits = 3,
							level = 'graduate',
							description = 'The UNIX kernel: architecture, inodes, process control, memory '
							'management, I/O subsystem. System calls in C: execution environment, memory '
							'management, terminal control, locking, file management, process management, '
							'interprocess communication. C ibraries. Program development and debugging tools.',
							prerequisites = 'CSC 8700'))

courses.append(models.Course(course = 'CSC 8720',
							department = 'Computing Sciences',
							title = 'System Administration Concepts',
							credits = 3,
							level = 'graduate',
							description = 'UNIX login process. Standard root, device and user directories and '
							'files. File system construction and management. Disk status and partitions. '
							'Monitoring system performance. Networking and communication.',
							prerequisites = 'CSC 8700'))

courses.append(models.Course(course = 'CSC 8750',
							department = 'Computing Sciences',
							title = 'Expert Systems',
							credits = 3,
							level = 'graduate',
							description = 'Knowledge representation and reasoning techniques; forward and '
							'backward chaining; semantic net and frame systems; uncertainty, automated knowledge '
							'acquisition; practical guidelines for implementing expert systems.',
							prerequisites = 'CSC 8520'))

courses.append(models.Course(course = 'CSC 9020',
							department = 'Computing Sciences',
							title = 'Independent Study',
							credits = 3,
							level = 'graduate',
							description = 'Individual research project in an advanced area of computer science, '
							'conducted under the guidance of a faculty member.<br /><a href="/academics/gradIS">'
							'Click here to go to the Graduate Independent Study Page.</a>',
							prerequisites = 'CSC 8520'))

courses.append(models.Course(course = 'CSC 9021',
							department = 'Computing Sciences',
							title = 'Independent Study Continuation',
							credits = 0,
							level = 'graduate',
							description = 'Continuation beyond the first semester for students who have registered '
							'for the independent study  (<a href="/academics/courses/74">CSC 9020</a>).',
							prerequisites = 'CSC 9020'))

courses.append(models.Course(course = 'CSC 9030',
							department = 'Computing Sciences',
							title = 'Thesis',
							credits = 3,
							level = 'graduate',
							description = 'Expanded independent study in which the student makes an original '
							'contribution to the computer science field. For more information about graduate '
							'thesis <a href="http://www1.villanova.edu/villanova/artsci/graduate/currentstude'
							'nts/thesis.html"> click here </a>',
							prerequisites = 'CSC 9020'))

courses.append(models.Course(course = 'CSC 8990',
							department = 'Computing Sciences',
							title = 'Graduate Computing Practicum',
							credits = 1,
							level = 'graduate',
							description = 'Work experience in computing. CSC graduate program approval required '
							'for a specific work opportunity. Required for the practicum option of the MSCS degree.',
							prerequisites = 'CSC 9020'))

courses.append(models.Course(course = 'PHI 2180',
							department = 'Philosophy',
							title = 'Computer Ethics',
							credits = 3,
							level = 'undergraduate',
							description = 'Codes of professional ethics, unauthorized access, ownership of software, '
							'and the social responsibility of computing professionals.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'MAT 4310',
							department = 'Mathematics',
							title = 'Statistical Methods',
							credits = 3,
							level = 'undergraduate',
							description = 'Data displays and summarization, probability distributions, point and '
							'interval estimation, hypothesis testing, categorical data analysis, regression and '
							'correlation.',
							prerequisites = 'MAT 1505'))

courses.append(models.Course(course = 'CSC 3080',
							department = 'Computing Sciences',
							title = 'Information Security and Protection',
							credits = 3,
							level = 'crossover',
							description = 'Explores the criticality of protecting information\'s availability, '
							'accuracy, authenticity, confidentiality, and integrity. Analysis of topics to include '
							'redundancy, backup and recovery, business continuity, security technologies, and '
							'controls such as audit, change management and testing.',
							prerequisites = 'CSC 2400'))

courses.append(models.Course(course = 'CSC 9025',
							department = 'Computing Sciences',
							title = 'Grand Challenges of Computing',
							credits = 3,
							level = 'graduate',
							description = 'Individual or group research/development project involving an advanced '
							'area of computer science, conducted under the guidance of a faculty member.<br />'
							'<a href="/academics/gradIS">Click here for more information.</a>',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 4710',
							department = 'Computing Sciences',
							title = 'Information Systems Project Management',
							credits = 3,
							level = 'crossover',
							description = 'Principles and techniques of information systems project management; '
							'qualitative and quantitative essentials to include project integration, scope, '
							'schedule, cost, quality, human resources, communications, and risk. Practical '
							'experience managing a project with complex technology issues.',
							prerequisites = 'Junior standing'))

courses.append(models.Course(course = 'CSC 4797',
							department = 'Computing Sciences',
							title = 'Information Systems Capstone',
							credits = 3,
							level = 'undergraduate',
							description = 'Student driven project on the application of an emerging technology '
							'that demonstrates learned project management, system design and communication '
							'skills. A cumulative experience to complete a student\'s portfolio of expertise '
							'in information systems.',
							prerequisites = 'Senior standing; Information Systems majors only'))

courses.append(models.Course(course = 'CSC 1035',
							department = 'Computing Sciences',
							title = 'Databases for Many Majors',
							credits = 3,
							level = 'nonmajor',
							description = 'No background in computing necessary. Design and implementation of '
							'your own database as a group project. Cooperative learning techniques to demystify '
							'key concepts: the relational model, normalization, the Entity-Relationship model and SQL.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 1990',
							department = 'Computing Sciences',
							title = 'Enrichment Seminar in Computing',
							credits = 3,
							level = 'undergraduate',
							description = 'The catalog description of this course will be posted soon.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 4510',
							department = 'Computing Sciences',
							title = 'Machine Learning',
							credits = 3,
							level = 'crossover',
							description = 'The nature of intelligence and the question of its computer '
							'implementation; the nature of learning and how it might be cast as an algorithm; '
							'the design of software systems that adapt to new circumstances in their environments.',
							prerequisites = 'CSC 1051'))

courses.append(models.Course(course = 'CSC 2400',
							department = 'Computing Sciences',
							title = 'Computing Systems I',
							credits = 3,
							level = 'undergraduate',
							description = 'Architecture of computer systems: representation of data; processor, '
							'memory and I/O organization. Assembly language programming. C programming language '
							'constructs and their relationships to the underlying architecture. Basics of operating '
							'systems: interrupts, concurrency, process scheduling, security, networking.',
							prerequisites = 'CSC 1052 and CSC 1300'))

courses.append(models.Course(course = 'CSC 2405',
							department = 'Computing Sciences',
							title = 'Computing Systems II',
							credits = 3,
							level = 'undergraduate',
							description = 'Processes, threads and concurrent programming. Scheduling and Dispatching. '
							'Linking and Relocating. Memory management. Virtual memory. System level I/O device '
							'management. File systems. Security and protection in depth. Real time and embedded systems. '
							'System performance evaluation.',
							prerequisites = 'CSC 2400'))

courses.append(models.Course(course = 'CSC 8991',
							department = 'Computing Sciences',
							title = 'Graduate Computing Practicum Continuation',
							credits = 0,
							level = 'graduate',
							description = 'The catalog description of this course will be posted soon.',
							prerequisites = 'CSC 8990'))

courses.append(models.Course(course = 'CSC 1000',
							department = 'Computing Sciences',
							title = 'The Practice of Computing',
							credits = 3,
							level = 'nonmajor',
							description = 'Anatomy of a computing system including tiny systems such as cell phones; '
							'resource management-memory, processes, file structure; network analysis-network topology, '
							'performance, privacy, security; application scripting-concepts and practices of programming.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 8541',
							department = 'Computing Sciences',
							title = 'Requirements Engineering',
							credits = 3,
							level = 'graduate',
							description = 'Students will practice current techniques of requirements engineering. This '
							'class will focus on developing excellent oral and written technical communication skills. '
							'Topics may include: requirements elicitation and analysis; requirements specification; test '
							'driven development; system modeling; requirements validation; requirements management.',
							prerequisites = 'CSC 8540'))

courses.append(models.Course(course = 'CSC 8542',
							department = 'Computing Sciences',
							title = 'Software Design and Evolution',
							credits = 3,
							level = 'graduate',
							description = 'Students will be introduced to both "high level" and "low level" design '
							'concepts. High level design concepts include client/server and web architectures, mobile '
							'computing, the use of common frameworks (e.g. J2EE and .NET), and strategies for evolving '
							'software. Low level design concepts include analysis patterns, design patterns, and '
							'refactoring approaches. Students will receive a specification, and will design and evolve '
							'a solution. This class will continue to emphasize oral and written technical communication '
							'skills.',
							prerequisites = 'CSC 8541'))

courses.append(models.Course(course = 'CSC 3990',
							department = 'Computing Sciences',
							title = 'Computing Research Topics',
							credits = 3,
							level = 'undergraduate',
							description = 'Centered around the development of a research project in one of several '
							'selected computing topics. Experimentation, data collection, literature review. Standard '
							'for written presentation of information. Reports of progress required of all students.',
							prerequisites = 'CSC 2053'))

courses.append(models.Course(course = 'CSC 8491',
							department = 'Computing Sciences',
							title = 'Data Mining and Database Programming',
							credits = 3,
							level = 'graduate',
							description = 'The catalog description of this course will be posted soon.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 2020',
							department = 'Computing Sciences',
							title = 'Web Development & Technologies I',
							credits = 3,
							level = 'nonmajor',
							description = 'Design of web content, utilization of web tools, configuration of supporting '
							'technologies. Emphasis on client-side services: HTML, style sheets, JavaScript, Document '
							'Object Model,DHTML.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 2025',
							department = 'Computing Sciences',
							title = 'Web Development & Technologies II',
							credits = 3,
							level = 'nonmajor',
							description = 'Design of web content, configuration of supporting web technologies. '
							'Emphasis on server-side services: databases and forms, CGI, Perl, PHP, XML, AJAX, cookies '
							'and session management, security issues.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'CSC 1045',
							department = 'Computing Sciences',
							title = 'Algorithms, Cartoons, and Animation',
							credits = 3,
							level = 'nonmajor',
							description = 'Computer-assisted animation & its programming dialects; cartoon creation '
							'from story-boarding to product delivery; algorithms - efficiency, correctness, '
							'understanding via animation.',
							prerequisites = 'None'))

courses.append(models.Course(course = 'MSE 2000',
							department = 'Computing Sciences',
							title = 'Evolution and Learning in Computational and Robotic Agents',
							credits = 4,
							level = 'crossover',
							description = 'Ever wonder how iTunes\' Genius option figures out what music or movies '
							'you might like based on your purchase history?  Can home-based medical-care robots learn '
							'how to respond to their human patients\' emotional patterns? This course explores how '
							'software designers and artificial intelligence researchers draw inspiration from biology '
							'and learning theory to design programs and robotic agents that learn and adapt to changes '
							'in their environment.  No prior programming experience is required.',
							prerequisites = 'None'))




for i in courses:
  db.session.add(i)

db.session.commit()