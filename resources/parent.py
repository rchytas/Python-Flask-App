from flask_restful import Resource
from models.parent import ParentModel


class Parent(Resource):
    def get(self, name):
        parent = ParentModel.find_by_name(name)
        if parent:
            return parent.json()
        return {'message': 'Parent not found'}, 404

    def post(self, name):
        if ParentModel.find_by_name(name):
            return {'message': "A parent with name '{}' already exists.".format(name)}, 400

        parent = ParentModel(name)
        try:
            parent.save_to_db()
        except:
            return {"message": "An error occurred creating the parent."}, 500

        return parent.json(), 201

    def delete(self, name):
        parent = ParentModel.find_by_name(name)
        if parent:
            parent.delete_from_db()

        return {'message': 'Parent deleted'}


class ParentList(Resource):
    def get(self):
        return {'parents': list(map(lambda x: x.json(), ParentModel.query.all()))}
