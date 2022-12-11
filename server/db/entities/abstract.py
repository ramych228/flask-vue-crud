from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
import json

Base = declarative_base()


class Abstract(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self):
        self.updated_at = datetime.utcnow()

    def serialize(self):
        dict = {
            'id': self.id,
            'created_at': json.dumps(self.created_at, default=str),
            'updated_at': json.dumps(self.updated_at, default=str)
        }
        return dict

    def __repr__(self):
        return '<Abstract(id=%r, created_at=%r, updated_at=%r)>' % (self.id, self.created_at, self.updated_at)
