from flask import Flask, request, json

from . import create_app

from .models import Person

app = create_app()


@app.route('/api/v1/person/', methods=['GET'])
def list():
    persons = Person.query.all()
    return json.jsonify([person.to_dict() for person in persons]), 200

@app.route('/api/v1/person/<person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.filter_by(id=person_id).first()
    return json.jsonify(person.to_dict())

