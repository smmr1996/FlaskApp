import sqlite3

connection = sqlite3.connect("data.db")
cursor=connection.cursor()

createTable="CREATE TABLE users (id int, username text, password text)"

cursor.execute(createTable)

insertQuery="INSERT INTO users VALUES (?,?,?)"

user=(1,'Jose',"asdf")
cursor.execute(insertQuery,user)

users= [
	(2,'Jerry',"asdf"),
	(3,'Jordan',"asdf"),
	(4,'Jay',"asdf")
]

selectQuery="SELECT * from users"
for row in cursor.execute(selectQuery):
	print(row)

cursor.executemany(insertQuery,users)

for row in cursor.execute(selectQuery):
	print(row)

connection.commit()
connection.close()


