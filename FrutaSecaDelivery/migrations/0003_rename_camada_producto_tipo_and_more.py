# Generated by Django 4.2.2 on 2023-06-29 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FrutaSecaDelivery', '0002_rename_entregable_envios_rename_estudiante_micuenta_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='camada',
            new_name='tipo',
        ),
        migrations.RemoveField(
            model_name='mispedidos',
            name='profesion',
        ),
    ]