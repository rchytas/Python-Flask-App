from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.object import ObjectModel


class Object(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('parent_id',
                        type=int,
                        required=True,
                        help="Every object needs a parent_id."
                        )

    @jwt_required()
    def get(self, name):
        item = ObjectModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ObjectModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Object.parser.parse_args()

        item = ObjectModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = ObjectModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
        data = Object.parser.parse_args()

        item = ObjectModel.find_by_name(name)

        if item:
            item.price = data['price']
        else:
            item = ObjectModel(name, **data)

        item.save_to_db()

        return item.json()


class ObjectList(Resource):
    def get(self):
        return {'objects': list(map(lambda x: x.json(), ObjectModel.query.all()))}
