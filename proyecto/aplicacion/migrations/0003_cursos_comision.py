# Generated by Django 5.0.2 on 2024-03-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_agencias_cursos_usuario_rename_estudiante_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='comision',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]