from django.contrib import admin
from .models import Application, JobPosting

# Register your models here.
admin.site.register(JobPosting)
admin.site.register(Application)