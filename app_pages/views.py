# portfolio/views.py
from django.shortcuts import render, get_object_or_404
from .models import Project, Category

from django.shortcuts import render
from .models import Category, Project, Skill, About

def home(request):
    categories = Category.objects.all()
    projects_by_category = {category: Project.objects.filter(category=category) for category in categories}
    skills = Skill.objects.all()  # Получаем список всех навыков
    about = About.objects.first()  # Предполагаем, что запись всего одна
    return render(request, 'home.html', {'categories': categories, 'projects_by_category': projects_by_category, 'skills': skills, 'about': about})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def category_projects(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    project_list = Project.objects.filter(category=category)
    paginator = Paginator(project_list, 3)  # По 3 проекта на страницу

    page_number = request.GET.get('page')
    try:
        projects = paginator.page(page_number)
    except PageNotAnInteger:
        # Если номер страницы не является целым числом, перенаправляем на первую страницу
        projects = paginator.page(1)
    except EmptyPage:
        # Если страница находится за пределами допустимых значений (например, 9999), отображаем последнюю страницу
        projects = paginator.page(paginator.num_pages)

    categories = Category.objects.all()  # Retrieve categories again
    return render(request, 'category_projects.html', {'category': category, 'projects': projects, 'categories': categories})


from django.shortcuts import render
from .models import Resume

def resume_detail(request):
    resume = Resume.objects.first()  # Получаем первое резюме из базы данных
    return render(request, 'resume_detail.html', {'resume': resume})

from django.shortcuts import render
from .models import Skill

def skill_list(request):
    skills = Skill.objects.all()  # Получаем все объекты Skill из базы данны
    return render(request, 'skill_list.html', {'skills': skills})

def about(request):
    categories = Category.objects.all()
    about = About.objects.first()  # Получаем первый объект About, если он есть
    skills = Skill.objects.all()  # Получаем список всех навыков
    return render(request, 'about.html', {'about': about, 'skills': skills, 'categories': categories})