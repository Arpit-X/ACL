from django.contrib import admin

# Register your models here.

from datamanagement.models import User

admin.site.register(User)