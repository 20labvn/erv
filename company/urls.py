from django.urls import path
from .views import add_company

urlpatterns = [
    path('add-company', add_company, name='add_company'),
]
