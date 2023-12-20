from django.contrib import admin
from django.urls import path
from sms import views
from sms.models import Student,Teacher

urlpatterns = [
    path('log',views.login,name="login"),
    path('stud',views.stud,name="stud"),
    path('teach',views.teach,name="teach"),

    


]

