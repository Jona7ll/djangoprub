# Generated by Django 5.1.1 on 2024-11-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_paciente_rut'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipodiagnostico',
            options={'ordering': ['especialidad', 'nombre']},
        ),
        migrations.AddField(
            model_name='tipodiagnostico',
            name='especialidad',
            field=models.CharField(choices=[('traumatologia', 'Traumatología'), ('cardiovascular', 'Cirugía Cardiovascular'), ('neurocirugia', 'Neurocirugía')], default='traumatologia', max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='genero',
            field=models.CharField(choices=[('', 'Seleccione...'), ('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1),
        ),
    ]
