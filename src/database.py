from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String, Integer, DateTime
from datetime import datetime

Base = declarative_base()

class PriceBitcoin(Base):
    __tablename__ = "prices_bitcoin"

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    cryptocurrency = Column(String(50), nullable=False)
    currency = Column(String(10), nullable=False)
    timestamp = Column(DateTime, default=datetime.now)
    