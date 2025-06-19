from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    
    def __str__(self):
        return f"{self.title} at {self.company} | ${self.salary}"
    

from django.contrib.auth.models import User

class Application(models.Model):
    job = models.ForeignKey("JobPosting", on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications", null=True, blank=True)  # new field
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    resume = models.FileField(upload_to="resumes/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application by {self.name} for job {self.job.title}"




# class Application(models.Model):
#     job = models.ForeignKey("JobPosting", on_delete=models.CASCADE, related_name="applications")
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()
#     resume = models.FileField(upload_to="resumes/", null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"Application by {self.name} for job {self.job.title}"
    