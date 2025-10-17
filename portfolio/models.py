from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default="Wesley Ros")
    subtitle = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    about_text = models.TextField(blank=True)

    def __str__(self):
        return "Site settings"

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} — {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    details = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.degree} — {self.institution}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
