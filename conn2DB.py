import sqlite3

conn = sqlite3.connect('databaseQA.db')

cursor = conn.cursor()

cursor.execute ('''CREATE TABLE IF NOT EXISTS DBMGTtb(
                id INTEGER PRIMARKY KEY TEXT AUTOINCRIMENT,
                question TEXT NOT NULL,
                option_a TEXT NOT NULL, 
                option_b TEXT NOT NULL, 
                option_c TEXT NOT NULL, 
                option_d TEXT NOT NULL, 
                answer TEXT NOT NULL ''')


quiz_bowl_questions = [
    ("What term refers to a structured collection of data organized and stored electronically?",
     "A) File", "B) Record", "C) Database", "D) Spreadsheet", "C) Database"),

    ("Name the component of a database management system (DBMS) responsible for defining the database structure.",
     "A) Data Manipulation Language (DML)", "B) Data Control Language (DCL)",
     "C) Data Definition Language (DDL)", "D) Data Query Language (DQL)", "C) Data Definition Language (DDL)"),

    ("Differentiate between SQL and NoSQL databases in terms of their data storage approach.",
     "A) SQL databases store data in tables with predefined schemas, while NoSQL databases store data in flexible formats like JSON.",
     "B) SQL databases store data in flexible formats like JSON, while NoSQL databases store data in tables with predefined schemas.",
     "C) SQL databases are schema-less, while NoSQL databases use predefined schemas.",
     "D) SQL databases are best suited for unstructured data, while NoSQL databases are designed for structured data.",
     "A) SQL databases store data in tables with predefined schemas, while NoSQL databases store data in flexible formats like JSON."),

    ("What is the primary purpose of normalization in database design?",
     "A) To maximize redundancy", "B) To minimize data integrity",
     "C) To reduce redundancy and dependency, improve data integrity, and optimize database performance.",
     "D) To ensure inconsistent data", "C) To reduce redundancy and dependency, improve data integrity, and optimize database performance."),

    ("Define a primary key in the context of a relational database.",
     "A) A unique identifier for each record in a table, ensuring data integrity and uniqueness.",
     "B) A secondary identifier for each record in a table",
     "C) A value that can be null in a table",
     "D) A value that changes frequently",
     "A) A unique identifier for each record in a table, ensuring data integrity and uniqueness.")

     (" What of the following is considered one of the 4 types of data?",
      "A). Source Data- raw facts and figures",
      "B). Meta Data- Data about data, ex. Data dictionary (self describing)",
      "C). Application Meta- Data about data, ex. Data dictionary (self describing)", 
      "D). Trifecta Data- Data pulling from three other types of data (multi describing)", 
      "D). Trifecta Data - Data pulling from three other types of data (multi describing)")

      ("What is the primary purpose of a database management system (DBMS)?", 
     "A) To create tables and fields",
      "B) To manage computer hardware resources",
      "C) To store, retrieve, and manipulate data",
      "D) To design user interfaces",
      "Answer: C) To store, retrieve, and manipulate data"),
    
    ("Which of the following is NOT a type of database model?", 
     "A) Relational",
      "B) Hierarchical",
      "C) Object-oriented",
      "D) Linear",
      "Answer: D) Linear"),

    ("What does SQL stand for in the context of databases?", 
     "A) Structured Query Language",
      "B) System Query Logic",
      "C) Sequential Query Language",
      "D) Semantic Query Logic",
      "Answer: A) Structured Query Language"),

    ("Which of the following is a key feature of relational databases?", 
     "A) Hierarchical data organization",
      "B) Limited data integrity constraints",
      "C) Ability to represent complex relationships between data entities",
      "D) Lack of support for transactions",
      "Answer: C) Ability to represent complex relationships between data entities")
]

cursor.executemany('''INSERT INTO databaseQA.db (question, option_a, option_b, option_c, option_d, correct answer
                   VALUES(?,?,?,?,?,?)''', quiz_bowl_questions)


