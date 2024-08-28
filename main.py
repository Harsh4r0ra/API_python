from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

# Define the path for the JSON file to store the data
DATA_FILE = "drivers_data.json"

# Driver data model
class Driver(BaseModel):
    first_name: str
    surname: str
    phone_number: str
    address: str
    truck_name: str
    destination_a: str
    destination_b: str
    sos_calls: int = 0

# Initialize the JSON file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Load data from JSON file
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save data to JSON file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Get all drivers
@app.get("/drivers")
def get_drivers():
    return load_data()

# Add a new driver
@app.post("/drivers")
def add_driver(driver: Driver):
    data = load_data()
    data.append(driver.dict())
    save_data(data)
    return {"message": "Driver added successfully"}

# Update driver data
@app.put("/drivers/{phone_number}")
def update_driver(phone_number: str, updated_driver: Driver):
    data = load_data()
    for driver in data:
        if driver["phone_number"] == phone_number:
            driver.update(updated_driver.dict())
            save_data(data)
            return {"message": "Driver updated successfully"}
    raise HTTPException(status_code=404, detail="Driver not found")

# Delete a driver
@app.delete("/drivers/{phone_number}")
def delete_driver(phone_number: str):
    data = load_data()
    new_data = [driver for driver in data if driver["phone_number"] != phone_number]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Driver not found")
    save_data(new_data)
    return {"message": "Driver deleted successfully"}
