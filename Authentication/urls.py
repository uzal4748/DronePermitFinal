from django.urls import path, include
from .views import *
from Main.views import permits

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('user_view/', user_view, name='user'),
    path('officer_view/', permits, name='officer'),
    path('logout/', logout, name='logout'),
]