import json

from flask import Flask, request

from . import create_app

from .models import Person

app = create_app()


@app.route('/api/v1/person')
def list():
    persons = Person.query.all()
    return jsonify(persons.to_dict()), 200

@app.route('/api/v1/person/<person_id>')
def get_person(person_id):
    persons = Person.query.filter_by(id=person_id)
    return persons

