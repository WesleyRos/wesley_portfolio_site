from django.contrib import admin
from .models import Profile,Tool,Case,Experience
admin.site.site_header='Portfólio profissional'
admin.site.site_title='Gerenciar portfólio'
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
 def has_add_permission(self,request):return not Profile.objects.exists()
@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
 list_display=('name','category','order');list_filter=('category',)
@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
 list_display=('title','category','published','order');prepopulated_fields={'slug':('title',)};filter_horizontal=('tools',);list_filter=('published',)
admin.site.register(Experience)

from .models import Education,Certificate
admin.site.register(Education)
admin.site.register(Certificate)
