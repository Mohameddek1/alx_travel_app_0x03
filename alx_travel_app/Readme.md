# README

This directory contains the main code and configuration for the travel booking app with Chapa payment integration and background email notifications using Celery and RabbitMQ.

## Project Overview
This project provides a travel booking API built with Django, Django REST Framework (DRF), and asynchronous email notifications.

## Celery & RabbitMQ Setup
1. Install RabbitMQ server (https://www.rabbitmq.com/download.html)
2. Install Python dependencies:
	```bash
	pip install -r requirements.txt
	```
3. Run migrations:
	```bash
	python manage.py migrate
	```
4. Start Celery worker:
	```bash
	celery -A alx_travel_app worker -l info
	```
5. Configure your SMTP email backend in `settings.py`.

## How it works
- When a booking is created, a confirmation email is sent asynchronously using Celery and RabbitMQ.
- The main request-response cycle is not blocked by email sending.
# alx_travel_app_0x01

This is the root README for the ALX Travel App 0x01 project.

## Project Overview
This project provides a travel booking API built with Django and Django REST Framework (DRF).

### Features
- Listings CRUD
- Bookings CRUD
- API documented with Swagger (drf-yasg)

### Setup
1. Install requirements: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Run server: `python manage.py runserver`

### API Endpoints
- `/api/listings/` - CRUD for listings
- `/api/bookings/` - CRUD for bookings

### Swagger Docs
- `/swagger/` for Swagger UI
- `/redoc/` for Redoc

---

Author: Mohameddeq Ahmed
ALX Backend Student
- `/redoc/` for Redoc
