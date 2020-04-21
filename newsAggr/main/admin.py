from django.contrib import admin
from .models import Headlines

# Register your models here.
class HeadlinesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title",{"fields":["title"]}),
        ("URL",{"fields":["url"]}),
        ("Image",{"fields":["image"]}),
    ]



admin.site.register(Headlines, HeadlinesAdmin)

