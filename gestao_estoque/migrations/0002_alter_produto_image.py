# Generated by Django 5.1.2 on 2024-10-27 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(upload_to='produtos/'),
        ),
    ]
