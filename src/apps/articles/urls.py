from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCreateView


app_name = "articles"

urlpatterns = [
    path("list", ArticleListView.as_view(), name="article_list"),
    path("detail/<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
    path("create", ArticleCreateView.as_view(), name="article_create"),
]
