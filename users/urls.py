from django.urls import path

from .views import CustomLoginView, signup_view, CustomLogoutView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
