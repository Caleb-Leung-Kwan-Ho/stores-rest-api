from db import db


class StoreModel(db.Model):
    __tablename__= "stores"
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(420))
    items = db.relationship('ItemModel', lazy='dynamic')




    def __init__(self,name):
        self.name=name

    def json(self):
        return {"name":self.name,'items':[i.json() for i in self.items.all()]}

    @classmethod    #doesn't need to know the instance but it works with the class
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()   #select *frrom items where name =name Limit 1
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
