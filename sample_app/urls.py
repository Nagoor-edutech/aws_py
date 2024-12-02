from django.urls import path
from . import views
import flask

urlpatterns=[
    path('',views.index,name='index')
    
]
