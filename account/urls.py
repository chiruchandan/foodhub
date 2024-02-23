from django.urls import path
from account import views

urlpatterns = [
    path("",views.index),
    path("RegResturant",views.registerResturant,name='RegResturant'),
    path('userreg',views.userRegister,name='userreg'),
]