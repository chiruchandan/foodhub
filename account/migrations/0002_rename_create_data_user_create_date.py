# Generated by Django 5.0.1 on 2024-02-23 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='create_data',
            new_name='create_date',
        ),
    ]
