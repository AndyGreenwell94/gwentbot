from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, literal

engine = create_engine('postgres://qobxbmkaamrqmr:469bd55ba4f4570379ca46b9dcd981085a9a72960c7e3f0982062916e38836d8@ec2-54-247-120-169.eu-west-1.compute.amazonaws.com:5432/d4a34ee9v58scr')

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

