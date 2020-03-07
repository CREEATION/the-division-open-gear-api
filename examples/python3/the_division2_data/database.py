from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


current_dir = os.path.dirname(__file__)

print(current_dir)
engine = create_engine('sqlite:///{}/gear.db'.format(current_dir), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():

    Base.metadata.create_all(bind=engine)
    print("we are connected to the database successfully")
