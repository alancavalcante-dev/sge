# Generated by Django 5.1.2 on 2024-10-27 01:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(upload_to='')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_estoque.marcaproduto')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_estoque.tipoproduto')),
            ],
        ),
    ]
