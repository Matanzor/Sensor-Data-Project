from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class SensorData(Base):
    __tablename__ = 'sensor_data'

    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer, nullable=False)
    time = Column(DateTime, nullable=False)
    pollution_level = Column(Float, nullable=False)

    def __repr__(self):
        return f"<SensorData {self.sensor_id} - {self.pollution_level} at {self.time}>"


# Database connection setup
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/sensor_data_db')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if they don't exist already
Base.metadata.create_all(bind=engine)
