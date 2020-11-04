# Generated by Django 3.1.2 on 2020-11-04 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infodesk', '0005_auto_20201104_0559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='hood',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='infodesk.neighbourhoods'),
        ),
    ]