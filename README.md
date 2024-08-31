# Airline Booking System API
### This is a simplified airline booking system built using Django and Django REST Framework. The application allows for managing flights and passengers through API endpoints with full CRUD (Create, Retrieve, Update, Delete) functionality.

## Features
* Create, Retrieve, Update, and Delete (CRUD) operations for Flights and Passengers
* API-based application with structured endpoints.
* Easy navigation through the homepage and direct access to API features.

## Prerequisites
-Ensure you have the following installed on your system:
* Python 3.12 or later
* Django 5.1
* Django REST Framework
* Git (to clone the repository)
* A good text/code editor😒.

## Installation
**Step 1: Clone the Repository**  
```
git clone <repository_url>
cd AirlineBookingSystem
```

**Step 2: Set Up a Virtual Environment**
```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**Step 3: Install Dependencies**
```
pip install -r requirements.txt
```

**Step 4: Set Up the Django Project**
- Navigate to the project directory and apply migrations to set up the database.
   ```
   python manage.py makemigrations
   python manage.py migrate
  ```
**Step 5: Create a Superuser**
- If you wish to access the admin panel this is advisable. I mean, you already know that, don't you? 🤦‍♂️🤦‍♂️
```
  python manage.py createsuperuser
```

**Step 6: Run the Development Server**
```
python manage.py runserver
```
- Your server should be running at http://127.0.0.1:8000/.

# Usage
## Homepage
When you navigate to http://127.0.0.1:8000/, you will be greeted with a homepage that provides links to view and manage flights and passengers.

## API Endpoints
### Flights
* List all flights: GET /api/flights/
* Retrieve a flight by ID: GET /api/flights/{id}/
* Create a new flight: POST /api/flights/
 * Request body example:
```
   {
    "flight_number": "AA123",
    "departure": "2024-09-01T14:30:00Z",
    "arrival": "2024-09-01T18:30:00Z",
    "origin": "JFK",
    "destination": "LAX",
    "capacity": 180
}
```
* Update a flight by ID: PUT /api/flights/{id}/
* Delete a flight by ID: DELETE /api/flights/{id}/

## Passengers
* List all passengers: GET /api/passengers/
* Retrieve a passenger by ID: GET /api/passengers/{id}/
* Create a new passenger: POST /api/passengers/
 * Request body example:
```
   {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "phone_number": "123-456-7890",
    "flight": 1  # Replace with a valid flight ID
}
```
* Update a passenger by ID: 'PUT /api/passengers/{id}/'
* Delete a passenger by ID: 'DELETE /api/passengers/{id}/'

## Final Notes
- Ensure that you have at least one flight created before attempting to create passengers, as each passenger must be associated with a flight. 🚥🚥🚥





