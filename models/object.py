from db import db


class ObjectModel(db.Model):
    __tablename__ = 'objects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    parent_id = db.Column(db.Integer, db.ForeignKey('parents.id'))
    parent = db.relationship('ParentModel')

    def __init__(self, name, price, parent_id):
        self.name = name
        self.price = price
        self.parent_id = parent_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * from Objects where name = 'name' LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
