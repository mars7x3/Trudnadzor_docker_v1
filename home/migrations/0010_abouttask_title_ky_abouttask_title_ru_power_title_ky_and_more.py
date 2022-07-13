# Generated by Django 4.0.5 on 2022-06-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_about_text_ky_about_text_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='abouttask',
            name='title_ky',
            field=models.CharField(max_length=300, null=True, verbose_name='Название основных задач службы'),
        ),
        migrations.AddField(
            model_name='abouttask',
            name='title_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Название основных задач службы'),
        ),
        migrations.AddField(
            model_name='power',
            name='title_ky',
            field=models.CharField(max_length=300, null=True, verbose_name='Название полномочий'),
        ),
        migrations.AddField(
            model_name='power',
            name='title_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Название полномочий'),
        ),
        migrations.AddField(
            model_name='powertext',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='powertext',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='tasktext',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='tasktext',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
    ]
