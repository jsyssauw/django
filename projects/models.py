from django.db import models
import uuid
from users.models import Profile #step 83:
# Create your models here.

class Project(models.Model):
    owner =models.ForeignKey(Profile,null=True, blank=True, on_delete=models.SET_NULL)  #step 83.6: add the owner to the model, on delete don't delete the project
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)       # null = True - description can be null
                                                                # blank = True - we can submit a form that is null
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")   ## step 57: add the picture to the model
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)             # because the tag definition is below add '' around tag, or remove the '' and move the tag class above
    vote_total = models.IntegerField(default=0,null=True, blank=True)
    vote_ratio = models.IntegerField(default=0,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)           # upon creation timestamp created
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)                   #by default (if ID is not specified django will create an autoincrement ID)

    def __str__(self):              ## action 30 - when we display the model, we want to show the titles
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote'),
    )
    # owner = 
#    project = models.ForeignKey(Project, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)      ## when the origin is deleted ,this record is deleted (could also be nullified)
    body = models.TextField(null=True, blank=True) 
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)           
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)                  

    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True)           
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)                  

    def __str__(self):
        return self.name