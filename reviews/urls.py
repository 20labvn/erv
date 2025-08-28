from django.urls import path

from .views import home_review, view_review, add_review, list_review

urlpatterns = [
    path('view-review/<id>', view_review, name='view_review'),
    path('add-review', add_review, name='add_review'),
    path('list-review', list_review, name='list_review'),
    path('', home_review, name='home_review'),
]
