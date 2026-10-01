from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Education, SkillCategory, Skill


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