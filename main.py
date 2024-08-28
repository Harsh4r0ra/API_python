from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import json
import os

app = FastAPI()

# Paths to JSON files
DRIVERS_FILE = 'drivers.json'
ADMINS_FILE = 'admins.json'
THREEPL_FILE = '3pl.json'

class Driver(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    address: str
    truck_name: str
    destinations: List[str]
    sos_calls: int

class Admin(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    company_name: str

class ThreePL(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    company_name: str

def ensure_file_exists(file_path: str):
    """Ensure the JSON file exists; create it if not."""
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file, indent=4)

def read_data(file_path: str) -> List[Dict]:
    """Read data from a JSON file."""
    ensure_file_exists(file_path)
    with open(file_path, 'r') as file:
        return json.load(file)

def write_data(file_path: str, data: List[Dict]):
    """Write data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Driver Endpoints
@app.post("/drivers/")
async def add_driver(driver: Driver):
    drivers = read_data(DRIVERS_FILE)
    drivers.append(driver.dict())
    write_data(DRIVERS_FILE, drivers)
    return driver

@app.delete("/drivers/{phone_number}")
async def remove_driver(phone_number: str):
    drivers = read_data(DRIVERS_FILE)
    updated_drivers = [driver for driver in drivers if driver['phone_number'] != phone_number]
    if len(updated_drivers) == len(drivers):
        raise HTTPException(status_code=404, detail="Driver not found")
    write_data(DRIVERS_FILE, updated_drivers)
    return {"message": "Driver removed successfully"}

@app.get("/drivers/{phone_number}")
async def view_driver(phone_number: str):
    drivers = read_data(DRIVERS_FILE)
    for driver in drivers:
        if driver['phone_number'] == phone_number:
            return driver
    raise HTTPException(status_code=404, detail="Driver not found")

# Admin Endpoints
@app.post("/admins/")
async def add_admin(admin: Admin):
    admins = read_data(ADMINS_FILE)
    admins.append(admin.dict())
    write_data(ADMINS_FILE, admins)
    return admin

@app.delete("/admins/{phone_number}")
async def remove_admin(phone_number: str):
    admins = read_data(ADMINS_FILE)
    updated_admins = [admin for admin in admins if admin['phone_number'] != phone_number]
    if len(updated_admins) == len(admins):
        raise HTTPException(status_code=404, detail="Admin not found")
    write_data(ADMINS_FILE, updated_admins)
    return {"message": "Admin removed successfully"}

@app.get("/admins/{phone_number}")
async def view_admin(phone_number: str):
    admins = read_data(ADMINS_FILE)
    for admin in admins:
        if admin['phone_number'] == phone_number:
            return admin
    raise HTTPException(status_code=404, detail="Admin not found")

# 3PL Endpoints
@app.post("/3pl/")
async def add_3pl(threepl: ThreePL):
    threepl_list = read_data(THREEPL_FILE)
    threepl_list.append(threepl.dict())
    write_data(THREEPL_FILE, threepl_list)
    return threepl

@app.delete("/3pl/{phone_number}")
async def remove_3pl(phone_number: str):
    threepl_list = read_data(THREEPL_FILE)
    updated_threepl = [threepl for threepl in threepl_list if threepl['phone_number'] != phone_number]
    if len(updated_threepl) == len(threepl_list):
        raise HTTPException(status_code=404, detail="3PL personnel not found")
    write_data(THREEPL_FILE, updated_threepl)
    return {"message": "3PL personnel removed successfully"}

@app.get("/3pl/{phone_number}")
async def view_3pl(phone_number: str):
    threepl_list = read_data(THREEPL_FILE)
    for threepl in threepl_list:
        if threepl['phone_number'] == phone_number:
            return threepl
    raise HTTPException(status_code=404, detail="3PL personnel not found")
