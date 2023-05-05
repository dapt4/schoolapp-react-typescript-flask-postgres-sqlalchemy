from flask import Flask, request
from database.db import engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.models import SchoolClass, Student, BelongsTo
from database.create_tables import create_tables


app = Flask(__name__)
# create_db_tables()

@app.route('/class', methods=['GET'])
def get_classes():
    try:
        with Session(engine) as session:
            stmt = select(SchoolClass)
            school_classes = session.scalars(stmt).all()
            school_classes = [school.to_dict() for school in school_classes]
            return school_classes
    except Exception as e:
        return {'error': str(e)}

@app.get('/class/<int:class_id>')
def get_a_class(class_id):
    try:
        with Session(engine) as session:
            stmt = select(SchoolClass).where(SchoolClass.id == class_id)
            school_class = session.scalars(stmt).one()
            return school_class.to_dict()
    except Exception as e:
        return {'error': str(e)}

@app.post('/class')
def create_class():
    try:
        with Session(engine) as session:
            school_class = SchoolClass(name=request.json['name'])
            session.add(school_class)
            session.commit()
            return school_class.to_dict()
    except Exception as e:
        return {'error': str(e)}
    
@app.delete('/class/<int:class_id>')
def delete_class(class_id):
    try:
        with Session(engine) as session:
            selected_class = session.get(SchoolClass, class_id)
            session.delete(selected_class)
            session.commit()
    except Exceptionerr as err:
        return {'error': str(err)}

