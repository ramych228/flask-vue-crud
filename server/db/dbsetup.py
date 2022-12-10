from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .entities.abstract import Base
from .entities.project import Project
from .entities.student import Student


class DBSetup:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_db(self):
        engine = create_engine('sqlite:///' + self.db_path, connect_args={'check_same_thread': False},
                               poolclass=StaticPool, echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(Project('Project 1', 'Project 1 description'))
        session.add(Project('Project 2', 'Project 2 description'))
        session.add(Project('Project 3', 'Project 3 description'))
        session.add(Student('Student 1', 'Student 1 description'))
        session.add(Student('Student 2', 'Student 2 description'))
        session.add(Student('Student 3', 'Student 3 description'))
        session.commit()
        session.close()

    def drop_db(self):
        engine = create_engine('sqlite:///' + self.db_path, connect_args={'check_same_thread': False},
                               poolclass=StaticPool, echo=True)
        Base.metadata.drop_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.commit()
        session.close()

    def reset_db(self):
        self.drop_db()
        self.create_db()

    def get_session(self):
        engine = create_engine('sqlite:///' + self.db_path, connect_args={'check_same_thread': False},
                               poolclass=StaticPool, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def close_session(self, session):
        session.commit()
        session.close()

    def get_db_path(self):
        return self.db_path


