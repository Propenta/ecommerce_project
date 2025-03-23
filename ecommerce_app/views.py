from django.contrib.auth import login, authenticate
from .forms import InscriptionForm
from django.shortcuts import render, get_object_or_404, redirect
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


def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = InscriptionForm()
    return render(request, 'pages/inscription.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'pages/connexion.html', {'form': {'errors': True}})
    else:
        return render(request, 'pages/connexion.html')