from rest_framework import viewsets
from complaints.models import Complaint
from complaints.serialisers import ComplaintSerialiser


class ComplaintViewset(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerialiser
