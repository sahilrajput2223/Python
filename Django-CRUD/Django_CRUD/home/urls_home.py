from django.urls import path
from . import views
app_name = "Home"

urlpatterns = [
    path('addUser', views.addUserDetails, name = "addUser"),
    path('allUser', views.allUser, name = "allUser"),
]