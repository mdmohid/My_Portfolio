from django.shortcuts import render

# Create your views here.
# def home(request):
#   return render(request, 'home.html')


from django.shortcuts import render
from .models import Education, SkillCategory, Project


def home(request):
    education = Education.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related("skills")
    featured_projects = Project.objects.filter(
            featured=True
        )

    context = {
        "education": education,
        "skill_categories": skill_categories,
        "featured_projects": featured_projects,
    }

    return render(
        request,
        "home.html",
        context
    )
