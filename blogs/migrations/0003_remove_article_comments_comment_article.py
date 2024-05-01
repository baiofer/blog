# Generated by Django 5.0.2 on 2024-04-29 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_article_comment_delete_blog_article_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.article'),
            preserve_default=False,
        ),
    ]
