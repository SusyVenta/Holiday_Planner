# Generated by Django 3.0.8 on 2020-07-11 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

# django uses Object-Relational Mapping: creates model that ca n be used with any database configured. Can change db
# and code stays same. using sqlite for dev, postgres for prod. can represent data with classes == models.


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]