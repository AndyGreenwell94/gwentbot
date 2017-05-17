import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

engine = create_engine(os.environ.get('CONNECTION'))
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Cards(Base):
    __tablename__ = 'card'

    index = Column(Integer, primary_key=True)
    name = Column(String)
    href = Column(String)
    text = Column(String)
    flavor = Column(String)
    image = Column(String)


