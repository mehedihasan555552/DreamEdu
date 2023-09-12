from django.db import models
from django.contrib.auth.models import User

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
    



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name
    


class applyType(models.TextChoices):
    language = 'Chinese language/Diploma'
    Bachelor = 'Bachelor'
    Masters = 'Masters'
    Phd = 'Ph.D'




class Apply(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    applytype = models.CharField(
        max_length=30,
        choices=applyType.choices,
        default=applyType.Bachelor
    )
    address = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    passport = models.FileField(upload_to = 'images/file/% Y/% m/% d/')
    photo = models.FileField(upload_to = 'images/file/% Y/% m/% d/')
    police_clearance = models.FileField(upload_to = 'images/file/% Y/% m/% d/')
    bank_statement = models.FileField(upload_to = 'images/file/% Y/% m/% d/')
    stady_plan = models.FileField(upload_to = 'images/file/% Y/% m/% d/')
    higher_secondary = models.FileField(upload_to = 'images/file/% Y/% m/% d/')
    other = models.FileField(upload_to = 'images/file/% Y/% m/% d/',null=True,blank=True)


    def __str__(self):
        return self.first_name
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    blog_pic = models.ImageField(default='default.jpg',null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name='blog_author',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ('-created_at',)


    def __str__(self):
        return self.title
    




class EmailSubscription(models.Model):
    email = models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    



class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    Picture = models.ImageField(default='default.jpg',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name