from flask_restful import Resource , reqparse
from models.user import UserModel

#resources is an external representation of an entity

class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="enter sthg god damn it")
    parser.add_argument('password', type=str, required=True, help="emter sthg god damn it")
    
    def post(self):
        data= UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message":"User already exits"}, 400
            
        user = UserModel(data['username'], data['password'])     #the same as data['username'],data['password'] as the parser
        user.save_to_db()

        return {"message":"User created successfully"}, 201
