from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import SensorData, SessionLocal
from datetime import datetime, timedelta

router = APIRouter()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/api/sensor_data")
def get_sensor_data(db: Session = Depends(get_db)):
    """
    Retrieve the average pollution level for the last 24 hours.
    """
    # Get data from the last 24 hours
    time_threshold = datetime.utcnow() - timedelta(days=1)

    data = db.query(SensorData).filter(SensorData.time >= time_threshold).all()

    if not data:
        raise HTTPException(status_code=404, detail="No data found in the last 24 hours")

    avg_pollution_level = sum([d.pollution_level for d in data]) / len(data)

    return {"average_pollution_level": avg_pollution_level, "sensor_count": len(data)}


@router.post("/api/sensor_data")
def add_sensor_data(sensor_id: int, pollution_level: float, db: Session = Depends(get_db)):
    """
    Add new sensor data.
    """
    if not sensor_id or pollution_level is None:
        raise HTTPException(status_code=400, detail="Missing required fields")

    new_data = SensorData(
        sensor_id=sensor_id,
        time=datetime.utcnow(),
        pollution_level=pollution_level
    )

    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return {"message": "Sensor data added successfully", "id": new_data.id}
