from django.contrib.gis.forms import PointField
from rest_framework import serializers

from datamanagement.models import ChildData


class ChildDataSerialiser(serializers.ModelSerializer):
    location = PointField()

    class Meta:
        model = ChildData
        fields = "__all__"

    def validate(self, attrs):
        if (not attrs.get("parent_id") or attrs.get("parent_id") == "") and attrs.get("is_orphan") is False:
            raise serializers.ValidationError("Non Orphan child must register with parent details")
        return super(ChildDataSerialiser, self).validate(attrs)
