from django.urls import path

from .views import add_company, view_company, home_view

urlpatterns = [
    path('view-company/<id>', view_company, name='view_company'),
    path('add-company', add_company, name='add_company'),
    path('', home_view, name='home_view'),
]
