from django.contrib.gis.db import models

# Create your models here.
from datamanagement.models import User


class Complaint(models.Model):
    STATUS_CHOICE = (
        ("submitted", "Submitted"),
        ("in_review", "In Review"),
        ("in_action", "In Action"),
        ("declined", "Declined"),
        ("done", "Done")
    )
    TYPE_CHOICE = (
        ("app", "App"),
        ("twitter", "Twitter")
    )
    created_on = models.DateTimeField(auto_created=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICE, default="submitted")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="complaints", default="not-available.png")
    loaction = models.PointField(srid=4326)
    type = models.CharField(default="app", choices=TYPE_CHOICE, max_length=7)
    declining_reason = models.TextField(blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)
    reported_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

