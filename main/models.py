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
      
      

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    short_description = models.TextField()
    description = models.TextField()

    technologies = models.CharField(
        max_length=500,
        help_text="Separate technologies with commas."
    )

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)

    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title
      
      
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject}"