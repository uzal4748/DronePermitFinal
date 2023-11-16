from django.urls import path, include
from .views import *

urlpatterns = [
    path('payment/', payment, name='payment'),
    #path('signup/', signup, name='signup'),
]