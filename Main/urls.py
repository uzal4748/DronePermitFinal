from django.urls import path,include
from . import views
from .views import *

app_name = 'Main'

urlpatterns = [
    path('',views.home_page, name="home"),
    path('dronepermit',views.dronepermit.as_view(), name="dronepermit"),
    # path('dronepermit',views.drone_permit, name="dronepermit"),
    # path('userprofile/',views.userprofile, name="userprofile"),
    path('userprofile/<int:owner_id>',userprofile, name="userprofile"),
    path('permits/', permits, name='permits'),
    path('update_status/', views.update_status, name='update_status'),
    # path('signin/', views.signin, name='signin'),
    # path('signup', views.signup, name='signup'),
]