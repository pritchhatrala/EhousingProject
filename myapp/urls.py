from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("", views.index, name="index"),
    path("complaint/", views.complaint, name="complaint"),
    path("contact/", views.contact, name="contact"),
    path("renthouse/", views.renthouse, name="renthouse"),
    path("sellhouse/", views.sellhouse, name="sellhouse"),
    path('all-sellhouse/', views.all_sellhouse, name="all_sellhouse"),  
    path('all-renthouse/', views.all_renthouse, name="all_renthouse"),
]
