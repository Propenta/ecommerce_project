from django.contrib import admin
from .models import *

# Register your models here.
class AdminArticle(admin.ModelAdmin):
    list_display = ('nom', 'description', 'prix', 'quantite_stock', 'image')
    search_fields = ('nom', 'prix')

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'last_name', 'first_name', 'email',)
    search_fields = ('username', 'email',)


admin.site.register(Article, AdminArticle)
admin.site.register(Utilisateur, UtilisateurAdmin)