# Generated by Django 4.0 on 2022-01-19 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс'),
        ),
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_text',
            field=models.CharField(max_length=200, verbose_name='Текст'),
        ),
    ]
