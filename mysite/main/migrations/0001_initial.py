# Generated by Django 4.1 on 2022-08-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('is_show_in_main_navigation', models.BooleanField(default=False, verbose_name='В основной навигации')),
                ('is_show_in_social_links', models.BooleanField(default=False, verbose_name='В доп. навигации')),
            ],
            options={
                'verbose_name': 'Категория(ю)',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
    ]
