from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField


GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )
GOVT_ID_CHOICES = (
    ("adhaar", "ADHAAR"),
    ("pan", "PAN"),
)


class User(AbstractUser):
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    govt_id_type = models.CharField(choices=GOVT_ID_CHOICES, max_length=6)
    govt_id = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    location = models.PointField(null=True)
    image = models.ImageField()


class Organisations(models.Model):
    ORGANISATION_CHOICES = (
        ("hospital", "Hospital"),
        ("school", "School"),
        ("orphanage", "Orphanage"),
        ("anganwadi", "Anganwadi")
    )
    incharge = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(choices=ORGANISATION_CHOICES, max_length=10)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    location = models.PointField()


class ChildData(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    identification_marks = models.TextField()
    dob = models.DateField()
    parent_contact_no = PhoneNumberField()
    parent_id_type = models.CharField(choices=GOVT_ID_CHOICES, blank=True, null=True, max_length=6)
    parent_id = models.CharField(blank=True, null=True, max_length=15)
    is_orphan = models.BooleanField(default=False)
    orphanage = models.ForeignKey(Organisations, blank=True, null=True, related_name="orphanage", on_delete=models.CASCADE)
    birth_location = models.PointField()
    school = models.ForeignKey(Organisations, blank=True, null=True, related_name="school", on_delete=models.CASCADE)
    enrolled_in_school = models.BooleanField(default=False)
    enrolled_in_orphanage = models.BooleanField(default=False)
    registered_by = models.ForeignKey(Organisations, related_name="registerer", on_delete=models.CASCADE)
