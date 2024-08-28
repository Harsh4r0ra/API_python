from fastapi import FastAPI, HTTPException

app = FastAPI()

# Sample data
roles = ["driver", "manager", "admin"]
users = [{"id": 1, "name": "John Doe", "role": "driver"}]
routes = [{"route_id": 1, "start": "Location A", "end": "Location B"}]
sos_calls = []  # To store SOS requests


@app.get("/")
def read_root():
    return {"message": "API is running!"}


# Roles route
@app.get("/roles")
def get_roles():
    return {"roles": roles}


# Users route
@app.get("/users")
def get_users():
    return {"users": users}


# Routes route
@app.get("/routes")
def get_routes():
    return {"routes": routes}


# SOS route
@app.post("/sos")
def sos_request(data: dict):
    sos_calls.append(data)
    return {"message": "SOS request received", "data": data}
