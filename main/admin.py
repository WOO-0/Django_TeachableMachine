from django.contrib import admin
from .models import TrainingImages, TrainingList

# Register your models here.

class TrainingImageInline(admin.TabularInline):
    model = TrainingImages
    extra = 3

class TrainingImageAdmin(admin.ModelAdmin):
    inlines = [TrainingImageInline]

admin.site.register(TrainingList, TrainingImageAdmin)