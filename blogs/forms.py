from django import forms  # type: ignore
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'comment', 'author']
        labels = {
            'title': 'Título',
            'comment': 'Contenido',
            'author': 'Creado por'
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'commentName']
        labels = {
            'comment': 'Comentario',
            'commentName': 'Escrito por'
        }
