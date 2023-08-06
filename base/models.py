from django.db import models

# Create your models here.
class UniversityNameList(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(default='university_logo.jpg',null=True,blank=True)

    def __str__(self):
        return self.name
    



class StudentsFeedback(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    Picture = models.ImageField(default='default.jpg',null=True,blank=True)
    country = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    



class StudySolution(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    Picture = models.ImageField(default='default.jpg',null=True,blank=True)


    def __str__(self):
        return self.name