from django.db import models

#create models here


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    university = models.CharField(max_length=200, blank=True)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-end_year"]

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name="skills"
    )
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name
