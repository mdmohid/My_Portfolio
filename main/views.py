from django.shortcuts import render

# Create your views here.
# def home(request):
#   return render(request, 'home.html')


from django.shortcuts import render
from django.contrib import messages
from .models import Education, SkillCategory, Project
from .forms import ContactForm


def home(request):
    education = Education.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related("skills")
    featured_projects = Project.objects.filter(
            featured=True
        )
    if request.method == "POST":
            form = ContactForm(request.POST)
    
            if form.is_valid():
                form.save()
    
                messages.success(
                    request,
                    "Thank you for your message! I'll get back to you as soon as possible."
                )
    
                form = ContactForm()
    else:
            form = ContactForm()
    

    context = {
        "education": education,
        "skill_categories": skill_categories,
        "featured_projects": featured_projects,
        'form' : form
    }

    return render(
        request,
        "home.html",
        context
    )
