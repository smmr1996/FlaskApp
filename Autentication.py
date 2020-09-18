from werkzeug.security import safe_str_cmp
from Users import User

def authenticate(username, password):
	user=User.getUserByUserName(username)
	if user and safe_str_cmp(user.password,password):
		return user


def identity(payload):
	user_id=payload['identity']
	return User.getUserByID(user_id)
