from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean
from sqlalchemy.orm import relationship
from .company import Base


class SecFiling(Base):
    __tablename__ = "sec_filings"

    id = Column(Integer, primary_key=True)
    cik = Column(
        String, index=True
    )  # Central Index Key, 10 digit number provided by the SEC
    ticker = Column(String, index=True)
    form_type = Column(String)  # 10-K, 10-Q, 8-K...
    period_end = Column(Date)
    local_path = Column(String)
    format = Column(String)  # ixbrl | xbrl | html
    parsed_at = Column(DateTime(timezone=True))
    parse_ok = Column(Boolean, default=False)
