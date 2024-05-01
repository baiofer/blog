from django.contrib import admin  # type: ignore
from .models import Article, Comment

# Registrar los modelos
admin.site.register(Article)
admin.site.register(Comment)
