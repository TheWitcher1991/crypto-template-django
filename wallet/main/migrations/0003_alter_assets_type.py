# Generated by Django 4.2.6 on 2023-10-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_assets_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='type',
            field=models.IntegerField(verbose_name='Тип изменения'),
        ),
    ]