# Generated by Django 4.1.2 on 2022-12-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0009_rename_category_productdb_categoryname'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='TotalPrice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
