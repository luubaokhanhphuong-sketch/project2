from django.db import models


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    class Meta:
        verbose_name_plural = 'Personal Info'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk and PersonalInfo.objects.exists():
            raise ValueError("Only one PersonalInfo instance allowed")
        super().save(*args, **kwargs)


class Skill(models.Model):
    class Category(models.TextChoices):
        LANGUAGE = 'language', 'Language'
        FRAMEWORK = 'framework', 'Framework'
        TOOL = 'tool', 'Tool'

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=Category.choices)
    proficiency = models.IntegerField(
        blank=True, null=True,
        help_text='1-100, leave blank if not applicable'
    )

    class Meta:
        ordering = ['category', '-proficiency']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    image = models.ImageField(upload_to='projects/', blank=True)
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
