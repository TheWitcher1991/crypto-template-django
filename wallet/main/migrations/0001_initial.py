# Generated by Django 4.2.6 on 2023-10-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(max_length=11, verbose_name='Состояние')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('exp', models.CharField(max_length=255, verbose_name='Короткое название')),
                ('img', models.CharField(max_length=255, verbose_name='Иконка')),
                ('mod', models.CharField(max_length=255, verbose_name='Изменение')),
                ('type', models.BooleanField(verbose_name='Тип изменения')),
            ],
            options={
                'verbose_name': 'Актив',
                'verbose_name_plural': 'Активы',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
