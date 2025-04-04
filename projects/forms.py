from django.forms import ModelForm
from django import forms  ##  STEP 75 add this import
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','featured_image','description','demo_link','source_link','tags']          ## must be fields ! can be "__all__"
                                                                                   ## action 48
                                                                                   ## step 62; add the featured_image in the form
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }
        
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter project title'})
        # self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter description'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})