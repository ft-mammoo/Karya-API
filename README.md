# Karya API - Task Management API

A production-ready Task Management API MVP built with Django REST Framework, featuring JWT authentication, pagination, search, and Swagger UI documentation.

## Features
- **Authentication**: JWT (JSON Web Tokens)
- **Task Management**: Full CRUD operations for tasks
- **Pagination**: Custom page-number pagination
- **Search & Filtering**: Filter by status/priority, search by title/description
- **Documentation**: Swagger UI & ReDoc integrated
- **Security**: CORS headers and environment variables (.env) configured

## Tech Stack
- Python 3.x
- Django & Django REST Framework
- SQLite (Local MVP)
- SimpleJWT
- drf-yasg (Swagger)

## Folder Structure
```text
Karya-API
├── core
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── tasks
    ├── admin.py
    ├── apps.py
    ├── filters.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── pagination.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/ft-mammoo/Karya-API.git
cd Karya-API
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate   # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Copy `.env.dist` to `.env` and configure your settings:
```bash
cp .env.dist .env
```

5. Run migrations and start the server:
```bash
python manage.py migrate
python manage.py runserver
```