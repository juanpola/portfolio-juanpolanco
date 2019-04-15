from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100, blank=True)   
    company = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(max_length=100, blank=True)
    end_date = models.CharField(max_length=100, blank=True )
    description = models.CharField(max_length=2000, blank=True)
    destwo = models.CharField(max_length=2000, blank=True, default='SOME STRING')
    desthree = models.CharField(max_length=2000, blank=True, default='SOME STRING')
    desfour = models.CharField(max_length=2000, blank=True, default='SOME STRING')
    desfive = models.CharField(max_length=2000, blank=True, default='SOME STRING')
    dessix = models.CharField(max_length=2000, blank=True, default='SOME STRING')
    desseven = models.CharField(max_length=2000, blank=True, default='SOME STRING')
    deseight = models.CharField(max_length=2000,blank=True, default='SOME STRING')
    desnine = models.CharField(max_length=2000, blank=True, default='SOME STRING')
    desten = models.CharField(max_length=2000, blank=True, default='SOME STRING')


    def __str__(self):
        return str(self.title)


    
class Project(models.Model):
    title = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(blank=True)
    url = models.URLField(max_length=300, blank=True,)


    def __str__(self):
        return str(self.title)



class Skill(models.Model):
    skillone = models.CharField(max_length=100)
    skilltwo = models.CharField(max_length=100)
    skillthree = models.CharField(max_length=100)
    skillfour = models.CharField(max_length=100)
    skillfive = models.CharField(max_length=100)
    skillsix = models.CharField(max_length=100)
    skillseven = models.CharField(max_length=100)
    skilleight = models.CharField(max_length=100)
    skillnine = models.CharField(max_length=100)
    skillten = models.CharField(max_length=100)
    skilleleven = models.CharField(max_length=100)
    skilltwelve = models.CharField(max_length=100)


class Education(models.Model):
    one = models.CharField(max_length=300, blank=True)
    two = models.CharField(max_length=300, blank=True)
    three = models.CharField(max_length=300, blank=True)


class Contact(models.Model):
    phone = models.CharField(max_length=50 )
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100, default='address')
