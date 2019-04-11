from django.contrib import admin
from core.models import Job, Project, Skill, Education, Contact

# Register your models here.
@admin.register(Job)
class Job(admin.ModelAdmin):
    pass


@admin.register(Project )
class Project(admin.ModelAdmin):
    pass

@admin.register(Skill)
class Experience(admin.ModelAdmin):
    pass

@admin.register(Education)
class Education(admin.ModelAdmin):
    pass

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    pass
