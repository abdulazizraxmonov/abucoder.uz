# portfolio/admin.py
from django.contrib import admin
from .models import Skill, Project, Category, Resume, About

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Resume)
admin.site.register(About)


