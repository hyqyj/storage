# Generated by Django 4.2.3 on 2023-07-11 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='name_text',
        ),
    ]
