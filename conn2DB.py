import sqlite3

conn = sqlite3.connect('databaseQA.db')

cursor = conn.cursor()

cursor.execute (''' CREATE TABLE IF NOT EXISTS QuizBowlDB (
                id INTEGER PRIMARKY KEY TEXT AUTOINCRIMENT,
                question TEXT NOT NULL,
                option_a TEXT NOT NULL, 
                option_b TEXT NOT NULL, 
                option_c TEXT NOT NULL, 
                option_d TEXT NOT NULL, 
                answer TEXT NOT NULL ''')


DBMGT_data = quiz_bowl_questions = [
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
]

cursor.executemany('''INSERT INTO quizbowlDB (question, option_a, option_b, option_c, option_d, correct answer
                   VALUES(?,?,?,?,?,?)''', quiz_bowl_questions)

conn.commit()

cursor.close()
conn.close()
