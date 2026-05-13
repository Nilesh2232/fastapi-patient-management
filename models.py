from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from database import engine

Base = declarative_base()


class Patient(Base):

    __tablename__ = "PatientDetails"

    Patient_id = Column(Integer, primary_key=True, index=True)

    First_Name = Column(String(50), nullable=False)
    Middle_Name = Column(String(50), nullable=True)

    Last_Name = Column(String(50), nullable=False)

    DOB = Column(String(20), nullable=False)

    Age = Column(Integer, nullable=False)

    Gender = Column(String(20), nullable=False)

    Phone = Column(String(15), nullable=False)

    Alternate_Phone = Column(String(15), nullable=True)

    Email = Column(String(100), nullable=True)

    Blood_Group = Column(String(5), nullable=True)


Base.metadata.create_all(bind=engine)