cursor.execute ('''CREATE TABLE IF NOT EXISTS OBMGTtb(
                id INTEGER PRIMARKY KEY TEXT AUTOINCRIMENT,
                question TEXT NOT NULL,
                option_a TEXT NOT NULL, 
                option_b TEXT NOT NULL, 
                option_c TEXT NOT NULL, 
                option_d TEXT NOT NULL, 
                answer TEXT NOT NULL ''')

organizational_behavior_questions_mc = [
    ("What is organizational behavior?",
     "A) The study of how individuals and groups behave within an organization.", "B) The process of managing financial resources in a company.",
      "C) The development of marketing strategies for businesses.", "D) The analysis of consumer behavior in the market.",
      "A. The study of how individuals and groups behave within an organization."),

    ("What are the key components of organizational behavior?",
     "A) Individual behavior, group behavior, and organizational aspects.", "B) Financial management, marketing, and human resources.",
      "C) Production, distribution, and sales.", "D) Leadership, motivation, and conflict resolution.",
      "A. Individual behavior, group behavior, and organizational aspects."),

    ("What is motivation in organizational behavior?",
     "A) The internal and external factors that stimulate desire and energy in people to be continually interested and committed to their jobs and roles.", "B) The process of organizing and coordinating activities in a company.",
      "C) The implementation of training programs for employees.", "D) The analysis of market trends and consumer preferences.",
      "A. The internal and external factors that stimulate desire and energy in people to be continually interested and committed to their jobs and roles. "),

    ("Define leadership in organizational behavior.",
     "A) The process of influencing and inspiring others to work towards achieving a common goal.", "B) The management of financial resources in a company.",
      "C) The development of new products and services.", "D) The study of consumer behavior in the market.",
      "A. The process of influencing and inspiring others to work towards achieving a common goal. "),

    ("What is organizational culture?",
     "A) The shared values, beliefs, and norms that influence the behavior of organizational members.", "B) The process of hiring and training employees.",
      "C) The analysis of market competition.", "D) The implementation of quality control measures.",
      "A. The shared values, beliefs, and norms that influence the behavior of organizational members. "),

    ("Explain the concept of diversity in organizational behavior.",
     "A) Diversity refers to the presence of individual differences based on gender, race, ethnicity, age, sexual orientation, etc., within an organization.", "B) Diversity refers to the variety of products offered by a company.",
      "C) Diversity refers to the number of employees in an organization.", "D) Diversity refers to the geographical locations of company offices.",
      "A. Diversity refers to the presence of individual differences based on gender, race, ethnicity, age, sexual orientation, etc., within an organization. ")
      
    ("What is the focus of the contingency approach to organizational behavior?",
    "A) The impact of situational factors on organizational outcomes",
    "B) The study of individual personality traits",
    "C) The analysis of organizational structures",
    "D) The examination of group dynamics",
    "A. The impact of situational factors on organizational outcomes"),
    
    ("What is the term for the process of adapting to a new organizational culture?",
    "A) Socialization",
    "B) Assimilation",
    "C) Conformity",
    "D) Integration",
    "A. Socialization"),
    
   ( "Which leadership style focuses on maximizing employee participation in decision-making?",
    "A) Autocratic leadership",
    "B) Transactional leadership",
    "C) Transformational leadership",
    "D) Democratic leadership",
    "D. Democratic leadership"),
    
    ("What theory suggests that employees are motivated by the belief that their efforts will lead to desired outcomes?",
    "A) Expectancy theory",
    "B) Equity theory",
    "C) Herzberg's two-factor theory",
    "D) Maslow's hierarchy of needs",
    "A. Expectancy theory"),
    
    ("What is the term for the phenomenon where individuals exert less effort in group settings compared to when working alone?",
    "A) Social loafing",
    "B) Groupthink",
    "C) Deindividuation",
    "D) Conformity",
    "A. Social loafing"),
    
    ("What concept refers to the tendency for individuals to attribute their own successes to internal factors and failures to external factors?",
    "A) Self-serving bias",
    "B) Fundamental attribution error",
    "C) Cognitive dissonance",
    "D) Group polarization",
    "A. Self-serving bias")
]

