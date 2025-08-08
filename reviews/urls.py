from django.urls import path
from .views import hello_world  # import hàm view hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),  # gán route / cho hàm hello_world
]
