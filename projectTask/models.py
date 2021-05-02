from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    duration = models.DurationField(default='')
    photoFileName = models.ImageField(null=True, default=None, blank=True)

class Task(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    startDate = models.DateField(auto_now_add=True)
    endDate = models.DateField(auto_now=False, auto_now_add=False)
    project = models.ForeignKey(to = Project, on_delete=models.CASCADE,related_name="tasks")