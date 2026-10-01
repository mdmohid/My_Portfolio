from django.shortcuts import render

# Create your views here.
# def home(request):
#   return render(request, 'home.html')


from django.shortcuts import render
from .models import Education, SkillCategory


def home(request):
    education = Education.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related("skills")

    context = {
        "education": education,
        "skill_categories": skill_categories,
    }

    return render(
        request,
        "home.html",
        context
    )
