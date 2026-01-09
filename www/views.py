from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Article
def home(request):
    return HttpResponse("Hello, welcome to the home page!")

# Create your views here.

class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    ordering = ['-published_at']
    
class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_single.html'
    context_object_name = 'article'