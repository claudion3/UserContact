# Generated by Django 3.2 on 2021-04-21 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_contact_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
