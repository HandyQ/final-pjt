# Generated by Django 3.2.3 on 2021-05-20 02:19

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
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(default=0, max_length=100)),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(max_length=100)),
                ('release_date', models.CharField(max_length=100)),
                ('vote_average', models.FloatField(default=0.0)),
                ('vote_count', models.IntegerField(default=0)),
                ('popularity', models.FloatField(default=0.0)),
            ],
        ),
    ]
