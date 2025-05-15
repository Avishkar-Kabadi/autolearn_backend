from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    proficiency_level = models.IntegerField(default=0)  # 0 to 100 scale maybe

class Internship(models.Model):
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)  # Applied, Interviewing, Offered, Rejected

class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)  # 0-100%
    last_updated = models.DateTimeField(auto_now=True)

class UserInternship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    application_status = models.CharField(max_length=50)  # Applied, Interviewing, etc.
    notes = models.TextField(blank=True)
