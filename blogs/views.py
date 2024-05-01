from rest_framework import generics  # type: ignore
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from django.shortcuts import render  # type: ignore
from .forms import ArticleForm, CommentForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_create.html', {'form': form})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=article)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/article_detail.html', {'article': article, 'comments': comments, 'form': form})


def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'blog/comment_detail.html', {'comment': comment})


def home(request):
    return render(request, 'blog/home.html')