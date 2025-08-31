from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


import os
import requests
from dotenv import load_dotenv
from .models import Payment
from .serializers import PaymentSerializer

load_dotenv()

CHAPA_SECRET_KEY = os.getenv('CHAPA_SECRET_KEY')

class WelcomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to ALX Travel App!"})

class PaymentInitiateView(APIView):
    def post(self, request):
        data = request.data
        booking_reference = data.get('booking_reference')
        amount = data.get('amount')
        email = data.get('email')
        payload = {
            "amount": amount,
            "currency": "ETB",
            "email": email,
            "tx_ref": booking_reference,
            "return_url": "https://yourdomain.com/payment/verify/"
        }
        headers = {"Authorization": f"Bearer {CHAPA_SECRET_KEY}"}
        response = requests.post("https://api.chapa.co/v1/transaction/initialize", json=payload, headers=headers)
        resp_data = response.json()
        if resp_data.get('status') == 'success':
            payment = Payment.objects.create(
                booking_reference=booking_reference,
                amount=amount,
                transaction_id=resp_data['data']['tx_ref'],
                status='Pending'
            )
            return Response({
                "checkout_url": resp_data['data']['checkout_url'],
                "payment_id": payment.id
            })
        return Response({"error": resp_data.get('message', 'Payment initiation failed')}, status=400)

class PaymentVerifyView(APIView):
    def get(self, request, tx_ref):
        headers = {"Authorization": f"Bearer {CHAPA_SECRET_KEY}"}
        response = requests.get(f"https://api.chapa.co/v1/transaction/verify/{tx_ref}", headers=headers)
        resp_data = response.json()
        try:
            payment = Payment.objects.get(transaction_id=tx_ref)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=404)
        if resp_data.get('status') == 'success' and resp_data['data']['status'] == 'success':
            payment.status = 'Completed'
            payment.save()
            # TODO: Trigger Celery email task here
            return Response({"message": "Payment successful"})
        else:
            payment.status = 'Failed'
            payment.save()
            return Response({"message": "Payment failed or incomplete"}, status=400)
