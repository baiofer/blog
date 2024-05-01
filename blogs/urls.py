from django.urls import path  # type: ignore
from .views import ArticleList, ArticleDetail, CommentList, CommentDetail
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/articles/', ArticleList.as_view(), name='article_list'),
    path('api/articles/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('api/comments/', CommentList.as_view(), name='comment_list'),
    path('api/comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
    path('comments/<int:pk>/', views.comment_detail, name='comment_detail'),
]
