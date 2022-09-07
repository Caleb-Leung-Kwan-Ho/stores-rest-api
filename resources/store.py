from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    
    
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'store not find'},404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message":"store '{}' already there".format(name)},400
        
        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message':'an error occurred while creating the store'},500

        return store.json(),201

    def delete(self,name):
        store= StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'Message':'store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': [i.json() for i in StoreModel.query.all()]}