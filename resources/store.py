from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "Already Existing"}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An exception raises during inserting item"}, 500

        return store.json(), 201

    def delete(self, name):
        item = StoreModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message": "Item succesfully deleted !"}


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
