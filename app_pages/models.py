from django.db import models

class About(models.Model):
    fullname = models.CharField(max_length=255)
    description = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    image = models.ImageField(upload_to='skills/', blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    skills = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Resume(models.Model):
    name = models.CharField(max_length=255)
    work = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    year_of_birth = models.DateField()
    photo = models.ImageField(upload_to='photos/')
    place_of_birth = models.CharField(max_length=255)
    project = models.ManyToManyField(Project)
    technical_skills = models.TextField()
    soft_skills = models.TextField()
    education = models.TextField()
    languages = models.TextField()
    certificates = models.TextField()
    download_resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
