from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    ticker = Column(String, nullable=False, unique=True)
    isin = Column(String, unique=True)
    figi = Column(String, unique=True)
    country = Column(String)
    sector = Column(String)
    industry = Column(String)
    listing_date = Column(Date)
    earnings = relationship("Earnings", back_populates="company", cascade="all, delete")
