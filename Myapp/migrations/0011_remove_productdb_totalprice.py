# Generated by Django 4.1.2 on 2022-12-10 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0010_productdb_totalprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdb',
            name='TotalPrice',
        ),
    ]