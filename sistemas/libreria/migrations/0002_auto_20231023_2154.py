# Generated by Django 3.2.8 on 2023-10-24 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='image',
        ),
        migrations.AddField(
            model_name='juego',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='juego',
            name='descripcion',
            field=models.TextField(null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='juego',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]
