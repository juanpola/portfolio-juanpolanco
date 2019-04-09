from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)   
    company = models.CharField(max_length=100, null=False, blank=False, unique=True)
    location = models.CharField(max_length=100, null=False, blank=False, unique=True)
    start_date = models.CharField(max_length=100, null=False, blank=False, unique=True)
    end_date = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.CharField(max_length=2000, null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.title)


    

    
