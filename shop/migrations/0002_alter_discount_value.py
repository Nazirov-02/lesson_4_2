# Generated by Django 5.1.5 on 2025-01-19 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
