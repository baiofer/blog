from rest_framework import serializers  # type: ignore
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'commentName', 'commentDate', 'article']


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            'title', 'comment', "author", 'createDate',
            'modificationDate', 'comments'
        ]
