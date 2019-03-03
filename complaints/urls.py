from django.urls import path, include
from rest_framework.routers import DefaultRouter
from complaints import views

router = DefaultRouter()
router.register(r'', views.ComplaintViewset)

urlpatterns = [
    path('', include(router.urls)),
]