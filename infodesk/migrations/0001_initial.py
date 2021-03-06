# Generated by Django 3.1.2 on 2020-11-03 14:39

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hood_name', models.CharField(max_length=100)),
                ('hood_location', models.CharField(max_length=100)),
                ('occupant_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='public_amenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity_name', models.CharField(max_length=200)),
                ('tel_number', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infodesk.neighbourhoods')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infodesk.neighbourhoods')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200)),
                ('business_email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('business_img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infodesk.neighbourhoods')),
            ],
        ),
    ]
