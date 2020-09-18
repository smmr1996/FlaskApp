import sqlite3
from flask_restful import Resource,reqparse

class User:
	def __init__(self,_id,name,password):
		self.id=_id
		self.name=name
		self.password=password

	def getUserByUserName(username):
		connection = sqlite3.connect("data.db")
		cursor=connection.cursor()
		selectQuery="SELECT * from users where username==?"
		result=cursor.execute(selectQuery,(username,))
		row=result.fetchone()
		if row:
			user=User(row[0],row[1],row[2])
		else:
			user=None
		connection.close()
		return user


	def getUserByID(_id):
		connection = sqlite3.connect("data.db")
		cursor=connection.cursor()
		selectQuery="SELECT * from users where id==?"
		result=cursor.execute(selectQuery,(_id,))
		row=result.fetchone()
		if row:
			user=User(row[0],row[1],row[2])
		else:
			user=None
		connection.close()
		return user

class NewUser(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('username',
		type=str,
		required=True,
		help="This field cannot be blank")
	parser.add_argument('password',
		type=str,
		required=True,
		help="This field cannot be blank")

	def post(self):
		
		data=NewUser.parser.parse_args()
		if User.getUserByUserName(data['username']):
			return {"message": "A user with that username already Exists"},400

		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()

		query="INSERT INTO users VALUES (NULL,?,?)"
		cursor.execute(query,(data['username'],data['password']))
		connection.commit()
		connection.close()
		return {"message":"User created successfully!"},201
