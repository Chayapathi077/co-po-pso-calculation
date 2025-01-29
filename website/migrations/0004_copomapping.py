# Generated by Django 5.1.4 on 2024-12-09 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_courseoutcome'),
    ]

    operations = [
        migrations.CreateModel(
            name='COPOMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_number', models.CharField(max_length=10)),
                ('po1', models.IntegerField(blank=True, null=True)),
                ('po2', models.IntegerField(blank=True, null=True)),
                ('po3', models.IntegerField(blank=True, null=True)),
                ('po4', models.IntegerField(blank=True, null=True)),
                ('po5', models.IntegerField(blank=True, null=True)),
                ('po6', models.IntegerField(blank=True, null=True)),
                ('po7', models.IntegerField(blank=True, null=True)),
                ('po8', models.IntegerField(blank=True, null=True)),
                ('po9', models.IntegerField(blank=True, null=True)),
                ('po10', models.IntegerField(blank=True, null=True)),
                ('po11', models.IntegerField(blank=True, null=True)),
                ('po12', models.IntegerField(blank=True, null=True)),
                ('pso1', models.IntegerField(blank=True, null=True)),
                ('pso2', models.IntegerField(blank=True, null=True)),
                ('pso3', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
