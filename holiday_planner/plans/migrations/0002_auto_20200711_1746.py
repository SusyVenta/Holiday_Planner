# Generated by Django 3.0.8 on 2020-07-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
