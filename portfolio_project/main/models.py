from django.db import models
from django.db import models

class Project(models.Model):

    CATEGORY_CHOICES = [
        ('Web', 'Web Development'),
        ('AI', 'Artificial Intelligence'),
        ('App', 'Application'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
