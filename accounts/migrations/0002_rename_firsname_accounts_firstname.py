# Generated by Django 3.2.5 on 2021-08-12 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='firsName',
            new_name='firstName',
        ),
    ]