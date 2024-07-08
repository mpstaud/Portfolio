import sqlite3
import bcrypt

con = sqlite3.connect("app.db")
cur = con.cursor()

table = """ CREATE TABLE user (
            Email VARCHAR(255) NOT NULL,
            First_Name CHAR(25) NOT NULL,
            Last_Name CHAR(25),
            Password VARCHAR(255) NOT NULL
        ); """


# cur.execute("""INSERT INTO user VALUES('staudachermatthew@gmail.com','Matthew','Staudacher','MILO1234')""")
for row in cur.execute("""SELECT * FROM user"""):
    print(row[0], row[3])

# con.commit()




con.close()