from django.shortcuts import render
from .models import Job, Project, Skill, Education, Contact
from django.shortcuts import render, get_object_or_404
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
    # Job_detail = get_object_or_404(Project, pk=job_id)
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context=context)

# def projectDetail(request, project_id):
#     project_detail = get_object_or_404(Project, pk=project_id)
#     return render(request, 'project_detial.html', {'project': project_detail})