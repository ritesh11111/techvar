from django.contrib import admin

# Register your models here.
from . models import Intern
from . models import Company

admin.site.register(Intern)
admin.site.register(Company)