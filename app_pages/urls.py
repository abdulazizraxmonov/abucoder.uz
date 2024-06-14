# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_projects, name='category_projects'),
    path('resume/', views.resume_detail, name='resume_detail'),
    path('skills/', views.skill_list, name='skill_list'),
    path('about/', views.about, name='about'),

]
