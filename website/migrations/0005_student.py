# Generated by Django 5.1.4 on 2024-12-13 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_copomapping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
