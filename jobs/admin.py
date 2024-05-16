from django.contrib import admin

from .models import Jobs, Category, Company

admin.site.register(Jobs)
admin.site.register(Category)
admin.site.register(Company)