# Generated by Django 3.2.18 on 2023-03-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_image', models.ImageField(upload_to='index')),
                ('movie_rating', models.CharField(max_length=50)),
                ('movie_name', models.CharField(max_length=150)),
                ('movie_genre', models.CharField(max_length=100)),
            ],
        ),
    ]