# Generated by Django 4.1.7 on 2023-05-12 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_category_alter_post_slug_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(max_length=125, on_delete=django.db.models.deletion.CASCADE, related_name='p_category', to='core.category'),
        ),
    ]
