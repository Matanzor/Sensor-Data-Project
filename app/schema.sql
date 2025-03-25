-- Create the database schema
CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    sensor_id INT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    co2_level DOUBLE PRECISION NOT NULL,
    pm25_level DOUBLE PRECISION NOT NULL,
    pm10_level DOUBLE PRECISION NOT NULL
);

-- Create an index for fast querying based on timestamp and sensor_id
CREATE INDEX idx_sensor_timestamp ON sensor_data (sensor_id, timestamp DESC);


-- As the data will grow over time, we might want to consider partitioning the sensor_data table by time.
-- This helps improve query performance.

-- Example for partitioning by date
--CREATE TABLE sensor_data (
--    id SERIAL PRIMARY KEY,
--    sensor_id INT NOT NULL,
--    timestamp TIMESTAMP NOT NULL,
--    co2_level DOUBLE PRECISION NOT NULL,
--    pm25_level DOUBLE PRECISION NOT NULL,
--    pm10_level DOUBLE PRECISION NOT NULL
--) PARTITION BY RANGE (timestamp);