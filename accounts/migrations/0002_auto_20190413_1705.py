# Generated by Django 2.0.2 on 2019-04-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cash',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=20),
        ),
    ]
