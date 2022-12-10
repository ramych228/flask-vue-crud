from sqlalchemy import Column, String

from .abstract import Abstract


class Project(Abstract):
    __tablename__ = 'projects'
    name = Column(String(100))
    brief = Column(String(500))

    def __init__(self, name, brief, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.brief = brief

    def serialize(self):
        dict = super().serialize()
        dict.update({
            'name': self.name,
            'brief': self.brief
        })
        return dict

    def update(self, name, brief):
        self.name = name
        self.brief = brief
        super().update()

    def __repr__(self):
        return '<Project(id=%r, created_at=%r, updated_at=%r, name=%r, brief=%r)>' % (
            self.id, self.created_at, self.updated_at, self.name, self.brief)
