# Generated by Django 3.1.3 on 2021-12-09 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('biblioapp', '0005_auto_20211209_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=25)),
                ('comentario', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('libro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioapp.libro')),
            ],
        ),
    ]
