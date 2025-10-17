from django.shortcuts import render, redirect
from .models import SiteSettings, Experience, Education, Project
from .forms import ContactForm

def index(request):
    settings = SiteSettings.objects.first()
    experiences = Experience.objects.all().order_by("order")
    educations = Education.objects.all().order_by("order")
    projects = Project.objects.all().order_by("-featured")
    return render(request, "portfolio/index.html", {
        "settings": settings,
        "experiences": experiences,
        "educations": educations,
        "projects": projects
    })

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ContactForm()
    return render(request, "portfolio/contact.html", {"form": form})
