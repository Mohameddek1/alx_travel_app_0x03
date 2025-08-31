from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'location',
            'price_per_night',
            'available',
            'created_at',
        ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'guest_name',
            'check_in',
            'check_out',
            'created_at',
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'listing',
            'reviewer_name',
            'rating',
            'comment',
            'created_at',
        ]
