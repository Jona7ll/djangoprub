# Generated by Django 5.1.1 on 2024-11-29 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_tipodiagnostico_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipodiagnostico',
            options={'ordering': ['especialidad', 'nombre']},
        ),
    ]