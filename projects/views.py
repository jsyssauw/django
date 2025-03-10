from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm          # step 45a - import the ProjectForm

# projectsList = [
#     {
#         'id': '1',
#         'title': 'Ecommerce Website',
#         'description': 'Fully functional ecommerce website'
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio Website',
#         'description': 'A personal website to write articles and display work'
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'An open source project built by the community'
#     },
#     {
#         'id': '4',
#         'title': 'Jan\'s special project',
#         'description': 'Top Secret bananas'
#     }
# ]



def projects(request):
    # return HttpResponse("Here are our products")
    page_name = 'projects.html'     # step 20: add variables to devsearch > projects > views : add variable + add it to the render as a dictionary.
    number = 10
    projects = Project.objects.all()
    # context = {
    #     'page' : page_name,
    #     'number' : number,
    #     'projects' : projectsList
    # }
    context = {
        "projects" : projects,
        "number" : number, 
        "page" : page_name
    }
    return render(request,'projects/projects.html', context)     # step 11: change the request from httpresponse to the template
                                                        # step 18: add the projects/ in the render argument to make sure that we pick the templates from devsearch > projects > templates > projects
                                                        # step 21: add variables to pass in devsearch > projects > views.py and test the if elif in the projects.html

def project(request, pk):
    #return HttpResponse(f"OUR PRODUCT {pk}")
    # projectObj = None
    # for i in projectsList:
    #     if i['id'] == pk:
    #         projectObj = i
    #         print(projectObj)
    # return render(request,'projects/single_project.html', {'project':projectObj})   # step 11: change the request from httpresponse to the template
    #                                                         # step 18: add the projects/ in the render argument to make sure that we pick the templates from devsearch > projects > templates > projects
    projectObj = Project.objects.get(id=pk)
    tags =  projectObj.tags.all()
    return render(request,'projects/single_project.html', {'project':projectObj,'tags':tags})   # step 11: change the request from httpresponse to the template

# Create your views here.
def createProject(request):             # step 42 - create the view
    form = ProjectForm()
    if request.method == 'POST':                            # action 49: let's process the post (note that action="" is in the form itself so redirecting to the same project)
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES)     # is.valid validates if all the mandatory fields are filled or not ... other checks
                                                            # ACTION 64a: add the files to be part of the form by adding request.FILES
        if form.is_valid():                                 # form.save() --> puts it in the database
            form.save()
            return redirect ('projects')
    
    context = {'form':form}                                 # step 45b - add the project form and pass as parameter to render. 
    return render(request, "projects/project_form.html", context)


# Create your views here.
def updateProject(request,pk):             # step 49 create update
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':                            
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES, instance = project)       # ACTION 64b: add the files to be part of the form by adding request.FILES              
        if form.is_valid():                                 
            form.save()
            return redirect ('projects')
    
    context = {'form':form}                                 
    return render(request, "projects/project_form.html", context)

# Create your views here.
def deleteProject(request,pk):             
    project = Project.objects.get(id=pk)
    context = {'object':project}
    
    if request.method == 'POST':                            
        # print(request.POST)
        project.delete()
        return redirect('projects')
    return render(request, "projects/delete_template.html", context)