# Generated by Django 3.1.2 on 2022-01-20 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20220120_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='name',
            field=models.CharField(default='Annonymous', max_length=255),
        ),
    ]
