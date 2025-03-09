
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name ='projects'),
            # step 19: make the project page the home page.
    path('project/<str:pk>/', views.project, name ='project'),
    path('create-project/', views.createProject, name ='create-project'),       ## action 43
    path('update-project/<str:pk>/', views.updateProject, name ='update-project'),       ## action 51
    path('delete-project/<str:pk>/', views.deleteProject, name ='delete-project'),       ## action 51
]