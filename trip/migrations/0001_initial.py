# Generated by Django 2.0.5 on 2018-06-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('resid', models.IntegerField(db_column='Resid', primary_key=True, serialize=False)),
                ('rescountry', models.CharField(blank=True, db_column='ResCountry', max_length=200, null=True)),
                ('resarea', models.CharField(blank=True, db_column='ResArea', max_length=200, null=True)),
                ('restype', models.CharField(blank=True, db_column='ResType', max_length=200, null=True)),
                ('resname', models.CharField(blank=True, db_column='ResName', max_length=200, null=True)),
                ('mealtime', models.CharField(blank=True, db_column='MealTime', max_length=500, null=True)),
                ('tel', models.CharField(blank=True, max_length=200, null=True)),
                ('remainingseats', models.IntegerField(blank=True, db_column='RemainingSeats', null=True)),
                ('rads', models.CharField(blank=True, db_column='Rads', max_length=200, null=True)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'restaurant',
                'managed': False,
            },
        ),
    ]
