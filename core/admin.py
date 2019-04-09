from django.contrib import admin
from core.models import Job

# Register your models here.
@admin.register(Job)
class DeckAdmin(admin.ModelAdmin):
    pass
