from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import relationship

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, nullable=False)
    birthday= db.Column(db.Date, nullable=False)
    animals= relationship('Animal', back_populates='zookeepers')

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment= db.Column(db.String, nullable=False)
    open_to_visitors= db.Column(db.Boolean, default=False)
    animals= relationship('Animal', back_populates='enclosures')

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String,nullable=False)
    species = db.Column(db.String,nullable=False)
    zookeeper_id= db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id= db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    zookeepers= db.relationship('Zookeeper', back_populates='animals')
    enclosures= db.relationship('Enclosure', back_populates='animals')



    
