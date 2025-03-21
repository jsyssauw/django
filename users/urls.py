from django.urls import path                       ## STEP 81: create this file
from . import views                             

urlpatterns = [
    path('', views.profiles, name ='profiles'),
]