# Generated by Django 4.1.7 on 2023-04-19 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_bookmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='bookmark_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='bookmark_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post'),
        ),
    ]
