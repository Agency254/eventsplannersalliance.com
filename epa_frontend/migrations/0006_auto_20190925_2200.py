# Generated by Django 2.2.5 on 2019-09-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epa_frontend', '0005_auto_20190925_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='status',
            field=models.CharField(choices=[('booked', 'booked'), ('available', 'available')], default='available', max_length=50),
        ),
    ]
