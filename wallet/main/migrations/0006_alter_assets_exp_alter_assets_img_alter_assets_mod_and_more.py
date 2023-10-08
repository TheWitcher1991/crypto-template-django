# Generated by Django 4.2.6 on 2023-10-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_users_alter_transactions_options_assets_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='exp',
            field=models.CharField(max_length=255, verbose_name='Короткое название'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='img',
            field=models.CharField(max_length=255, verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='mod',
            field=models.CharField(max_length=255, verbose_name='Изменение'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='state',
            field=models.CharField(max_length=255, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='type',
            field=models.IntegerField(verbose_name='Тип изменения'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='user',
            field=models.IntegerField(verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='coin',
            field=models.CharField(max_length=255, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='date',
            field=models.CharField(max_length=255, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='sender',
            field=models.IntegerField(verbose_name='Отправитель'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='state',
            field=models.IntegerField(verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='sum',
            field=models.CharField(max_length=255, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='type',
            field=models.IntegerField(verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='user',
            field=models.IntegerField(verbose_name='Получатель'),
        ),
        migrations.AlterField(
            model_name='users',
            name='code',
            field=models.CharField(max_length=255, verbose_name='Ключ подписи'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=255, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='users',
            name='img',
            field=models.CharField(max_length=255, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='users',
            name='lvl',
            field=models.CharField(max_length=255, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=255, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='users',
            name='progress',
            field=models.CharField(max_length=255, verbose_name='Прогресс'),
        ),
        migrations.AlterField(
            model_name='users',
            name='salt',
            field=models.CharField(max_length=255, verbose_name='Соль пароля'),
        ),
    ]