# Generated by Django 2.1.4 on 2019-01-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groot', '0003_similarity_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expire',
            fields=[
                ('expire_idx', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.IntegerField()),
                ('reason', models.TextField()),
                ('accept_date', models.DateTimeField(blank=True, null=True)),
                ('c_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Expire',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Extend',
            fields=[
                ('extend_idx', models.IntegerField(primary_key=True, serialize=False)),
                ('term', models.PositiveIntegerField(default=1)),
                ('status', models.IntegerField()),
                ('reason', models.TextField()),
                ('accept_date', models.DateTimeField(blank=True, null=True)),
                ('c_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Extend',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('update_idx', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.IntegerField()),
                ('reason', models.TextField()),
                ('accept_date', models.DateTimeField(blank=True, null=True)),
                ('c_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Update',
                'managed': False,
            },
        ),
    ]
