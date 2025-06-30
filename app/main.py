from sqlalchemy import create_engine
from backend.models.company import Base

# Crear conexión al motor de PostgreSQL
engine = create_engine("postgresql://screener:screener123@localhost:5432/screener_db")

# Crear todas las tablas
Base.metadata.create_all(bind=engine)
