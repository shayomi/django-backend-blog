# Generated by Django 3.1.2 on 2021-12-20 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
