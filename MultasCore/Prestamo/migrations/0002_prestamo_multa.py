# Generated by Django 3.2.7 on 2022-01-26 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prestamo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='Multa',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]