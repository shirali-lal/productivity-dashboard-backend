# Productivity Management Dashboard Backend API

This is a backend API for a Productivity Management Dashboard built using Django and Django REST Framework.

## Features
- JWT Authentication
- Task CRUD operations
- Task filtering by status and priority
- Overdue task handling
- Productivity dashboard summary
- Secure user-based data access

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite Database

## Setup Instructions

1. Clone the repository
git clone https://github.com/yourusername/productivity-dashboard-backend.git

2. Create virtual environment
python -m venv venv

3. Activate virtual environment
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

4. Install dependencies
pip install django djangorestframework djangorestframework-simplejwt

5. Run migrations
python manage.py makemigrations
python manage.py migrate

6. Create admin user
python manage.py createsuperuser

7. Run server
python manage.py runserver

Server runs at http://127.0.0.1:8000/

## API Endpoints

Login:
POST /api/login/

Tasks:
GET /api/tasks/
POST /api/tasks/
PUT /api/tasks/{id}/
DELETE /api/tasks/{id}/

Dashboard:
GET /api/dashboard/summary/

## Admin Panel
http://127.0.0.1:8000/admin

## Author
Shirali Lal
