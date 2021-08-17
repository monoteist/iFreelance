# Generated by Django 3.2.6 on 2021-08-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=250, verbose_name='Заказ')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('views', models.CharField(max_length=50, verbose_name='Просмотры')),
                ('responses', models.CharField(max_length=50, verbose_name='Отклики')),
                ('time', models.CharField(max_length=50, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]