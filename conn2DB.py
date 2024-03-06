import sqlite3

conn = sqlite3.connect('databaseQA.db')

cursor = conn.cursor()

DBMGT_data = quiz_bowl_questions = [
    ("What term refers to a structured collection of data organized and stored electronically?",
     [("A) File", False), ("B) Record", False), ("C) Database", True), ("D) Spreadsheet", False)]),
    
    ("Name the component of a database management system (DBMS) responsible for defining the database structure.",
     [("A) Data Manipulation Language (DML)", False), ("B) Data Control Language (DCL)", False),
      ("C) Data Definition Language (DDL)", True), ("D) Data Query Language (DQL)", False)]),

    ("Differentiate between SQL and NoSQL databases in terms of their data storage approach.",
     [("A) SQL databases store data in tables with predefined schemas, while NoSQL databases store data in flexible formats like JSON.", True),
      ("B) SQL databases store data in flexible formats like JSON, while NoSQL databases store data in tables with predefined schemas.", False),
      ("C) SQL databases are schema-less, while NoSQL databases use predefined schemas.", False),
      ("D) SQL databases are best suited for unstructured data, while NoSQL databases are designed for structured data.", False)]),

    ("What is the primary purpose of normalization in database design?",
     [("A) To maximize redundancy", False), ("B) To minimize data integrity", False),
      ("C) To reduce redundancy and dependency, improve data integrity, and optimize database performance.", True),
      ("D) To ensure inconsistent data", False)]),

    ("Define a primary key in the context of a relational database.",
     [("A) A unique identifier for each record in a table, ensuring data integrity and uniqueness.", True),
      ("B) A secondary identifier for each record in a table", False),
      ("C) A value that can be null in a table", False),
      ("D) A value that changes frequently", False)])
]

