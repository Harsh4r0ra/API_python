# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

# Define paths for JSON storage
DATA_FILE = "data.json"

# Initialize JSON file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump({"drivers": [], "admins": [], "3pl": []}, file)

# Models
class Driver(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    address: str
    truck_name: str
    destinations: list
    sos_calls: int

class Admin(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    company_name: str

class ThirdPartyLogistics(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    company_name: str


# Helper functions
def read_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def write_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Routes for Drivers
@app.post("/drivers/")
def add_driver(driver: Driver):
    data = read_data()
    data["drivers"].append(driver.dict())
    write_data(data)
    return {"message": "Driver added successfully"}

@app.delete("/drivers/{phone_number}")
def delete_driver(phone_number: str):
    data = read_data()
    data["drivers"] = [driver for driver in data["drivers"] if driver["phone_number"] != phone_number]
    write_data(data)
    return {"message": "Driver deleted successfully"}


# Routes for Admins
@app.post("/admins/")
def add_admin(admin: Admin):
    data = read_data()
    data["admins"].append(admin.dict())
    write_data(data)
    return {"message": "Admin added successfully"}

@app.delete("/admins/{phone_number}")
def delete_admin(phone_number: str):
    data = read_data()
    data["admins"] = [admin for admin in data["admins"] if admin["phone_number"] != phone_number]
    write_data(data)
    return {"message": "Admin deleted successfully"}


# Routes for 3PL Personnel
@app.post("/3pl/")
def add_3pl(personnel: ThirdPartyLogistics):
    data = read_data()
    data["3pl"].append(personnel.dict())
    write_data(data)
    return {"message": "3PL personnel added successfully"}

@app.delete("/3pl/{phone_number}")
def delete_3pl(phone_number: str):
    data = read_data()
    data["3pl"] = [person for person in data["3pl"] if person["phone_number"] != phone_number]
    write_data(data)
    return {"message": "3PL personnel deleted successfully"}
