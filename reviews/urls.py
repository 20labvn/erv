from django.urls import path
from .views import home_review

urlpatterns = [
    path('/as', home_review, name='home_review'),
]
