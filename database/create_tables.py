from database.db import engine
from sqlalchemy import MetaData
from models.models import SchoolClass, Student, BelongsTo

metadata = MetaData()

def create_tables():
    metadata.create_all(engine, tables=[
        SchoolClass.__table__,
        Student.__table__,
        BelongsTo.__table__])


