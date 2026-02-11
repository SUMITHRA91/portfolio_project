from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project

admin.site.register(Project)
from .models import Contact

admin.site.register(Contact)
