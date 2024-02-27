
from django.urls import path
from vmsapp import views

app_name ='vmsapp'
urlpatterns = [
    path('',views.user_login,name="login"),
    path('signup',views.signup,name="signup"),
    path('user_dashboard/',views.user_dashboard,name="user_dashboard"),
    path('security_department_dashboard',views.security_department_dashboard,name="sd_dashboard"),
    path('vehicle_registration/',views.vehicle_registration,name="vehicle_registration"),
    path('vehicle_listing',views.vehicle_listing,name="vehicle_listing"),
    path('vehicle_list/', views.vehicle_list, name='vehicle_list'),
    path('vehicle_details/<int:vehicle_id>/', views.vehicle_details, name='vehicle_details'),
    path('quality_check/<int:vehicle_id>/',views.quality_check, name='quality_check'),
    path('vehicle_checkout/<int:vehicle_id>/',views.vehicle_checkout, name='vehicle_checkout'),
    path('user_logout/',views.user_logout,name='user_logout'),   
]