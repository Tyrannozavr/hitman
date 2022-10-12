from django.contrib import admin
from .models import Technics

admin.site.register(Technics)

# @admin.register(Technics)
# class AdmivTechnics(admin.ModelAdmin):
#     fields = ['name', 'age']
