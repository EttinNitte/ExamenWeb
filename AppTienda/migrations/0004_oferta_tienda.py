# Generated by Django 2.1.2 on 2018-12-06 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppTienda', '0003_auto_20181205_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='Tienda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppTienda.Tienda'),
        ),
    ]
