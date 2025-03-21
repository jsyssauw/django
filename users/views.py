from django.shortcuts import render
from .models import Profile                 

# Create your views here.       
def profiles(request):                                  ## step 81 - register the view.
    profiles = Profile.objects.all()
    context = {'profiles': profiles}                  # step 82 - pass the profiles to the template.
    return render(request, 'users/profiles.html',context)