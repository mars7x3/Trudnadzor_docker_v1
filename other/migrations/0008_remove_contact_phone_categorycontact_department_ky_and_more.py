# Generated by Django 4.0.5 on 2022-06-08 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0007_alter_categorycontact_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='categorycontact',
            name='department_ky',
            field=models.CharField(max_length=300, null=True, verbose_name='Название службы'),
        ),
        migrations.AddField(
            model_name='categorycontact',
            name='department_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Название службы'),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_ky',
            field=models.CharField(max_length=300, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title_ky',
            field=models.CharField(max_length=300, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Должность'),
        ),
        migrations.CreateModel(
            name='PhoneContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='other.contact', verbose_name='Контакты')),
            ],
        ),
    ]
