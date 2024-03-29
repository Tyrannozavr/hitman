# Generated by Django 4.0.5 on 2022-06-29 18:27

import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('1', 'Голова'), ('2', 'Туловище'), ('3', 'Левая рука'), ('4', 'Правая рука'), ('5', 'Левая нога'), ('6', 'Правая нога')], max_length=40), size=3), size=3)),
                ('defend', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('1', 'Голова'), ('2', 'Туловище'), ('3', 'Левая рука'), ('4', 'Правая рука'), ('5', 'Левая нога'), ('6', 'Правая нога')], max_length=40), size=3), size=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
