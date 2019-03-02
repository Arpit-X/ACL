from django.contrib import admin

# Register your models here.

from datamanagement.models import User, Organisations, ChildData
from django.contrib.gis import admin as gis_admin
from django.contrib.gis import forms
from django.contrib.gis.db import models

class YourClassAdminForm(forms.ModelForm):
    birth_location = forms.PointField(widget=forms.OSMWidget(attrs={
            'display_raw': True}))

class YourClassAdmin(gis_admin.GeoModelAdmin):
    form = YourClassAdminForm


gis_admin.site.register(ChildData, YourClassAdmin)
admin.site.register(User)
admin.site.register(Organisations)
# admin.site.register(ChildData)