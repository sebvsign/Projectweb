# Generated by Django 3.1.2 on 2020-11-10 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectowebApp', '0004_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('etiqueta', models.CharField(max_length=5)),
                ('logo', models.ImageField(upload_to='equipos')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectowebApp.regiones')),
            ],
        ),
    ]
