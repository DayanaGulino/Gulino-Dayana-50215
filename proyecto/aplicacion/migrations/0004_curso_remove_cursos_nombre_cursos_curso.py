# Generated by Django 5.0.2 on 2024-03-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_cursos_comision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=48)),
                ('comision', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='nombre',
        ),
        migrations.AddField(
            model_name='cursos',
            name='curso',
            field=models.CharField(default='Curso Predeterminado', max_length=48),
            preserve_default=False,
        ),
    ]
