import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_table="CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username text,password text)"

cursor.execute(create_table)
create_item="CREATE TABLE IF NOT EXISTS itemdb (name text,price real)"

cursor.execute(create_item)

connection.commit()
connection.close()