# Generated by Django 4.1.7 on 2023-04-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_myusermodel_pfp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusermodel',
            name='pfp',
            field=models.ImageField(default='../media/images/users/default.jpg', null=True, upload_to='images/users/'),
        ),
    ]
