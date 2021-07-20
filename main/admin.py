from django.contrib import admin
from .models import TrainingImage, TrainingList

# Register your models here.

class TrainingImageInline(admin.TabularInline):
    model = TrainingImage
    extra = 3

class TrainingImageAdmin(admin.ModelAdmin):
    inlines = (TrainingImageInline,)

admin.site.register(TrainingList, TrainingImageAdmin)