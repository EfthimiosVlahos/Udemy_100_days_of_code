import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db=sqlite3.connect("books-collection.db") #Creating connection to new database
# cursor=db.cursor() #Cursor that will control our database and does all the work (also known as mouse or pointer)

#Notes for below line of code:

#.execute()- This method will tell the cursor to execute an action. All actions in SQLite databases are expressed
# as SQL (Structured Query Language) commands. These are almost like English sentences with keywords written in ALL-CAPS.
# There are quite a few SQL commands. But don't worry, you don't have to memorise them.

#books -  This is the name that we've given the new table we're creating.

#() -  The parts that come inside the parenthesis after CREATE TABLE books ( ) are going to be the fields in this table.
# Or you can imagine it as the Column headings in an Excel sheet.

#id INTEGER PRIMARY KEY -  This is the first field, it's a field called "id" which is of data type INTEGER and it will
# be the PRIMARY KEY for this table. The primary key is the one piece of data that will uniquely identify this record
# in the table. e.g. The primary key of humans might be their passport number because no two people in the same country
# has the same passport number.

#title varchar(250) NOT NULL UNIQUE -  This is the second field, it's called "title" and it accepts a variable-length
# string composed of characters. The 250 in brackets is the maximum length of the text. NOT NULL means it must have a
# value and cannot be left empty. UNIQUE means no two records in this table can have the same title.

#author varchar(250) NOT NULL -  A field that accepts variable-length Strings up to 250 characters called autho
# r that cannot be left empty.

#rating FLOAT NOT NULL -  A field that accepts FLOAT data type numbers, cannot be empty and the field is called rating.

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) "
#                "NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

#This will create a new entry in our books table for the Harry Potter book and commit the changes to our database.

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


#Code using SQL Alchemy:

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# CREATE RECORD
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()

