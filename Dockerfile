# 1. Base Image: Lightweight Python OS
FROM python:3.12-slim

# 2. Environment Variables: Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Work Directory: Inside the container
WORKDIR /app

# 4. Install Dependencies: Copy requirements first to leverage Docker cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Application Code
COPY . /app/

# 6. Expose Port
EXPOSE 8000

# 7. Start Command: Migrate DB, collect static files, then start Gunicorn
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn core.wsgi:application --bind 0.0.0.0:8000"]
