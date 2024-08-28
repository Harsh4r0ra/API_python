import requests

BASE_URL = "http://127.0.0.1:8000"

# Function to view a specific driver by phone number
def view_driver(phone_number):
    url = f"{BASE_URL}/drivers/{phone_number}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Driver data:", response.json())
    else:
        print("Failed to retrieve driver data:", response.status_code, response.json())

# Function to view a specific admin by phone number
def view_admin(phone_number):
    url = f"{BASE_URL}/admins/{phone_number}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Admin data:", response.json())
    else:
        print("Failed to retrieve admin data:", response.status_code, response.json())

# Function to view a specific 3PL personnel by phone number
def view_3pl(phone_number):
    url = f"{BASE_URL}/3pl/{phone_number}"
    response = requests.get(url)
    if response.status_code == 200:
        print("3PL personnel data:", response.json())
    else:
        print("Failed to retrieve 3PL personnel data:", response.status_code, response.json())

# Example usage
if __name__ == "__main__":
    # View driver data
    view_driver("1234567890")

    # View admin data
    view_admin("0987654321")

    # View 3PL personnel data
    view_3pl("1122334455")
