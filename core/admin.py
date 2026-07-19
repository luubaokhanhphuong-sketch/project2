from django.contrib import admin

from .models import PersonalInfo, Project, Skill


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if PersonalInfo.objects.exists():
            return False
        return True


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'created_at')
    search_fields = ('title', 'tech_stack')
