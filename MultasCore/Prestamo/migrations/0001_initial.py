# Generated by Django 3.2.7 on 2022-01-19 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dispositivos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechainicio', models.DateField()),
                ('fechafin', models.DateField()),
                ('fechaentrega', models.DateField(null=True)),
                ('Usuario', models.CharField(max_length=25)),
                ('Estado', models.CharField(max_length=25)),
                ('Fdispositivo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Dispositivos.dispositivos')),
            ],
        ),
    ]