from django.contrib import admin
from .models import *

# Register your models here.
class AdminArticle(admin.ModelAdmin):
    list_display = ('nom', 'description', 'prix', 'quantite_stock', 'image')
    search_fields = ('nom', 'prix')

admin.site.register(Article, AdminArticle)