# Generated by Django 2.0.5 on 2018-06-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('idattraction', models.IntegerField(db_column='idAttraction', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.CharField(blank=True, max_length=500, null=True)),
                ('addr', models.CharField(blank=True, max_length=1000, null=True)),
                ('imgsrc', models.CharField(blank=True, max_length=1000, null=True)),
                ('officailurl', models.CharField(blank=True, max_length=1000, null=True)),
                ('country_id', models.IntegerField(blank=True, null=True)),
                ('region_id', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'attraction',
                'managed': False,
            },
        ),
    ]