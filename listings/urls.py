from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WelcomeView, ListingViewSet, BookingViewSet, PaymentInitiateView, PaymentVerifyView

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('api/', include(router.urls)),
    path('api/payment/initiate/', PaymentInitiateView.as_view(), name='payment-initiate'),
    path('api/payment/verify/<str:tx_ref>/', PaymentVerifyView.as_view(), name='payment-verify'),
]
