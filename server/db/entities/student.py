from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import json

from .abstract import Abstract
from .project import Project


class Student(Abstract):
    __tablename__ = 'students'
    name = Column(String)
    username = Column(String)
    description = Column(String)
    # lame
    password = Column(String)
    token = Column(String)
    # projects = relationship("Project", secondary=student_project, back_populates="students")

    def __init__(self, name, description, username, password, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
        self.token = token
        self.password = password
        self.username = username

    def serialize(self):
        dict = super().serialize()
        dict.update({
            'name': self.name,
            'description': self.description,
            'password': self.password,
            'username': self.username,
            'token': json.dumps(self.token, default=str)
        })
        return dict

    def update(self, name, description, username, password, token):
        self.name = name
        self.description = description
        self.token = token
        self.password = password
        self.username = username
        super().update()

    def __repr__(self):
        return '<Student(id=%r, created_at=%r, updated_at=%r, name=%r, description=%r, token=%r, password=%r, username=%r)>' % (
            self.id, self.created_at, self.updated_at, self.name, self.description, self.token, self.password,
            self.username)
