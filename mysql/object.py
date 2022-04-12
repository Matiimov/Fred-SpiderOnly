import logging
from mysql.connector import MySQLConnector
from sqlalchemy import Column, String, DATE, FLOAT
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

logger = logging.getLogger(__name__)


db_connector = MySQLConnector.from_config().db_engine
session_factory = sessionmaker()
session_factory.configure(bind=db_connector)
Session = scoped_session(session_factory)  # thread-safe
session = Session()

class CompanyInfo(Base):
    __tablename__ = "companyInfo"

    company_id = Column(String(20), primary_key=True)
    date = Column(DATE, primary_key=True)
    value = Column(FLOAT, nullable=True)

    def __init__(self, company_id, date, value):
        self.company_id = company_id
        self.date = date
        self.value = value

    @staticmethod
    def add(company_id, date, value):
        company_info = CompanyInfo(company_id, date, value)
        session.add(company_info)
        session.commit()