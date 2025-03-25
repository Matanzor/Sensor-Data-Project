# Sensor Data API Project 🌱

This project demonstrates how to build a fast, real-time API for storing and retrieving sensor data, such as air quality levels or CO2 concentrations. The API is built using **FastAPI** and integrates with **PostgreSQL** for efficient storage and querying of time-series data.

## 🚀 Project Overview

The API allows you to:
1. **Add new sensor data** to the database.
2. **Retrieve average pollution levels** from the last 24 hours.

It integrates **FastAPI** with **PostgreSQL** using **SQLAlchemy** for seamless data handling and efficient querying. This project is designed to showcase real-time data handling, database optimization, and API performance.

## 🛠️ Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs.
- **SQLAlchemy**: A SQL toolkit for Python that provides an ORM for database management.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **Uvicorn**: An ASGI server used to run the FastAPI app.
- **Pydantic**: Data validation and settings management using Python type annotations.

## 🧑‍💻 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sensor-data-api.git
cd sensor-data-api
```

### 2. Create and Activate Virtual Environment
If you don’t have a virtual environment setup, create one:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3. Install Dependencies
Install the necessary packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Database Connection
Make sure you set your PostgreSQL database connection in app/config.py. Replace the following with your database credentials:

```bash
SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/sensor_data_db'
```

### 5. Run the Application
To start the FastAPI app, run:

```bash
uvicorn main:app --reload
```
The server will be running at http://localhost:8000.

## 🔧 API Endpoints
### 1. POST /api/sensor_data 📝
Add new sensor data
This endpoint allows you to add new sensor data (e.g., pollution levels) to the database.

Request:
```bash
POST http://localhost:8000/api/sensor_data?sensor_id=1&pollution_level=5.5
```
Query Parameters:
- sensor_id: The ID of the sensor that recorded the data.
- pollution_level: The pollution level (e.g., CO2 concentration) recorded by the sensor.

Response:
```json
{
  "message": "Sensor data added successfully",
  "id": 1
}
```

## 2. GET /api/sensor_data 📊
### Retrieve the average pollution level for the last 24 hours
This endpoint returns the average pollution level recorded by all sensors over the past 24 hours.

Request:
```bash
GET http://localhost:8000/api/sensor_data
```

Response:
```json
{
  "average_pollution_level": 5.2,
  "sensor_count": 50
}
```

## 💡 Key Features
- Real-Time Data: Handles real-time sensor data with FastAPI for fast processing.
- PostgreSQL: Efficient querying and storage of time-series data using PostgreSQL.
- API Endpoints: Provides both POST and GET endpoints for interacting with sensor data.
- Data Validation: Input data is validated using Pydantic, ensuring correct data types and formats.
- Scalability: Optimized to handle large amounts of data efficiently with PostgreSQL.
- 
## 🧑‍🤝‍🧑 Collaboration
Feel free to fork this project, open issues, or submit pull requests for improvements! 🚀

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

Enjoy working with real-time data! 🌱
