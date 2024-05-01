from django.db import models  # type: ignore


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    comment = models.TextField()
    author = models.CharField(max_length=200)
    createDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """ Un blog al que se añadirán entradas """
    comment = models.TextField()
    commentName = models.CharField(max_length=200)
    commentDate = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments'
    )
