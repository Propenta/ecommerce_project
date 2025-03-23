from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('catalogue/', catalogue, name='catalogue'),
    path('article/<int:article_id>/', detail_article, name='detail_article'),
    path('inscription/', inscription, name='inscription'),
    path('deconnexion/', auth_views.LogoutView.as_view(next_page='home'), name='deconnexion'),
    path('connexion/', user_login, name='connexion'),
]
