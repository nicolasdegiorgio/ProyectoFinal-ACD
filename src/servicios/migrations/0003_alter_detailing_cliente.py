# Generated by Django 4.0.6 on 2022-08-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_alter_detailing_status_alter_detailing_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailing',
            name='cliente',
            field=models.IntegerField(),
        ),
    ]
