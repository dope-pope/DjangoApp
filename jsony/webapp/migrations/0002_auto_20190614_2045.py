# Generated by Django 2.2.1 on 2019-06-14 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='empID',
            new_name='emp_id',
        ),
    ]
