import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def to_dict(self) :
        return {
            'id' : self.id,
            'name' :self.name
        }