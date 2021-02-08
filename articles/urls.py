from django.urls import path, reverse
from .views import ArticleListView 

urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list")
]
