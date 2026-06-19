# DineReserve Hub

## Tech Stack
- Django (Admin Panel)
- FastAPI (API Layer)
- MySQL
- JWT Authentication

## Setup Instructions

### Clone Repository
git clone <repo-url>

### Create Virtual Environment
python -m venv venv

### Activate Environment
venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

### Django Admin
cd django_admin
python manage.py migrate
python manage.py runserver

### FastAPI
cd fastapi_api
uvicorn main:app --reload

## API Endpoints
POST /auth/register
POST /auth/login
GET /branches
GET /tables
POST /reservations
GET /user/reservations
PATCH /reservations/{id}/cancel
