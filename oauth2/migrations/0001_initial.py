# Generated by Django 3.2.6 on 2021-09-05 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=300)),
                ('avatar', models.CharField(max_length=300)),
                ('public_flags', models.IntegerField()),
                ('flags', models.IntegerField()),
                ('locale', models.CharField(max_length=300)),
                ('mfa_enabled', models.BooleanField()),
                ('last_login', models.DateTimeField()),
            ],
        ),
    ]
