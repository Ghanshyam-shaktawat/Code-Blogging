# Generated by Django 4.1.7 on 2023-04-01 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_post_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pub_date',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=200), max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'draft'), (1, 'publish')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
