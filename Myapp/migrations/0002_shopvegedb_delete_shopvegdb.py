# Generated by Django 4.1.2 on 2022-11-12 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shopvegedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VegitableName', models.CharField(blank=True, max_length=50, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Image', models.ImageField(upload_to='profile')),
            ],
        ),
        migrations.DeleteModel(
            name='shopvegdb',
        ),
    ]
