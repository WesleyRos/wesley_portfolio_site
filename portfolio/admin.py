from django.contrib import admin
from .models import SiteSettings, Experience, Education, Project, ContactMessage

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "email", "linkedin")

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "start_date", "end_date")
    ordering = ("-start_date", "order")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "start_date", "end_date")
    ordering = ("-start_date", "order")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "sent_at")
