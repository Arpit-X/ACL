from django.contrib.gis.forms import PointField
from rest_framework import serializers

from complaints.models import Complaint


class ComplaintSerialiser(serializers.ModelSerializer):
    location = PointField()

    class Meta:
        model = Complaint
        fields = "__all__"
