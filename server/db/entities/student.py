from sqlalchemy import Column, String

from .abstract import Abstract


class Student(Abstract):
    __tablename__ = 'students'
    name = Column(String)
    description = Column(String)

    def __init__(self, name, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description

    def serialize(self):
        dict = super().serialize()
        dict.update({
            'name': self.name,
            'description': self.description
        })
        return dict

    def update(self, name, description):
        self.name = name
        self.description = description
        super().update()

    def __repr__(self):
        return '<Student(id=%r, created_at=%r, updated_at=%r, name=%r, description=%r)>' % (
            self.id, self.created_at, self.updated_at, self.name, self.description)