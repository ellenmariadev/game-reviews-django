# Generated by Django 4.1.3 on 2022-11-10 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='genre',
        ),
        migrations.AddField(
            model_name='games',
            name='genre',
            field=models.ManyToManyField(to='games.genre'),
        ),
    ]