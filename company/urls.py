from django.urls import path
from .views import add_company, view_company

urlpatterns = [
    path('view-company', view_company, name='view_company'),
    path('add-company', add_company, name='add_company'),
]
