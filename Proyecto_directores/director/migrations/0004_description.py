# Generated by Django 4.0.6 on 2022-07-23 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0003_remove_movie_isbn_alter_movie_sumary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese una descripcion de la pelicula)', max_length=200)),
            ],
        ),
    ]
