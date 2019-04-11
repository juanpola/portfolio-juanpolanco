from django.shortcuts import render
from .models import Job, Project, Skill, Education, Contact
# Create your views here.


def home(request):
    return render(request, 'index.html')


def resume(request):
    jobs = Job.objects.all()
    skills = Skill.objects.all()
    education = Education.objects.all()
    contact = Contact.objects.all()
    context = {
            'jobs': jobs,
            'skills': skills,
            'education': education,
            'contact': contact,

    }
    return render(request, 'resume.html', context=context)


def project(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context=context)
