from flask import Response, request
from database.Items import Item
from flask_restful import Resource


class ItemsApi(Resource):
    @staticmethod
    def get():
        Items = Item.objects().to_json()
        return Response(Items, mimetype="application/json", status=200)

    @staticmethod
    def post(self):
        body = request.get_json()
        Item = Item(**body).save()
        id = Item.id
        return {'id': str(id)}, 200


class ItemApi(Resource):
    @staticmethod
    def put(self, id):
        body = request.get_json()
        Item.objects.get(id=id).update(**body)
        return '', 200

    @staticmethod
    def delete(self, id):
        Item = Item.objects.get(id=id).delete()
        return '', 200

    @staticmethod
    def get(self, id):
        Items = Item.objects.get(id=id).to_json()
        return Response(Items, mimetype="application/json", status=200)
