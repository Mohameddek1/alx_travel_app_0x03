from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from .tasks import send_booking_confirmation_email

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        # Send confirmation email asynchronously
        if hasattr(booking, 'customer') and hasattr(booking.customer, 'email'):
            send_booking_confirmation_email.delay(booking.customer.email, booking.id)

class WelcomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to ALX Travel App!"})