cursor.executemany('''INSERT INTO databaseQA.db (question, option_a, option_b, option_c, option_d, correct answer
                   VALUES(?,?,?,?,?,?)''', organizational_behavior_questions_mc)

cursor.execute ('''CREATE TABLE IF NOT EXISTS MKTtb(
                id INTEGER PRIMARKY KEY TEXT AUTOINCRIMENT,
                question TEXT NOT NULL,
                option_a TEXT NOT NULL, 
                option_b TEXT NOT NULL, 
                option_c TEXT NOT NULL, 
                option_d TEXT NOT NULL, 
                answer TEXT NOT NULL ''')

 
marketing_questions = [
    ("What is the primary goal of marketing?",
     "A) To increase profits",
      "B) To satisfy customer needs and wants",
      "C) To minimize costs",
      "D) To expand market share",
      "Answer: B) To satisfy customer needs and wants"),
    
    ("What is the marketing mix composed of?",
     "A) Product, Price, Promotion, People",
      "B) Product, Price, Promotion, Place",
      "C) Product, Promotion, Placement, Profit",
      "D) Product, Price, Placement, Profit",
      "B. Product, Price, Promotion, Place"),

    ("What is branding?",
     "A) The process of creating a unique name and image for a product",
      "B) The process of selling products online",
      "C) The process of advertising products on social media",
      "D) The process of distributing products to retailers",
      "A. The process of creating a unique name and image for a product"),

    ("What is market segmentation?",
     "A) Targeting the entire market with a single marketing strategy",
      "B) Dividing the market into smaller, distinct groups of consumers with similar needs",
      "C) Selling products at different prices in different markets",
      "D) Promoting products to a global audience",
      "B. Dividing the market into smaller, distinct groups of consumers with similar needs"),

    ("What is the purpose of a SWOT analysis in marketing?",
     "A) To identify Strengths, Weaknesses, Opportunities, and Threats related to a business or product",
      "B) To develop promotional campaigns",
      "C) To analyze sales data",
      "D) To create customer personas",
      "A. To identify Strengths, Weaknesses, Opportunities, and Threats related to a business or product"),

    ("What is the role of market research in marketing?",
     "A) To create brand logos",
      "B) To analyze consumer behavior and preferences",
      "C) To negotiate contracts with suppliers",
      "D) To manage inventory levels",
      "B. To analyze consumer behavior and preferences"),

    ("What is the difference between advertising and public relations?",
     "A) Advertising focuses on paid promotional messages, while public relations focuses on building relationships with media and stakeholders",
      "B) Advertising focuses on building relationships with media and stakeholders, while public relations focuses on paid promotional messages",
      "C) Advertising is conducted online, while public relations is conducted offline",
      "D) Advertising is aimed at businesses, while public relations is aimed at consumers",
      "A. Advertising focuses on paid promotional messages, while public relations focuses on building relationships with media and stakeholders"),

    ("What is the purpose of a target market?",
     "A) To identify competitors",
      "B) To determine pricing strategies",
      "C) To focus marketing efforts on specific groups of consumers",
      "D) To select distribution channels",
      "C. To focus marketing efforts on specific groups of consumers"),

    ("What is the difference between a product and a service?",
     "A) A product is tangible, while a service is intangible",
      "B) A product is intangible, while a service is tangible",
      "C) A product is sold to businesses, while a service is sold to consumers",
      "D) A product is used for personal purposes, while a service is used for business purposes",
       "A. A product is tangible, while a service is intangible"),

    ("What is the purpose of a marketing plan?",
     "A) To outline business objectives and strategies for reaching target markets",
      "B) To manage human resources within a company",
      "C) To track financial performance",
      "D) To develop product prototypes",
      "A. To outline business objectives and strategies for reaching target markets")
]

cursor.executemany (''' INSERT INTO databaseQA.db  (question, option_a, option_b, option_c, option_d, correct answer
                   VALUES(?,?,?,?,?,?)''', marketing_questions)



conn.commit()

cursor.close()
conn.close()
