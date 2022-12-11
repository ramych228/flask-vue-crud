from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import json

from .abstract import Abstract


class Startup(Abstract):
    __tablename__ = 'startups'
    name = Column(String(100))
    brief = Column(String(500))
    description = Column(String(1000))

    def __init__(self, name, brief, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.brief = brief
        self.description = description

    def serialize(self):
        dict = super().serialize()
        dict.update({
            'name': self.name,
            'brief': self.brief,
            'description': self.description
        })
        return dict

    def update(self, name, brief, description):
        self.name = name
        self.brief = brief
        self.description = description
        super().update()

    def __repr__(self):
        return '<Startup(id=%r, created_at=%r, updated_at=%r, name=%r, brief=%r)>' % (
            self.id, self.created_at, self.updated_at, self.name, self.brief)
