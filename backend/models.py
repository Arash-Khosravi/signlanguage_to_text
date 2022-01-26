from sqlalchemy import Column, String, Integer
from database import Base


class Translate(Base):
    __tablename__ = 'translate'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url = Column(String)
    description = Column(String)


class Photo(Base):
    __tablename__ = 'photo'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url = Column(String)
    description = Column(String)

