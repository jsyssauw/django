from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','featured_image','description','demo_link','source_link','tags']          ## must be fields ! can be "__all__"
                                                                                   ## action 48
                                                                                   ## step 62; add the featured_image in the form