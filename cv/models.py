from django.db import models

# Create your models here.

class Education(models.Model):
    title = models.CharField(max_length=200, default='')
    date = models.CharField(max_length=100, default='')
    description = models.TextField()

class Achievement(models.Model):
    title = models.CharField(max_length=200, default='')
    date = models.CharField(max_length=100, default='')

class Skill(models.Model):
    title = models.CharField(max_length=200, default='')

class Course(models.Model):
    title = models.CharField(max_length=200, default='')
