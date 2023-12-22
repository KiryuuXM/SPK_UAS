from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Smartphones(Base):
    __tablename__ = 'smartphones'
    id = Column(Integer, primary_key=True)
    model = Column(String(50))
    processor = Column(String(50)) 
    ram = Column(String(50))
    storage = Column(String(50))
    battery_capacity = Column(String(50))
    screen_size = Column(String(50))
    price = Column(String(50))

    def __repr__(self):
        return f"smartphones(id={self.id!r}, model={self.model!r}"
