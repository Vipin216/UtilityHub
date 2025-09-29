from django.db import models

class GPA(models.Model):
    credit = models.IntegerField()
    grade = models.CharField()
    
