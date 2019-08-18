import sys
from datetime import datetime
from model.setting import Base, ENGINE
from sqlalchemy import Column, Integer, String, DateTime


class User(Base):
    """
    ユーザモデル
    """
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200), nullable=False)
    age = Column('age', Integer)
    email = Column('email', String(100))
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
