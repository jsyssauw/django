from django.contrib import admin

# Register your models here.
from .models import Project, Review, Tag


admin.site.register(Project)        ## to show the Project model/table in the Admin console
admin.site.register(Review)        ## to show the Project model/table in the Admin console
admin.site.register(Tag)        ## to show the Project model/table in the Admin console