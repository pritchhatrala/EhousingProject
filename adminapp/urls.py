from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
    # login/Logout  url
    path('', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

    # admin page url
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # admin All CRUD section urls
    path('view_renthouses/', views.view_renthouses, name='view_renthouses'),
    path('view_sellhouses/', views.view_sellhouses, name='view_sellhouse'),
    path('view_complaints/', views.view_complaints, name='view_complaints'),

    # delete urls
    path("deletedata/<int:id>/", views.deletedata, name="deletedata"),
    path("deleteRentdata/<int:id>/", views.deleteRentdata, name="deleteRentdata"),
    path("deletecomplaint/<int:id>/", views.deletecomplaint, name="deletecomplaint"),

    # update urls
    path("update_sellhouse/<int:id>/",views.updateSelldata, name="updateSelldata"),
    path("update_renthouse/<int:id>/",views.updateRentdata, name="updateRentdata"),
    path("update_complaintdata/<int:id>/",views.updateComplaintdata, name="updatecomplaintdata"),

]