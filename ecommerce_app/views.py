from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')


def catalogue(request):
    articles = Article.objects.all()
    return render(request, 'pages/catalogue.html', {'articles': articles})


def detail_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'pages/detail_article.html', {'article': article})