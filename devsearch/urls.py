"""
URL configuration for devsearch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings                ## step 61 : configuring the media url
from django.conf.urls.static import static

# def homePage(request):
#     return HttpResponse("Hello World")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('projects.urls'))
    # path("", homePage)
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  ## step 61 : configuring the media url
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)  ## step 65 : configuring the static url in urls.py