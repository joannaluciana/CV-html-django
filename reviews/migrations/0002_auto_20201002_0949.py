# Generated by Django 3.0.5 on 2020-10-02 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='book',
            new_name='project',
        ),
    ]
