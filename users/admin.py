from django.contrib import admin

## STEP 83 : register the model in admin.py devsearch > users > admin.py

# Register your models here.
from .models import Profile

admin.site.register(Profile)        ## to show the Project model/table in the Admin console