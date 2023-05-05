from sqlalchemy import create_engine
from sqlalchemy import MetaData

engine = create_engine('postgresql://postgres:19570744@localhost/schoolapp', echo=True)


