# Generated by Django 4.1.7 on 2023-12-14 09:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0017_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Bookmark',
        ),
    ]
