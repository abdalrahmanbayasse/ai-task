from django.urls import path
from .views import send_request

urlpatterns = [
    path('', send_request , name = 'home')
]


