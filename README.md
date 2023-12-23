Brief Project Description

View available hotel rooms with details such as room cost and capacity.
Filter and sort rooms by price and capacity.
Search for available rooms within a specified time interval.
Reserve a room after authentication.
View their own reservations.
The superuser (administrator) has the ability to:

Add, delete, and edit rooms through the Django admin panel.
Edit reservation records through the Django admin panel.
Reservations can be canceled by both users and superusers.

Technology Stack
Django: A Python web framework for building applications.
Django Rest Framework (DRF): A Django extension for building APIs.
PostgreSQL: A relational database.
Additional libraries as needed for specific functional requirements.
The project provides a user-friendly registration, authentication, and authorization system, allowing users to interact seamlessly with the hotel room booking system.

Getting Started
To set up the project locally, follow these steps:

Clone the repository.
Install dependencies: pip install -r requirements.txt.
Run migrations: python manage.py migrate.
Start the development server: python manage.py runserver.
API Endpoints
/api/register/: Register a new user. (auth - bearer your_jwt_token)
/api/token/refresh/: Refresh the access token.
/api/room/filter_price/: Get a list of rooms with price filtering (e.g., /api/room/filter_price/?capacity=2).
/api/booking/search/: Search for available rooms.
/api/booking/book/<int:room_id>/: Book a room.
/api/booking/manage/: Manage rooms (list all rooms and reservations).
/api/booking/delete/<int:booking_id>/: Cancel a reservation.
