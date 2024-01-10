#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal= Animal.query.get_or_404(id)
    response_body= f'''
    <ul>
        <li>ID: {animal.id}</li>
        <li>Name: {animal.name}</li>
        <li>Species: {animal.species}</li>
        <li>Zookeeper: {animal.zookeepers.name}</li>
        <li>Enclosure: {animal.enclosures.environment}</li>
    </ul>
    '''
    response= make_response(response_body,200)
    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get_or_404(id)
    response_body = f'''
    <ul>
        <li>ID: {zookeeper.id}</li>
        <li>Name: {zookeeper.name}</li>
        <li>Birthday: {zookeeper.birthday}</li>
        <li>Animals:
            <ul>
    '''

    for animal in zookeeper.animals:
        response_body += f'<li>Animal: {animal.name}</li>'

    response_body += '''
            </ul>
        </li>
    </ul>
    '''
    return response_body


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure= Enclosure.query.get_or_404(id)
    response_body= f'''
    <ul>
        <li>ID: {enclosure.id}<li>
        <li>Environment: {enclosure.environment}<li>
        <li>Open to visitors: {"Yes" if enclosure.open_to_visitors else "No"}</li>
        <li>Animals:
            <ul>
    '''
    for animal in enclosure.animals:
        response_body += f'<li>Animal: {animal.name}</li>'

    response_body += '''
            </ul>
        </li>
    </ul>
    '''

    return response_body


if __name__ == '__main__':
    app.run(port=5555, debug=True)
