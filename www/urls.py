# www/urls.py
from django.urls import path
from .views import home, ArticleList
from .views import ArticleDetail

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
]

