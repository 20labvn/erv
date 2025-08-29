from django.urls import path

from .views import add_comment

urlpatterns = [
    path('add-comment/<int:review_id>', add_comment, name='add_comment'),
]
