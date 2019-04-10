# Generated by Django 2.0.2 on 2019-04-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('cap', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('cmp', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('change', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('stocks_offered', models.IntegerField(default=0)),
                ('stocks_remaining', models.IntegerField(default=models.IntegerField(default=0))),
                ('cap_type', models.CharField(blank=True, choices=[('small', 'Small Cap'), ('mid', 'Mid Cap'), ('large', 'Large Cap')], max_length=20, null=True)),
                ('industry', models.CharField(blank=True, max_length=120, null=True)),
                ('temp_stocks_bought', models.IntegerField(default=0)),
                ('temp_stocks_sold', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['cap_type', 'code'],
            },
        ),
    ]