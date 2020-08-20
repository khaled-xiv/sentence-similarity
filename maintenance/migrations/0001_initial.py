# Generated by Django 3.0.3 on 2020-08-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'components',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=30)),
                ('commissioned_on', models.DateTimeField()),
                ('code', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'equipments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('error_code', models.CharField(max_length=10)),
                ('dateTime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'errors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Failure',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comp', models.CharField(max_length=50)),
                ('dateTime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'failures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comp', models.CharField(max_length=50)),
                ('dateTime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'maintenances',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Telemetry',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('volt', models.FloatField()),
                ('rotate', models.FloatField()),
                ('pressure', models.FloatField()),
                ('vibration', models.FloatField()),
                ('dateTime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'telemetries',
                'managed': False,
            },
        ),
    ]
