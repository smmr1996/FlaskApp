from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from Autentication import authenticate,identity
from Users import NewUser
from item import Items, Itemlist

app=Flask(__name__)
api=Api(app)
app.secret_key="Jose"

jwt=JWT(app,authenticate,identity)

items=[]


api.add_resource(Items,"/items/<string:name>")
api.add_resource(Itemlist,"/items")
api.add_resource(NewUser,"/register")

if __name__=='__main__':
	app.run(port=3000)


