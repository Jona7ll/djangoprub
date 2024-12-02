# Generated by Django 5.1.1 on 2024-11-23 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_tipodiagnostico_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='especialidad',
            field=models.CharField(choices=[('traumatologia', 'Traumatología'), ('cardiovascular', 'Cirugía Cardiovascular'), ('neurocirugia', 'Neurocirugía')], default='traumatologia', max_length=20),
        ),
    ]