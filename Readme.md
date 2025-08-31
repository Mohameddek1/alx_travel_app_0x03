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
ALX Backend Studentssss
- `/redoc/` for Redoc

# Payment Integration with Chapa API

## Setup

1. Duplicate `alx_travel_app_0x01` to `alx_travel_app_0x02`.
2. Add `.env` file with your Chapa API key:
	```
	CHAPA_SECRET_KEY=your_chapa_secret_key_here
	```
3. Install dependencies:
	- python-dotenv
	- requests
	- celery

## Payment Model
- Defined in `listings/models.py`.
- Tracks booking reference, amount, transaction ID, status, timestamps.

## API Endpoints
- **Initiate Payment:** `POST /api/payment/initiate/`
- **Verify Payment:** `GET /api/payment/verify/<tx_ref>/`

## Workflow
1. On booking, initiate payment via Chapa API.
2. Store transaction and set status to Pending.
3. After payment, verify status and update model.
4. On success, send confirmation email (Celery).

## Testing
- Use Chapa sandbox for test payments.
- Check logs and Payment model for status updates.

## Error Handling
- Failed/incomplete payments update status to Failed.

## Next Steps
- Implement Celery email task in `listings/tasks.py`.
- Add booking-payment integration in booking workflow.
