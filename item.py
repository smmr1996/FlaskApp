import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
class Items(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('name',
		type=str,
		required=True,
		help="This field cannot be blank")
	parser.add_argument('price',
		type=float,
		required=True,
		help="This field cannot be blank")
	def get(self,name):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query="SELECT * FROM itemdb WHERE name=?"
		result=cursor.execute(query,(name,))
		row=result.fetchone()
		connection.close()
		if row:
			return {'name':row[0], 'price':row[1]},200

		return {"message":"Item not found!"},404

	def put(self,name):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		querysearch="SELECT * FROM itemdb WHERE name=?"
		result=cursor.execute(querysearch,(name,))
		row=result.fetchone()
		data=Items.parser.parse_args()
		item={
				"name": data["name"],
				"price":data["price"]
			}
		if not row:
			
			queryinsert="INSERT INTO itemdb VALUES (?,?)"
			cursor.execute(queryinsert,(item['name'],item['price']))
			connection.commit()
			connection.close()
			return item, 201
		queryUpdate="UPDATE itemdb SET price=? where name=?"
		cursor.execute(queryUpdate,(item['price'],item['name']))
		connection.commit()
		connection.close()
		return item, 201


	def post(self,name):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		querysearch="SELECT * FROM itemdb WHERE name=?"
		result=cursor.execute(querysearch,(name,))
		row=result.fetchone()
		connection.close()
		if row:
			return {'message':"Item with name '{}' already exists".format(name)},400
		data=Items.parser.parse_args()
		item={
				"name": data["name"],
				"price":data["price"]
			}
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		queryinsert="INSERT INTO itemdb VALUES (?,?)"
		cursor.execute(queryinsert,(item['name'],item['price']))
		connection.commit()
		connection.close()
		return item, 201

	def delete(self,name):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query="DELETE FROM itemdb WHERE name=?"
		cursor.execute(query,(name,))
		connection.commit()
		connection.close()
		return {'message':"Item Deleted!"},200


class Itemlist(Resource):
	@jwt_required()
	def get(self):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query="SELECT * FROM itemdb"
		lis=[]
		for row in cursor.execute(query):
			item={'name':row[0], 'price':row[1]}
			lis.append(item)
		connection.close()
		return {"items":lis},200

			

