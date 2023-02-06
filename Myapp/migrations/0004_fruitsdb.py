# Generated by Django 4.1.2 on 2022-11-14 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_rename_shopvegedb_shopvegdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='fruitsdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FruitsName', models.CharField(blank=True, max_length=50, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Image', models.ImageField(upload_to='profile')),
            ],
        ),
    ]
