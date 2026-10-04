from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Education, SkillCategory, Skill, Project, ContactMessage


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "degree",
        "institution",
        "university",
        "start_year",
        "end_year",
        "order",
    )

    list_editable = ("order",)


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "order",
    )

    list_editable = ("order",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "level",
        "order",
    )

    list_filter = ("category",)
    list_editable = ("level", "order")
    
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "featured",
        "order",
        "created_at",
    )

    list_filter = ("featured",)

    list_editable = (
        "featured",
        "order",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }
    
    
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    list_editable = ("is_read",)

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    readonly_fields = ("created_at",)

    ordering = ("-created_at",)