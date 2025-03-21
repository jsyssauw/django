from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
# STEP 83 create the profile class Mixin(models.Model)
#    In essence, we could actually leverage and extend the user table / model, but this entails specific risks. the user table is a build in table and has a lot of dependencies on it. (e.g. django authentification). Therefore we create a single 



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)     ## if the user is deleted, the related profile is deleted
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)  
    username = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=1000, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True, default="profiles/user-default.png")       ## by default it goes to static/image
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)           # upon creation timestamp created
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)                   #by default (if ID is not specified django will create an autoincrement ID)    
    

    def __str__(self):              ## action 30 - when we display the model, we want to show the titles
        return str(self.user.username) if self.user.username else "Unkown User"