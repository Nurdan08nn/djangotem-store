# Generated by Django 5.1.2 on 2024-10-28 16:59

import django.db.models.deletion
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
                ('category_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prise', models.DecimalField(decimal_places=2, max_digits=10)),
                ('have', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('video', models.FileField(blank=True, null=True, upload_to='vid/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
