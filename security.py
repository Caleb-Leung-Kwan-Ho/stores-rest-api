from resources.user import UserModel
import hmac


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and hmac.compare_digest(user.password ,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)