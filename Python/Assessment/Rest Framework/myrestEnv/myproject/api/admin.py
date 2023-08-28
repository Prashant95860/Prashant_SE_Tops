from django.contrib import admin
from .models import *
# Register your models here.

class Snippetadmin(admin.ModelAdmin):
    list_display = ('id','title','language')
admin.site.register(Snippet,Snippetadmin)
