# Generated by Django 3.1.3 on 2022-01-16 20:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biblioapp', '0006_auto_20220116_2148'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pedido',
            new_name='Reserva',
        ),
    ]
