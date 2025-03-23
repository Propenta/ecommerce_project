from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('catalogue/', catalogue, name='catalogue'),
    path('article/<int:article_id>/', detail_article, name='detail_article')
]
