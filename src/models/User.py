from Database.database import Base
from sqlalchemy import Column , Integer , String


class User(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    model_no = Column(String(10),unique=True)
    model_type = Column(String(10))
    model_year = Column(Integer)
    price = Column(Integer)
    date = Column(String)


