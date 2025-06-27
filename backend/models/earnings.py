from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .company import Base


class Earnings(Base):
    __tablename__ = "earnings"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)

    period = Column(String, nullable=False)
    report_date = Column(Date, nullable=False)
    eps_basic = Column(Float, nullable=True)  # Ganancia por acción
    eps_diluted = Column(Float, nullable=True)  # Ganancia por acción diluida
    net_income = Column(Float, nullable=True)  # Resultado neto en moneda local

    company = relationship("Company", back_populates="earnings")
