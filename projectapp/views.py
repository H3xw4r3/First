from django.shortcuts import render, HttpResponse
from .models import Project

# Create your views here.


def index(request):
    return HttpResponse('<h1>Home Page</h1>')
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project' : project
    }
    return render(request, 'project_detail.html', context)
