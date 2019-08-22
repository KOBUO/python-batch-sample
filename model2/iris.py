import datetime
from model2.setting import Base
from sqlalchemy import Column, Integer, String, DateTime, Float


class Iris(Base):
    __tablename__ = 'iris'
    id = Column('id', Integer, primary_key=True)
    sepal_length = Column('sepal_length', Float)
    sepal_width = Column('sepal_width', Float)
    petal_length = Column('petal_length', Float)
    petal_width = Column('petal_width', Float)
    species = Column('species', String(200))
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
