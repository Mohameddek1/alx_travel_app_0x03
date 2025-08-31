from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WelcomeView, ListingViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('api/', include(router.urls)),
]
