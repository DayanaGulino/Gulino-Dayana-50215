# Generated by Django 5.0.2 on 2024-03-12 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_cursos_comision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='nombre',
            new_name='curso',
        ),
    ]