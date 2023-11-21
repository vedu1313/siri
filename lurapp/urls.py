from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name="home"),
    path('index/',views.index),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('services/',views.service,name="service"),
    path('contactus/',views.contactus,name="contactus")
]

